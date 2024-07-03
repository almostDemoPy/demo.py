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

  def level_up(self, file : TextIO, user_id : int) -> bool:
    user_data : dict[str, int] = file.get(str(user_id), {"level": 1, "experience": 0})
    level : int = user_data["level"]
    experience : int = user_data["experience"]
    if int(experience ** (1 / self.multiplier)) > level:
      user_data["level"] : int = int(experience ** (1 / self.multiplier))
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

  @level_info.error
  async def error(self, interaction : discord.Interaction, error : Exception) -> None:
    traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(LevelCog(bot))