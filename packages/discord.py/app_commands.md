# Application Commands
Application commands are categorized into two: slash commands, and context menu commands. These are introduced when typing a ` / ` forward slash in the chatbox, or right-clicking on a message or user.


## Slash Commands

Slash commands can be constructed with the <a href = "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree.command">` @CommandTree.command() `</a> decorator, or <a href = "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.command">` @app_commands.command() `</a> decorator when performed inside <a href = "https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html">Cogs</a>.

When constructing a slash command, the function will always take up first argument as the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction'>` Interaction `</a> object.

**Example**
```py
@bot.tree.command()
async def sample(interaction : Interaction) -> None: ...
```


### Slash Options
Options in a slash command corresponds to an argument in a function. Therefore, to append a slash option, you can just append another argument to your command callback.


#### Option Types


The enlisted below are the accepted option types, by which ` str ` is the defaut. To specify the option type, simply annotate the argument with it:
- ` str `
- ` int `
- ` bool `
- ` float `
- <a href = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.User'>` User `</a> or <a href = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.Member'>` Member `</a>
- <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandChannel'>` AppCommandChannel `</a> or <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandThread'>` AppCommandThread `</a>
- <a href = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.Role'>` Role `</a>
- <a href = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment'>` Attachment `</a>

**Example**
```py
@tree.command()
async def sample(interaction : Interaction, name : str) -> None:
  await interaction.response.send_message(f"Hello, {name}!")
```

> **See also**
> <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Namespace'>` Namespace `</a>


#### Option Descriptions
To append descriptions to your options, append the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.describe'>` @app_commands.describe() `</a> decorator to your function. The decorator takes in keyword arguments, of which are in pairs as: the name of the option / argument to describe, and its description.

**Example**
```py
@tree.command()
@app_commands.describe(
  name = "Name of the user"
)
async def sample(interaction : Interaction, name : str) -> None:
  await interaction.response.send_message(f"Hello, {name}!")
```


### Choices
Slash Choices lets the user pick from a fixed list of values. <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.choices'>` @app_commands.choices() `</a> decorator is used to construct a choice option. The decorator takes up keyword arguments, going in pairs by: the name of the option / argument to construct a slash choice on, and its list of values as <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#choice'>` Choice `</a> objects.

**Example**
```py
@tree.command()
@describe(choice = "Your playing card")
@choices(
  choice = [
    Choice(name = "Rock", value = "rock"),
    Choice(name = "Paper", value = "paper"),
    Choice(name = "Scissors", value = "scissors")
  ]
)
async def sample(interaction : Interaction, choice : str) -> None:
  await interaction.response.send_message(f"You chose {choice}")
```

> **NOTE**
> 1. Choices can only have up to 25 values. Otherwise, you can use <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.autocomplete'>` @autocomplete() `</a> decorator instead.
> 2. The type of the ` value ` of the ` Choice ` objects must match the annotation specified to the argument / option.


### Autocompletes
Unlike slash choices, autocomplete maintains the display of a list of valid values, while allowing the user to input anything else other than the valid values. <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.autocomplete'>` @app_commands.autocomplete() `</a> decorator is used to construct an autocomplete option. The decorator takes up keyword arguments, by which in pairs as: the argument / option to construct as an autocomplete, and the callback / function to handle the corresponding argument / option.

Similar to slash choices, autocomplete callbacks return a list of <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Choice'>` Choice `</a> objects.

**Example**
```py
async def language_autocomplete(interaction : Interaction, current : str) -> List[str]:
  languages : List[str] = ["Python", "Javascript", "C", "Rust"]
  return [
    Choice(name = language, value = language)
    for language in languages
    if current.lower() in language.lower()
  ]
```

**Explanation**
The autocomplete callback requires 2 arguments: ` interaction ` - the interaction object, ` current ` - the text the user has currently typed in. The function returns a list of programming languages whose name contains a substring of what the user has currently typed.

> **NOTE**
> Autocompletes do not limit the user from typing anything else, thus you must handle properly if the user picked a value that is outside of the encoded valid values.


### Error Handling
The <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command.error'>` @error `</a> of a command function / callback can be attache to another function for the command's error handling. The error handler function takes up 2 required arguments: ` interaction ` - the interaction object, and ` error ` - the exception that was caught.

**Example**
```py
@tree.command()
async def sample(interaction : Interaction) -> None: ...

@sample.error
async def error(interaction : Interaction, error : Exception) -> None:
  print(error)
```


### Slash Commands in Cogs
To construct a slash command in a ` Cog ` subclass, <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.command'>` @app_commands.command() `</a> is used. ` @CommandTree.command() ` won't work in this case.

**Example**
```py
class Sample(Cog):
  @app_commands.command()
  async def sample(self, interaction : Interaction) -> None:
    ...
```


## Context Menus
Context Menus are those commands where you right-click on a message or user and are found under ` Apps ` section. Unlike slash commands, context menus only take up 2 required arguments: ` interaction ` - the interaction object, and ` user ` or ` message ` - the user or message object the command was ran on, depending on the type it is registered as.

<a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree.context_menu'>` @context_menu() `</a> decorator is used to construct a context menu command.


### User Context Menu Commands
To construct a user-type context menu command, the second argument should be a ` Member ` or ` User ` annotated.

