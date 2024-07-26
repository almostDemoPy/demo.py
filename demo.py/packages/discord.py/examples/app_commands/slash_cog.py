from discord import (
  app_commands,
  Client,
  Interaction
)
from discord.ext.commands import (
  Cog,
  Bot
)

class SampleCog(Cog):
  def __init__(
    self,
    bot : Bot | Client
  ) -> None:
    self.bot : Bot | Client = bot

  @app_commands.command(
    name = "slash",
    description = "Sample slash commands in cog"
  )
  async def slash(
    self,
    interaction : Interaction
  ) -> None:
    await interaction.response.send_message(
      "Pong !"
    )

  @slash.error
  async def error(
    self,
    interaction : Interaction,
    error : Exception
  ) -> None:
    print(error)

async def setup(
  bot : Bot | Client
) -> None:
  await bot.add_cog(SampleCog(bot))