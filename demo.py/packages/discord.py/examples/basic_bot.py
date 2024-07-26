from discord import Intents
from discord.ext.commands import Bot

bot : Bot = Bot(
  intents = Intents.default(),
  command_prefix = "!"
)

@bot.listen()
async def on_ready() -> None:
  print(f"{bot.user.name} is online")

if __name__ == "__main__":
  token : str = "BOT_TOKEN"
  bot.run(token)