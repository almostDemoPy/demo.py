from discord import (
  app_commands,
  Interaction,
  Intents,
  Client
)
from app_commands import CommandTree

bot_intents : Intents = Intents.default()


# commands.Bot

bot : Bot = Bot(
  command_prefix = "!",
  intents = bot_intents
)

@bot.tree.command(
  name = "slash",
  description = "Sample bot slash command"
)
async def slash_bot(
  interaction : Interaction
) -> None:
  await interaction.response.send_message(
    "Hello !"
  )

@slash_bot.error
async def error(
  interaction : Interaction,
  error : Exception
) -> None:
  print(error)


# discord.Client

client : Client = Client(
  intents = bot_intents
)
tree : CommandTree = CommandTree(client)

@tree.command(
  name = "slash",
  description = "Sample client slash command"
)
async def slash_client(
  interaction : Interaction
) -> None:
  await interaction.response.send_message(
    "Pong !"
  )

@slash_client.error
async def error(
  interaction : Interaction,
  error : Exception
) -> None:
  print(error)