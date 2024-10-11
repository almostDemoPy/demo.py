# UI Kit
Components can be added and accessed in ` Message ` objects. UI Components can be of these types: buttons, modals, and select menus ( or dropdowns ).


## Views
Views contain the components of a message. These may contain buttons and / or select menus. Each view have 5-by-5 grid of component slots, summing up to 25 slots. Buttons occupy 1 component slot, while select menus take up the entire row ( or 5 component slots ).

Views are constructed by initiating or subclassing with <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View'>` View `</a> class. These views can then be passed to a ` view ` parameter of a messageable or interaction response.

**Example**
```py
class Sample(View):
  def __init__(self) -> None: super().__init__()

  ...

@tree.command()
async def sample(interaction : Interaction) -> None:
  await interaction.response.send_message(view = Sample())
```


### Append Components
To add a button or select menu to a ` View ` object, <a href = 'https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.add_view' text-decoration = none>` await Bot.add_view() `</a> is used. Components passed in this method should be instances and not the classes itself.

**Example**
```py
button : Button = Button(...)
view.add_item(button)
```


### Persistent Views
By default, views have a timeout of ` 180 ` seconds. This timeout resets when a component interaction has been created. Persistent views do not die, even after the bot's process has been restarted. To construct one, the ` timeout ` parameter of a ` View ` class should be ` None `. Components of the view should contain unique ` custom_id `s as well. The view should be then added to the bot via <a href = 'https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.add_view'>` await Bot.add_view() `</a> method.

**Example**
```py
class Sample(View):
  def __init__(self) -> None:
    super().__init__(timeout = None)

  @button(
    label = "Sample Button",
    custom_id = "sample_button"
  )
  async def sample_button(self, interaction : Interaction, button : Button) -> None:
    ...

bot.add_view(Sample())
```


## Buttons
Buttons can be constructed with <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.button'>` @ui.button() `</a> decorator or <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button'>` Button `</a> class.


### Creating with the Decorator
The button should be constructed inside a <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View'>` View `</a> subclass.

The callback of the button should contain three arguments: the view object the button is contained in, the interaction object, and the button object itself.

**Example**
```py
class Sample(View):
  def __init__(self) -> None: super().__init__()

  @button(
    label = "Sample Button"
  )
  async def sample_button(self, interaction : Interaction, button : Button) -> None:
    await interaction.response.send_message("Button clicked!")
```


### Creating with the Class
The button can be subclassed outside the ` View ` (sub)class or initiated inside the view's ` __init__ ` dunder method.

When subclassing, the ` callback ` takes up 2 arguments: ` self ` - the button itself, and ` interaction ` - the interaction object. When subclassing or initating with the class, an instance should be passed in <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View.add_item'>` View.add_item() `</a> to append it to the view.

**Example**
```py
# subclassing

class SampleButton(Button):
  def __init__(self) -> None:
    super().__init__(label = "Sample Button")

  async def callback(self, interaction : Interaction) -> None:
    ...

view : View = View()
view.add_item(SampleButton())


# class initiating

class SampleView(View):
  def __init__(self) -> None:
    self.sample_button : Button = Button(label = "Sample Button")
    self.sample_button.callback : Callable[[Self, Interaction, Button], None] = self.button_callback
    self.add_item(self.sample_button)
    super().__init__()

  async def button_callback(self, interaction : Interaction, button : Button) -> None:
    ...
```


### URL Buttons
URL Buttons can only be created through the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button'>` Button `</a> class, and only <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button.label'>` label `</a> and <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button.url'>` url `</a> attributes can be passed.

**Example**
```py
url_button : Button = Button(label = "sample button", url = "https://example.com")
view.add_item(url_button)
```


## Modals
Modals are pop-up menus in the UI. They are only sent as a response to an interaction, via <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse.send_modal'>` await InteractionResponse.send_modal() `</a>.

Modals are constructed via <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Modal'>` Modal `</a> subclass, which takes 1 required keyword argument ( of the 3 parameters ): ` title ` - title of the modal.
**Example**
```py
class SampleModal(Modal):
  def __init__(self) -> None: super().__init__(title = "Sample Modal")
```

