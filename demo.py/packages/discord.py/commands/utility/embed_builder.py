import discord
import traceback
from datetime import datetime
from discord import app_commands, ui
from discord.ext import commands

class PropertyEditModal(ui.Modal):
  def __init__(self, index : int, embeds : list[discord.Embed], embed_property : str, view : ui.View) -> None:
    self.index : int = index
    self.embeds : list[discord.Embed] = embeds
    self.embed_property : str = embed_property
    self.view : ui.View = view
    self.properties : dict = {
      "Title": self.embeds[self.index].title if self.embeds[self.index].title else "",
      "Description": self.embeds[self.index].description if self.embeds[self.index].description else "",
      "Footer_Text": self.embeds[self.index].footer.text if self.embeds[self.index].footer.text else "",
      "Footer_Icon_URL": self.embeds[self.index].footer.icon_url if self.embeds[self.index].footer.icon_url else "",
      "Image": self.embeds[self.index].image.url if self.embeds[self.index].image else "",
      "Thumbnail": self.embeds[self.index].thumbnail.url if self.embeds[self.index].thumbnail else "",
      "Timestamp": str(int(self.embeds[self.index].timestamp.timestamp())) if self.embeds[self.index].timestamp else "",
      "URL": self.embeds[self.index].url if self.embeds[self.index].url else ""
    }
    self.max_lengths : dict = {
      "Title": 256,
      "Description": 4_000,
      "Footer_Text": 2_048,
      "Footer_Icon_URL": None,
      "Image": 4_000,
      "Thumbnail": 4_000,
      "Timestamp": 4_000,
      "URL": 4_000
    }
    self.styles : dict = {
      "Title": False,
      "Description": True,
      "Footer_Text": False,
      "Footer_Icon_URL": False,
      "Image": False,
      "Thumbnail": False,
      "Timestamp": False,
      "URL": False
    }
    super().__init__(
      timeout = None,
      title = "Embed Edit"
    )
    self.prompt : ui.TextInput = ui.TextInput(
      custom_id = "embed_property_edit_modal",
      default = self.properties[self.embed_property],
      label = self.embed_property,
      max_length = self.max_lengths[self.embed_property] if self.max_lengths[self.embed_property] else 4_000,
      min_length = 0,
      placeholder = "Leave empty to remove",
      style = discord.TextStyle.long if self.styles[self.embed_property] else discord.TextStyle.short,
      required = False
    )
    self.add_item(self.prompt)

  async def on_submit(self, interaction : discord.Interaction) -> None:
    new_value : str = str(self.prompt)
    match self.embed_property:
      case "Title": self.embeds[self.index].title = new_value
      case "Description": self.embeds[self.index].description = new_value
      case "Footer_Text": self.embeds[self.index].set_footer(text = new_value, icon_url = self.embeds[self.index].footer.icon_url)
      case "Footer_Icon_URL":
        if not new_value: new_value = None
        if new_value:
          if new_value.lower() == "{{self.avatar}}": new_value = interaction.user.display_avatar
        try:
          self.embeds[self.index].set_footer(text = self.embeds[self.index].footer.text, icon_url = new_value)
          await interaction.response.edit_message(
            content = None,
            embeds = self.embeds
          )
        except:
          self.embeds[self.index].set_footer(text = self.embeds[self.index].footer.text, icon_url = None)
          await interaction.response.edit_message(
            content = "Invalid ` Footer_Icon_URL `",
            embeds = self.embeds
          )
        return
      case "Image":
        if not new_value: new_value = None
        if new_value:
          if new_value.lower() == "{{self.banner}}":
            user = await interaction.client.fetch_user(interaction.user.id)
            if not user.banner:
              await interaction.response.edit_message(
                content = "You have no banner",
                embeds = self.embeds
              )
              return
            new_value = user.banner.url
        try:
          self.embeds[self.index].set_image(new_value)
          await interaction.response.edit_message(
            content = None,
            embeds = self.embeds
          )
        except:
          self.embeds[self.index].set_image(None)
          await interaction.response.edit_message(
            content = "Invalid ` Image URL `",
            embeds = self.embeds
          )
        return
      case "Thumbnail":
        if not new_value: new_value = None
        if new_value:
          if new_value.lower() == "{{self.avatar}}": new_value = interaction.user.display_avatar
        try:
          self.embeds[self.index].set_thumbnail(url = new_value)
          await interaction.response.edit_message(
            content = None,
            embeds = self.embeds
          )
        except:
          self.embeds[self.index].set_thumbnail(url = None)
          await interaction.response.edit_message(
            content = "Invalid ` Image URL `",
            embeds = self.embeds
          )
        return
      case "Timestamp":
        if not new_value: new_value = None
        if new_value:
          if new_value.lower() == "{{datetime.now()}}": new_value = datetime.now()
          else:
            new_value = datetime.fromtimestamp(int(new_value))
        try:
          self.embeds[self.index].timestamp = new_value
          await interaction.response.edit_message(
            content = None,
            embeds = self.embeds
          )
        except:
          self.embed.timestamp = None
          await interaction.response.edit_message(
            content = "Invalid ` timestamp `",
            embed = self.embed
          )
        return
      case "URL":
        if not new_value: new_value = None
        try:
          self.embed.url = new_value
          await interaction.response.edit_message(
            content = None,
            embeds = self.embeds
          )
        except:
          self.embeds[self.index].url = None
          await interaction.response.edit_message(
            content = "Invalid ` URL `",
            embeds = self.embeds
          )
        return
    for child in self.view.children:
      if child.disabled: child.disabled = False
    self.view.children[-1].label = "Send"
    await interaction.response.edit_message(
      content = None,
      embeds = self.embeds,
      view = self.view
    )

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedFieldEdit(ui.Modal):
  def __init__(self, index : int, embeds : list[discord.Embed], field_index : int) -> None:
    self.index : int = index
    self.embeds : list[discord.Embed] = embeds
    self.field_index : int = field_index
    super().__init__(
      timeout = None,
      title = "Embed Field Edit"
    )
    self.field_name : ui.TextInput = ui.TextInput(
      custom_id = "embed_field_edit_name",
      default = self.embeds[self.index].fields[self.field_index].name if abs(self.field_index) < len(self.embeds[self.index].fields) else "",
      label = "Field Name",
      max_length = 256,
      min_length = 1,
      required = True,
      style = discord.TextStyle.short
    )
    self.field_value : ui.TextInput = ui.TextInput(
      custom_id = "embed_field_edit_value",
      default = self.embeds[self.index].fields[self.field_index].value if abs(self.field_index) < len(self.embeds[self.index].fields) else "",
      label = "Field Value",
      max_length = 1_024,
      min_length = 1,
      required = True,
      style = discord.TextStyle.long
    )
    self.at_index : ui.TextInput = ui.TextInput(
      custom_id = "embed_field_edit_index",
      default = str(self.field_index),
      label = "Field Index",
      max_length = 2,
      min_length = 1,
      required = True,
      style = discord.TextStyle.short
    )
    self.add_item(self.field_name)
    self.add_item(self.field_value)
    if not (abs(self.field_index) < len(self.embeds[self.index].fields)):
      self.add_item(self.at_index)

  async def on_submit(self, interaction : discord.Interaction) -> None:
    field_name : str = str(self.field_name.value)
    field_value : str = self.field_value.value
    at_index : str = self.at_index.value
    try:
      at_index : int = abs(int(at_index))
      if at_index > len(self.embeds[self.index].fields):
        await interaction.response.edit_message(
          content = f"` Field Index ` must only be from ` 0 ` to ` {len(self.embeds[self.index].fields)} `",
          embeds = self.embeds
        )
        return
      if at_index > 24:
        await interaction.response.edit_message(
          content = "` Field Index ` must only be from ` 0 ` to ` 24 `",
          embeds = self.embeds
        )
        return
    except:
      traceback.print_exc()
      await interaction.response.edit_message(
        content = "Invalid ` Field Index `",
        embeds = self.embeds
      )
      return
    if at_index < len(self.embeds[self.index].fields):
      self.embeds[self.index].set_field_at(
        at_index,
        name = field_name,
        value = field_value,
        inline = False
      )
    else:
      self.embeds[self.index].insert_field_at(
        at_index,
        name = field_name,
        value = field_value,
        inline = False
      )
    view = ui.View(timeout = None)
    view.index = self.index
    view.add_item(EmbedFieldSelect(self.embeds[self.index].fields))
    view.add_item(EmbedFieldRemove(self.index, self.embeds))
    view.add_item(EmbedAddField())
    await interaction.response.edit_message(
      content = None,
      embeds = self.embeds,
      view = view
    )

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedFieldRemove(ui.Select):
  def __init__(self, index : int, embeds : list[discord.Embed]) -> None:
    self.index : int = index
    self.embeds : list[discord.Embed] = embeds
    if self.embeds[self.index].fields:
      self.select_options = [discord.SelectOption(label = str(field_count + 1)) for field_count in range(len(self.embeds[self.index].fields))]
    else:
      self.select_options = [discord.SelectOption(label = "None")]
    super().__init__(
      custom_id = "embed_field_remove",
      max_values = len(self.embeds[self.index].fields) if self.embeds[self.index].fields else 1,
      min_values = 1,
      placeholder = "Select an embed field to remove",
      disabled = False if self.embeds[self.index].fields else True,
      options = self.select_options,
      row = 1
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      indexes : list[int] = [int(value) - 1 for value in self.values][::-1]
      if len(self.embeds[self.view.index].fields) == len(indexes):
        self.embeds[self.view.index].clear_fields()
        if not self.embeds[self.view.index].fields:
          self.disabled = True
      else:
        for index in indexes:
          self.embeds[self.view.index].remove_field(index)
        self.disabled = False
      view = ui.View(
        timeout = None
      )
      view.index = self.view.index
      view.add_item(EmbedFieldSelect(self.embeds[self.view.index].fields))
      view.add_item(EmbedFieldRemove(self.view.index, self.embeds))
      view.add_item(EmbedAddField())
      await interaction.response.edit_message(
        content = None,
        embeds = self.embeds,
        view = view
      )
    except:
      traceback.print_exc()

class EmbedFieldSelect(ui.Select):
  def __init__(self, fields) -> None:
    self.fields = fields
    if fields:
      self.select_options = [discord.SelectOption(label = str(field_count + 1)) for field_count in range(len(self.fields))]
    else:
      self.select_options = [discord.SelectOption(label = "None")]
    super().__init__(
      custom_id = "embed_field_select",
      max_values = 1,
      min_values = 1,
      placeholder = "Select an embed field to edit",
      disabled = False if fields else True,
      options = self.select_options,
      row = 0
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      value : int = int(self.values[0])
      await interaction.response.send_modal(EmbedFieldEdit(self.view.index, interaction.message.embeds, value - 1))
    except:
      traceback.print_exc()

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedAddField(ui.Button):
  def __init__(self) -> None:
    super().__init__(
      custom_id = "embed_add_field_button",
      disabled = False,
      label = "Add Field",
      style = discord.ButtonStyle.green
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      await interaction.response.send_modal(EmbedFieldEdit(self.view.index, interaction.message.embeds, len(interaction.message.embeds[self.view.index].fields)))
    except:
      traceback.print_exc()

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class BackButton(ui.Button):
  def __init__(self, section : str) -> None:
    self.section : str = section
    super().__init__(
      custom_id = "embed_back_button",
      disabled = False,
      label = "Back",
      style = discord.ButtonStyle.gray
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      view = ui.View(
        timeout = None
      ).add_item(
        EmbedSelect(embeds = interaction.message.embeds)
      ).add_item(
        EmbedPropertySelect(interaction.message.embeds)
      ).add_item(
        EmbedRemove(interaction.message.embeds)
      ).add_item(
        ClearButton(interaction.message.embeds)
      ).add_item(
        AddEmbed(interaction.message.embeds)
      ).add_item(
        SendButton(interaction.message.embeds)
      )
      view.index = self.view.index
      view.children[0].options[view.index].default = True
      await interaction.response.edit_message(
        content = None,
        view = view
      )
    except:
      traceback.print_exc()

class SendButton(ui.Button):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    super().__init__(
      custom_id = "send_button",
      disabled = False if self.embeds else True,
      label = "Send",
      style = discord.ButtonStyle.green
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      await interaction.channel.send(embeds = interaction.message.embeds)
      self.disabled = True,
      self.label = "Sent"
      await interaction.response.edit_message(
        content = None,
        view = self.view
      )
    except:
      traceback.print_exc()

class ClearButton(ui.Button):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    super().__init__(
      custom_id = "clear_button",
      disabled = False if self.embeds else True,
      label = "Clear",
      style = discord.ButtonStyle.red
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      embed : discord.Embed = discord.Embed(
        color = 0x2b2d31
      ).set_author(
        name = interaction.user.name,
        icon_url = interaction.user.display_avatar
      )
      view = ui.View(
        timeout = None
      ).add_item(
        EmbedSelect(embeds = [embed])
      ).add_item(
        EmbedPropertySelect([embed])
      ).add_item(
        EmbedRemove([embed])
      ).add_item(
        ClearButton([embed])
      ).add_item(
        AddEmbed([embed])
      ).add_item(
        SendButton([embed])
      )
      view.index = None
      await interaction.response.edit_message(
        content = None,
        embeds = [embed],
        view = view
      )
    except:
      traceback.print_exc()

class AddEmbed(ui.Button):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    super().__init__(
      custom_id = "add_embed_button",
      disabled = False if len(self.embeds) < 10 else True,
      label = "Add Embed",
      style = discord.ButtonStyle.green
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      embed : discord.Embed = discord.Embed(
        description = "embed template",
        color = 0x2b2d31
      )
      if not self.embeds:
        embed.set_author(
          name = interaction.user.name,
          icon_url = interaction.user.display_avatar
        )
      self.embeds.append(embed)
      view = ui.View(
        timeout = None
      ).add_item(
        EmbedSelect(embeds = self.embeds)
      ).add_item(
        EmbedPropertySelect(self.embeds)
      ).add_item(
        EmbedRemove(self.embeds)
      ).add_item(
        ClearButton(self.embeds)
      ).add_item(
        AddEmbed(self.embeds)
      ).add_item(
        SendButton(self.embeds)
      )
      view.index = self.view.index
      await interaction.response.edit_message(
        content = None,
        embeds = self.embeds,
        view = view
      )
    except:
      traceback.print_exc()

class EmbedRemove(ui.Select):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    if self.embeds:
      self.select_options = [discord.SelectOption(label = str(embed_count + 1)) for embed_count in range(len(self.embeds))]
    else:
      self.select_options = [discord.SelectOption(label = "None")]
    super().__init__(
      custom_id = "embed_remove",
      disabled = False if self.embeds else True,
      max_values = len(self.embeds) if self.embeds else 1,
      min_values = 1,
      options = self.select_options,
      placeholder = "Select an embed to remove"
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      indexes : list[int] = [int(index) - 1 for index in self.values][::-1]
      if len(indexes) == len(self.embeds):
        self.embeds = []
      else:
        for index in indexes:
          self.embeds.pop(index)
      if len(self.embeds) == 1:
        self.embeds[0].set_author(
          name = interaction.user.name,
          icon_url = interaction.user.display_avatar
        )
      view = ui.View(
        timeout = None
      ).add_item(
        EmbedSelect(embeds = self.embeds)
      ).add_item(
        EmbedPropertySelect(self.embeds)
      ).add_item(
        EmbedRemove(self.embeds)
      ).add_item(
        ClearButton(self.embeds)
      ).add_item(
        AddEmbed(self.embeds)
      ).add_item(
        SendButton(self.embeds)
      )
      view.index = self.view.index
      await interaction.response.edit_message(
        content = None,
        embeds = self.embeds,
        view = view
      )
    except:
      traceback.print_exc()

class EmbedPropertySelect(ui.Select):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    if self.embeds:
      self.is_disabled = False
    else:
      self.is_disabled = True
    super().__init__(
      custom_id = "embed_property_select",
      max_values = 1,
      min_values = 1,
      placeholder = "Select an embed property to edit",
      options = [
        discord.SelectOption(label = "Description"),
        discord.SelectOption(label = "Fields"),
        discord.SelectOption(label = "Footer_Icon_URL"),
        discord.SelectOption(label = "Footer_Text"),
        discord.SelectOption(label = "Image"),
        discord.SelectOption(label = "Thumbnail"),
        discord.SelectOption(label = "Timestamp"),
        discord.SelectOption(label = "Title"),
        discord.SelectOption(label = "URL")
      ],
      disabled = self.is_disabled
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      if self.view.index is None:
        await interaction.response.edit_message(
          content = "You didn't select an embed yet !"
        )
        return
      embed_property : str = self.values[0]
      if embed_property == "Fields":
        fields = interaction.message.embeds[self.view.index].fields
        view = ui.View(
          timeout = None
        )
        view.index = self.view.index
        view.add_item(EmbedFieldSelect(fields))
        view.add_item(EmbedFieldRemove(self.view.index, interaction.message.embeds))
        view.add_item(BackButton("embed_fields"))
        view.add_item(EmbedAddField())
        await interaction.response.edit_message(
          view = view
        )
        return
      await interaction.response.send_modal(PropertyEditModal(self.view.index, interaction.message.embeds, embed_property, self.view))
    except:
      traceback.print_exc()

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedSelect(ui.Select):
  def __init__(self, embeds : list[discord.Embed]) -> None:
    self.embeds : list[discord.Embed] = embeds
    if self.embeds:
      self.select_options = [discord.SelectOption(label = str(embed_count + 1)) for embed_count in range(len(embeds))]
    else:
      self.select_options = [discord.SelectOption(label = "None")]
    super().__init__(
      custom_id = "embed_select",
      max_values = 1,
      min_values = 1,
      options = self.select_options,
      placeholder = "Select an embed to edit",
      disabled = False if self.embeds else True
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    try:
      for option in self.options:
        if option.default:
          option.default = False
      value : int = int(self.values[0])
      embeds = interaction.message.embeds
      if self.view.index is not None: embeds[self.view.index].color = 0x2b2d31
      self.view.index = value - 1
      self.options[value - 1].default = True
      embeds[value - 1].color = 0x5865F2
      await interaction.response.edit_message(
        content = None,
        view = self.view,
        embeds = embeds
      )
    except:
      traceback.print_exc()

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedBuilder(commands.GroupCog, name = "embed", description = "/embed"):
  def __init__(self, bot : commands.Bot) -> None:
    self.bot : commands.Bot = bot

  @app_commands.command(
    name = "create",
    description = "Create an embed in the channel"
  )
  async def embed_create(self, interaction : discord.Interaction) -> None:
    await interaction.response.defer(
      ephemeral = True
    )
    embed : discord.Embed = discord.Embed(
      color = 0x2b2d31
    ).set_author(
      name = interaction.user.name,
      icon_url = interaction.user.display_avatar
    )
    view = ui.View(
      timeout = None
    ).add_item(
      EmbedSelect(embeds = [embed])
    ).add_item(
      EmbedPropertySelect([embed])
    ).add_item(
      EmbedRemove([embed])
    ).add_item(
      ClearButton([embed])
    ).add_item(
      AddEmbed([embed])
    ).add_item(
      SendButton([embed])
    )
    view.index = None
    await interaction.followup.send(
      embeds = [embed],
      view = view
    )

  @embed_create.error
  async def error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(EmbedBuilder(bot))