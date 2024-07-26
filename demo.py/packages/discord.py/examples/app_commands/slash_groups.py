from discord import (
  app_commands,
  Client,
  Interaction
)
from discord.app_commands import Group
from discord.ext.commands import (
  Bot,
  Cog
)

class SampleCog(Cog):
  def __init__(
    self,
    bot : Bot | Client
  ) -> None:
    bot : Bot | Client = bot

  group : Group = Group(
    name = "group",
    description = "App command group"
  )

  @group.command(
    name = "command",
    description = "/group command"
  )
  async def group_command(
    self,
    interaction : Interaction
  ) -> None:
    await interaction.response.send_message(
      "Pong !"
    )

  @group_command.error
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