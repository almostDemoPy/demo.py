from discord import (
  Intents,
  Member
)
from discord.ext.commands import Bot, Context

bot_intents : Intents = Intents.default()
bot_intents.message_content = True

bot : Bot = Bot(
  command_prefix = "!",
  intents = bot_intents
)

@bot.command(
  name = "sample",
  description = "A sample of a prefix command"
)
async def sample(
  ctx : Context
) -> None:
  author : Member = ctx.author
  await ctx.send(
    f"Hello, {author} !"
  )

@sample.error
async def sample_error(
  context : Context,
  error : Exception
) -> None:
  print(error)