### Text Inputs
Text inputs holds the field placeholders in a modal. You can only append up to 5 text inputs in one modal. Text inputs are constructed inside a ` Modal ` subclass, with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.TextInput'>` TextInput `</a> class.

Callbacks for the modal is defined in ` on_submit ` function of the class. The callback takes 2 arguments: ` self ` - the modal itself, ` interaction ` - the interaction object. When the modal is submitted, text input can be accessed as attributes of the modal class. As such, using the ` str() ` conversion method, or its <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.TextInput.value'>` value `</a> attribute, will return the user input for that specific field / text input. All text input values are always treated as ` str `s.

**Example**
```py
class SampleModal(Modal):
  def __init__(self) -> None:
    super().__init__(timeout = None)

  field : TextInput = TextInput(
    label = "Sample Field",
    style = TextStyle.short
  )

  async def on_submit(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"You wrote: {self.field.value}")

@tree.command()
async def sample(interaction : Interaction) -> None:
  await interaction.response.send_modal(SampleModal())
```

## Select Menus
Select menus are dropdowns in the UI. They are similar to choices-type slash options.


### Selects
To construct a select menu, one can subclass the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Select'>` Select `</a> class.

The ` options ` parameter should be a list of <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.SelectOption'>` SelectOption `</a>, and will not exceed 25 options. Callbacks for select menus are defined in ` callback ` function of the class / object. To retrieve a list of values the user selected, <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Select.values'>` values `</a> attribute is accessed.

**Example**
```py
class SampleSelect(Select):
  def __init__(self) -> None:
    super().__init__(
      options = [
        SelectOption(label = "A"),
        SelectOption(label = "B"),
        SelectOption(label = "C")
      ]
    )

  async def callback(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"You selected: {self.values[0]}")
```

Select menus can also be created with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.select'>` @select() `</a> decorator. The decorator's ` cls ` parameter defaults to ` Select `, this can be modified to alter to a predefined select menu.

The function attached by the decorator should have three parameters: ` self ` - the view itself, ` interaction ` - the interaction object, and ` select ` - the select menu object.

**Example**
```py
class SampleView(View):
  @select(
    cls = ChannelSelect,
    channel_types = [ChannelType.text]
  )
  async def sample(self, interaction : Interaction, select : ChannelSelect) -> None:
    await interaction.response.send_message(f"Teleporting to: {select.values[0].mention}")
```


### Channel Selects
Channel selects are predefined selects whose options are list of channels. <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.ChannelSelect.channel_types'>` channel_types `</a> attribute / parameter can be modified to show options of a specific type of channel only ( defaults to all channels ). Channel selects are constructed with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.ChannelSelect'>` ChannelSelect `</a> class.

**Example**
```py
class SampleSelect(ChannelSelect):
  def __init__(self) -> None:
    super().__init__(
      channel_types = [ChannelType.text]
    )

  async def callback(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"You chose the channel: {self.values[0].mention}")
```


### Role Selects
Role selects are predefined select menus whose options are a list of guild roles. Role selects are constructed with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.RoleSelect'>` RoleSelect `</a> class.

**Example**
```py
class SampleSelect(RoleSelect):
  def __init__(self) -> None:
    super().__init__()

  async def callback(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"Pinging the role: {self.values[0].mention}")
```


### Mentionable Selects
Mentionable selects are predefined select menus whose options are a list of guild members and roles. Mentionable selects are constructed with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.MentionableSelect'>` MentionableSelect `</a> class.

**Example**
```py
class SampleSelect(MentionableSelect):
  def __init__(self) -> None:
    super().__init__()

  async def callback(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"Pinging member / user: {self.values[0].mention}")
```


### User Selects
User selects are predefined select menus whose options are a list of guild members. User selects are constructed with the <a href = 'https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.UserSelect'>` UserSelect `</a> class.

**Example**
```py
class SampleSelect(UserSelect):
  def __init__(self) -> None:
    super().__init__()

  async def callback(self, interaction : Interaction) -> None:
    await interaction.response.send_message(f"Pinging member: {self.values[0].mention}")
```