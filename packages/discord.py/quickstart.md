# Quickstart


## Pip Installation
To install ` discord.py `, open a terminal with these steps:
1. ` Win + R ` or ` Win + S `
2. Type ` cmd `
3. Press ` Enter `

Enter the following command below in your terminal:
```bash
$ pip install discord.py
```


## Minimal Setup
```py
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_message(message : discord.Message) -> None:
  if message.content.lower() == "hi":
    await message.send("hello !")

client.run("TOKEN")
```

**Walkthrough**
1. ` import discord ` imports the library to your file.
2. ` Intents.default() ` enables every intent except the privileged gateway intents, and stores it in the ` intents ` variable. The ` message_content ` intent is enabled so the bot can read the contents of a message. This intent should also be enabled in your Developer Portal.
3. A ` discord.Client ` is initiated and the ` intents ` variable is passed. ` client ` will be the object variable of our bot.
4. ` @client.event ` lets the bot to listen for ` on_message ` events - an event that is triggered when a message is sent or created.
  4.1 When this event listener is triggered, ` message.content.lower() ` converts the message content into lowercase, and checks if it equals to ` "hi" `.
  4.2 If it does, the bot will send a ` "hello !" ` message in the chat, called by the ` await message.send() ` method.
5. Lastly, the client is ran via ` client.run() ` which takes a parameter of the bot's token stored in ` str `. Any lines of code called past this method will not be executed as the method is blocking.

> **NOTE**
> 
> ` @Client.event ` or ` @Bot.event ` is blocking for prefix commands. To avoid this, append a [` await Bot.process_commands() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.process_commands) method call at the end of the event listener, or use the [` @Bot.listen() `](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.listen) decorator.
> ```py
> @bot.event
> async def on_message(message : Message) -> None:
>   ...
>   await bot.process_commands(message)
> 
> # or
> 
> @bot.listen()
> async def on_message(message : Message) -> None:
>   ...
> ```