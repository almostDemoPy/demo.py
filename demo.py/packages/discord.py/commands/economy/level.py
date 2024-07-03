import discord
import json
import traceback
from discord import app_commands, ui
from discord.ext import commands
from typing import TextIO

class LevelCog(commands.Cog):
  def __init__(self, bot : commands.Bot) -> None:
    self.bot : commands.Bot = bot
    self.experience_gain_amount : int = 5
    self.multiplier : int = 4

  level : app_commands.Group = app_commands.Group(
    name = "level",
    description = "/level"
  )

  def get_max_exp(self, file : TextIO, user_id : int) -> int:
    level : int = file.get(str(user_id), {"level": 1, "experience": 0})["level"]
    max_experience : int = int((level + 1) ** self.multiplier)
    return max_experience

  def level_up(self, user_id : int) -> int | None:
    file : TextIO = self.load_file('json/level.json')
    user_data : dict[str, int] = file.get(str(user_id), {"level": 1, "experience": 0})
    level : int = user_data["level"]
    experience : int = user_data["experience"]
    if int(experience ** (1 / self.multiplier)) > level:
      new_level : int = int(experience ** (1 / self.multiplier))
      user_data["level"] : int = new_level
      file[str(user_id)].update(user_data)
      self.save_file('json/level.json', file)
      return True
    return False

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
    user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0})
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
    amount : app_commands.Range[int, 1, 10_000]
  ) -> None:
    user : discord.Member = member or interaction.user
    file : TextIO = self.load_file('json/level.json')
    user_data : dict[str, int] = file.get(str(user.id), {"level": 1, "experience": 0})
    user_data["experience"] += amount
    file.update(user_data)
    self.save_file('json/level.json', file)
    new_level : bool = self.level_up(user.id)
    embeds = [
      discord.Embed(
        description = f"Successfully gave {member.mention} ` {amount:,} ` Experiences.",
        color = 0x39ff14
      ).set_author(
        name = interaction.client.user.name,
        icon_url = interaction.client.user.display_avatar
      )
    ]
    if new_level:
      embeds.append(
        discord.Embed(
          description = f"Congratulations, {member.mention} ! You levelled up to ` Level {new_level:,} ` !",
          color = 0x2b2d31
        ).set_thumbnail(
          url = member.display_avatar
        )
      )
    await interaction.response.send_message(
      member.mention if new_level else "",
      embeds = embeds
    )

  @level_info.error
  @level_add_experience.error
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