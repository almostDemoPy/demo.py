# Prefix Commands
Unlike slash commands and context menu commands, prefix commands aren't application commands. Merely, they are a mechanism of listening for ` on_message ` events, parsing and processing the message content. Prefix commands were considered the legacy commands.

To construct a prefix command, [` @Bot.command() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.command) decorator is used. The function the decorator is attached to should contain 1 required argument: ` ctx ` - the [` Context `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context) object.

**Example**
```py
@bot.command()
async def sample(ctx : Context) -> None:
  await ctx.send("hello world")
```

Prefix commands are triggered by the bot's set [` command_prefix `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.command_prefix). This attribute is required and can be set when initiating your ` Bot ` class.

```py
bot : Bot = Bot(command_prefix = "!", ...)
```

Now your commands will be executed with the ` ! ` prefix, i.e ` !ping `. For your prefix commands to trigger, your bot would also need the ` message_content ` intent. This intent should be enabled in your ` Intents ` instance.

```py
intents : Intents = Intents.default()
intents.message_content : bool = True
bot : Bot = Bot(command_prefix = "!", intents = intents)
```


## Prefix Commands in Cogs
[` @commands.command() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.command) is used when constructing a prefix command inside a Cog.

**Example**
```py
class Sample(Cog):
  @commands.command()
  async def sample(self, ctx : Context) -> None:
    await ctx.send("hello world")
```


## Responding to the Prefix Command
A prefix command can be responded with [` await Context.send() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context.send) or [` await Context.reply() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context.reply). Unlike application commands, whom you have to respond within 3 seconds or 15 minutes, you can completely ignore responding to the prefix command as well. By default, the command name will copy the name of the function the decorator is attached to, unless further modified in the decorator itself.

**Example**
```py
@bot.command()
async def sample(ctx : Context) -> None:
  await ctx.reply("hello world")
```


## Command Arguments
Similar to application commands, arguments for the prefix commands are the arguments in its function callback. The value received defaults to ` str `, unless annotated with a class or converter.

**Example**
```py
@bot.command()
async def sample(ctx : Context, member : Member) -> None:
  await ctx.send(f"Hello, {member.mention}!")
```

> **See also**
> 
> - [Converters](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#converters)


## Error Handling
[` @error `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Command.error) decorator of a command function can be attached to another function for the command's error handling. The error handler function should contain 2 required arguments: ` ctx ` - the ` Context ` object, and ` error ` - the exception catched

**Example**
```py
@bot.command()
async def sample(ctx : Context) -> None:
  print(1 + "2")

@sample.error
async def error(ctx : Context, error : Exception) -> None:
  print(error)
```