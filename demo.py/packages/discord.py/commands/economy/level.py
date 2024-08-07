import discord
import json
import traceback
from datetime import datetime
from discord import app_commands, ui
from discord.ext import commands
from typing import Literal, TextIO

class LevelCog(commands.Cog):
  def __init__(self, bot : commands.Bot) -> None:
    self.bot : commands.Bot = bot
    self.experience_gain_amount : int = 5
    self.multiplier : int = 4
    self.interval_threshold : int = 10

  @commands.Cog.listener()
  async def on_message(
    self,
    message : discord.Message
  ) -> None:
    try:
      user : discord.Member = message.author
      file : TextIO = self.load_file('json/level.json')
      user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0, "last_message": None})
      if not user_data["last_message"]:
        user_data["experience"] += self.experience_gain_amount
        user_data["last_message"] = int(datetime.now().timestamp())
        file[str(user.id)].update(user_data)
        self.save_file('json/level.json', file)
      else:
        last_message_timestamp : int = user_data["last_message"]
        current_timestamp : int = int(datetime.now().timestamp())
        if current_timestamp - last_message_timestamp > self.interval_threshold:
          user_data["experience"] += self.experience_gain_amount
          user_data["last_message"] = int(datetime.now().timestamp())
          file[str(user.id)].update(user_data)
          self.save_file('json/level.json', file)
      new_level : int | None = self.level(user.id)
      if new_level and new_level > level:
        await message.reply(
          embed = discord.Embed(
            description = f"Congratulations, {member.mention} ! You levelled up to ` Level {new_level:,} ` !",
            color = 0x2b2d31
          ).set_thumbnail(
            url = member.display_avatar
          ),
          mention_author = False
        )
      if new_level and new_level < level:
        await message.reply(
          embed = discord.Embed(
            description = f"Unfortunately, {member.mention} levelled down to ` Level {new_level:,} `",
            color = 0x2b2d31
          ).set_thumbnail(
            url = member.display_avatar
          ),
          mention_author = False
        )
    except:
      traceback.print_exc()

  level : app_commands.Group = app_commands.Group(
    name = "level",
    description = "/level"
  )

  def get_max_exp(self, file : TextIO, user_id : int) -> int:
    level : int = file.get(str(user_id), {"level": 1, "experience": 0, "last_message": None})["level"]
    max_experience : int = int((level + 1) ** self.multiplier)
    return max_experience

  def level(self, user_id : int) -> int | None:
    file : TextIO = self.load_file('json/level.json')
    user_data : dict[str, int] = file.get(str(user_id), {"level": 1, "experience": 0, "last_message": None})
    level : int = user_data["level"]
    experience : int = user_data["experience"]
    if int(experience ** (1 / self.multiplier)) > level:
      new_level : int = int(experience ** (1 / self.multiplier))
      user_data["level"] : int = new_level if new_level >= 1 else 1
      file[str(user_id)].update(user_data)
      self.save_file('json/level.json', file)
      return new_level if new_level >= 1 else 1
    return None

  def load_file(self, path : str) -> TextIO:
    with open(path, "r") as f:
      file : TextIO = json.load(f)
    return file

  def save_file(self, path : str, file : TextIO) -> None:
    with open(path, "w") as f:
      json.dump(file, f, indentt = 2)

  @level.command(
    name = "info",
    description = "Check a user's current level"
  )
  @app_commands.describe(
    member = "Select another member :"
  )
  async def level_info(self, interaction : discord.Interaction, member : discord.Member | None = None) -> None:
    file : TextIO = self.load_file("json/level.json")
    user : discord.Member = member or interaction.user
    user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0, "last_message": None})
    max_experience : int = self.get_max_exp(file, user.id)
    await interaction.response.send_message(
      embed = discord.Embed(
        description = f"**Level** : ` {user_data["level"]:,} `\n" \
          f"**Experience** : ` {user_data["experience"]:,} | {max_experience:,} `",
        color = 0x2b2d31
      ).set_author(
        name = user.name,
        icon_url = user.display_avatar
      ).set_thumbnail(
        url = user.display_avatar
      ).set_footer(
        text = f"User ID : {user.id}"
      ),
      ephemeral = True
    )

  @level.command(
    name = "add_exp",
    description = "Add experience to a member"
  )
  @app_commands.describe(
    member = "To whom the experience will be added",
    amount = "Amount of experience to add"
  )
  @app_commands.checks.has_role(
    "Levelling Manager"
  )
  async def level_add_experience(
    self,
    interaction : discord.Interaction,
    member : discord.Member,
    amount : app_commands.Range[int, -10_000, 10_000]
  ) -> None:
    if amount == 0:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = "` amount ` parameter cannot be ` 0 `",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      return
    user : discord.Member = member or interaction.user
    file : TextIO = self.load_file('json/level.json')
    user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0, "last_message": None})
    level : int = user_data["level"]
    if amount < 0 and abs(amount) > user_data["experience"]:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = f"Negative ` amount ` cannot be less than ` {user_data["experience"]:,} `",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      return
    user_data["experience"] += amount
    file.update(user_data)
    self.save_file('json/level.json', file)
    new_level : int | None = self.level(user.id)
    embeds = [
      discord.Embed(
        description = f"Successfully gave {member.mention} ` {amount:,} ` Experiences.",
        color = 0x39ff14
      ).set_author(
        name = interaction.client.user.name,
        icon_url = interaction.client.user.display_avatar
      )
    ]
    if new_level and new_level > level:
      embeds.append(
        discord.Embed(
          description = f"Congratulations, {member.mention} ! You levelled up to ` Level {new_level:,} ` !",
          color = 0x2b2d31
        ).set_thumbnail(
          url = member.display_avatar
        )
      )
    if new_level and new_level < level:
      embeds.append(
        discord.Embed(
          description = f"Unfortunately, {member.mention} levelled down to ` Level {new_level:,} `",
          color = 0x2b2d31
        ).set_thumbnail(
          url = member.display_avatar
        )
      )
    await interaction.response.send_message(
      member.mention if new_level else "",
      embeds = embeds
    )

  @level.command(
    name = "rm_exp",
    description = "Remove some experience from a member"
  )
  @app_commands.describe(
    member = "To whose experience to deduct",
    amount = "Amount of experiences to deduct"
  )
  async def level_remove_experience(
    self,
    interaction : discord.Interaction,
    member : discord.Member,
    amount : app_commands.Range[int, -10_000, 10_000]
  ) -> None:
    if amount == 0:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = "` amount ` parameter cannot be ` 0 `",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      return
    user : discord.Member = member or interaction.user
    file : TextIO = self.load_file('json/level.json')
    user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0, "last_message": None})
    level : int = user_data["level"]
    if amount > user_data["experience"]:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = f"` amount ` cannot be more than ` {user_data["experience"]:,} `",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      return
    user_data["experience"] -= amount
    file.update(user_data)
    self.save_file('json/level.json', file)
    new_level : int | None = self.level(user.id)
    embeds = [
      discord.Embed(
        description = f"Successfully deducted ` {amount:,} ` Experiences from {member.mention}",
        color = 0x39ff14
      ).set_author(
        name = interaction.client.user.name,
        icon_url = interaction.client.user.display_avatar
      )
    ]
    if new_level and new_level > level:
      embeds.append(
        discord.Embed(
          description = f"Congratulations, {member.mention} ! You levelled up to ` Level {new_level:,} ` !",
          color = 0x2b2d31
        ).set_thumbnail(
          url = member.display_avatar
        )
      )
    if new_level and new_level < level:
      embeds.append(
        discord.Embed(
          description = f"Unfortunately, {member.mention} levelled down to ` Level {new_level:,} `",
          color = 0x2b2d31
        ).set_thumbnail(
          url = member.display_avatar
        )
      )
    await interaction.response.send_message(
      member.mention if new_level else "",
      embeds = embeds
    )

  @level.command(
    name = "leaderboard",
    description = "Current levelling leaderboard"
  )
  @app_commands.describe(
    member = "Get the leaderboard rank of a member"
    scope = "Scope of the leaderboard"
  )
  async def level_leaderboard(
    self,
    interaction : discord.Interaction,
    member : discord.Member = None,
    scope : Literal["global", "guild"] = "global"
  ) -> None:
    user : discord.Member = member or interaction.user
    guild : discord.Guild = interaction.guild
    file : TextIO = self.load_file('json/level.json')
    leaderboard : list[str] = sorted(file.keys, key = lambda x : file[x]["experience"], reverse = True)
    if scope == "guild":
      leaderboard : list[str] = [
        user_id for user_id in leaderboard if guild.get_member(int(user_id))
      ]
      if not leaderboard:
        await interaction.response.send_message(
          embed = discord.Embed(
            description = f"No one is placed in ` {guild.name} `'s levelling leaderboard currently",
            color = 0xff3131
          ).set_author(
            name = interaction.client.user.name,
            icon_url = interaction.client.user.display_avatar
          ),
          ephemeral = True
        )
        return

  @level_add_experience.error
  @level_info.error
  @level_leaderboard.error
  @level_remove_experience.error
  async def error(self, interaction : discord.Interaction, error : Exception) -> None:
    if isinstance(error, app_commands.MissingRole):
      await interaction.response.send_message(
        embed = discord.Embed(
          description = f"You do not have permission to execute this command",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ).add_field(
          name = "Reason :",
          value = f"> Missing Role : ` {error.missing_role} `",
          inline = True
        ),
        ephemeral = True
      )
      return
    traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(LevelCog(bot))