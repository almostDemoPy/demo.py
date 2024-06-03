import asyncio
import discord
import traceback
from datetime import datetime, timedelta
from discord import app_commands
from discord.ext import commands

class SelfDestruct(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(
    name = "self_destruct",
    description = "Self-desctruct !!"
  )
  async def self_destruct(self, interaction : discord.Interaction) -> None:
    current_timestamp : int = int((datetime.now() + timedelta(seconds = 10)).timestamp())
    await interaction.response.send_message(
      embed = discord.Embed(
        description = f"Self-destructing <t:{current_timestamp}:R>",
        color = 0xff3131
      )
    )
    await asyncio.sleep(10)
    await interaction.edit_original_response(
      embed = discord.Embed(
        description = "Touch grass",
        color = 0xff3131
      )
    )

  @self_destruct.error
  async def error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

async def setup(bot) -> None:
  await bot.add_cog(SelfDestruct(bot))