**Example**
```py
@tree.context_menu()
async def sample(interaction : Interaction, member : Member) -> None:
  await interaction.response.send_message(f"Pinged {member.mention}")
```

### Message Context Menu Commands
To construct a message-type context menu command, the second argument should be ` Message ` annotated.

**Example**
```py
@tree.context_menu()
async def sample(interaction : Interaction, message : Message) -> None:
  await interaction.response.send_message(f"{message.author.name} sent this message")
```


### Context Menus in Cogs
To create a context menu command inside a ` Cog ` subclass, <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.ContextMenu'>` ContextMenu `</a> class is initiated inside the cog's ` __init__ ` dunder method or separate function.

**Example**
```py
class Sample(Cog):
  def __init__(self) -> None:
    self.ctx_menu : ContextMenu = ContextMenu(
      name = "hello world",
      callback = self.ctx_menu_callback
    )

  async def ctx_menu_callback(self, interaction : Interaction, message : Message) -> None:
    ...
```


## Responding to an Interaction
Interactions must be responded and cannot be ignored. This can be done using the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse'>` InteractionResponse `</a> instance of an <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction'>` Interaction `</a> object, obtained via the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.response'>` response `</a> attribute.

There are a few choices of responding to the interaction: deferring the interaction, editing the original response of a component or modal interaction, sending a modal, or sending like an ordinary message. All interactions must be responding within 3 seconds, or 15 minutes if deferred, otherwise the interaction will become invalid.

### Deferring
Deferring an interaction lets the bot wait for 15 minutes rather than 3 seconds for an interaction response. This allows some long-processing code to flow through without the interaction becoming invalid.

The <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse.defer'>` await InteractionResponse.defer() `</a> method, the method used to defer the interaction, accepts 2 keyword arguments:
- **ephemeral** : ` bool ` = whether to respond publicly or only to the user who executed the interaction. Defaults to ` False `
- **thinking** : ` bool ` = in UI terms, this is represented as if the bot is thinking of a response. To remove the thinking state, you must send a followup message using <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.followup'>` await Interaction.followup.send() `</a>

**Example**
```py
@tree.command()
async def sample(interaction : Interaction) -> None:
  await interaction.response.defer()
  await interaction.followup.send(...)
```

> **NOTE**
> You cannot respond with another ` InteractionResponse ` method again after you defer since you can only respond once to an interaction. If you wish to update the deferring response, use <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.followup'>` await Interaction.followup.send() `</a> instead


### Editing the Original Response
To edit the original response of a component or modal interaction, use <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse.edit_message'>` await InteractionResponse.edit_message() `</a>. The parameters of the method are of similar to a ` send() ` method.

**Example**
```py
class Sample(Button):
  def callback(self, interaction : Interaction) -> None:
    await interaction.response.edit_message("edited message")
```


### Standard Response
Standard way to respond to an interaction is similar to any other ` send() ` method, with the use of <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse.send_message'>` await InteractionResponse.send_message() `</a>

**Example**
```py
@tree.command()
async def sample(interaction : Interaction) -> None:
  await interaction.response.send_message("hello world")
```


## Registering Application Commands
Registering your command tree updates the application commands to the API. Doing so will reflect the changes you made to your application commands' code into the Discord app client ( Note: changes to command callback does not need registering ).

To register your application commands, <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree.sync'>` await CommandTree.sync() `</a> is called. **It is highly advisable that you don't register your application commands automatically by doing it in an event, loop, or any automated mechanism. This may cause your application to get rate limited. Instead, you may do it in a command**.

The method takes up 1 optional keyword argument:
- **guild** : Optional[<a href = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake'>` Snowflake `</a>] = the guild to sync the commands to. If this is ` None `, it instead registers the global application commands. Defaults to ` None `

**Example**
```py
@bot.command()
@commands.is_owner()
async def sync(ctx : Context) -> None:
  await ctx.bot.tree.sync()
  await ctx.reply("Application commands have been successfully registered")
```

> **NOTE**
> If the applications still have not showed up, try restarting your Discord, or check and properly construct and register your application commands.


## User-Installed Application Commands
User-installed application commands allow the user to install it to their account, which by then they can execute anywhere where they are without needing to invite the bot in a guild or DM, as long as it's registered to be available in that context.

A user-install application command can be constructed with either <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.allowed_installs'>` @allowed_installs() `</a> or <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.user_install'>` @user_install() `</a> decorator. With the ` @allowed_installs() ` decorator, ` users ` parameter should be passed as ` True `.

To specify what contexts the application command is available to be executed, <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.allowed_contexts'>` @allowed_contexts() `</a> decorator is used. The decorator takes 3 keyword arguments:
- **guilds** : ` bool ` = whether the command can be executed in a guild without the bot having to be in it
- **dms** : ` bool ` = whether the command can be executed in the bot's DM
- **private_channels** : ` bool ` = whether the command can be executed in a group DM or DM other than the bot's

**Example**
```py
@tree.command()
@allowed_installs(guilds = True, users = True)
@allowed_contexts(guilds = True, dms = True, private_channels = True)
async def sample(interaction : Interaction) -> None:
  await interaction.response.send_message("I'm ran in a DM channel!")
```