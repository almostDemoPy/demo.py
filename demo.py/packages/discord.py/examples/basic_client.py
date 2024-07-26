from discord import (
  Client,
  Intents
)

client : Client = Client(
  intents = Intents.default()
)

@client.listen()
async def on_ready() -> None:
  print(f"{client.user.name} is online")

if __name__ == "__main__":
  token : str = "BOT_TOKEN"
  client.run(token)