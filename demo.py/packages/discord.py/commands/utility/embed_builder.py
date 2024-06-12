import discord
import traceback
from discord import app_commands, ui
from discord.ext import commands

class PropertyEditModal(ui.Modal):
  def __init__(self, embed : discord.Embed, embed_property : str) -> None:
    self.embed : discord.Embed = embed
    self.embed_property : str = embed_property
    self.properties : dict = {
      "Title": self.embed.title if self.embed.title else ""
    }
    super().__init__(
      timeout = None,
      title = "Embed Edit"
    )
    self.prompt : ui.TextInput = ui.TextInput(
      custom_id = "embed_property_edit_modal",
      default = self.properties[self.embed_property],
      label = self.embed_property,
      max_length = 256,
      min_length = 0,
      placeholder = "Leave empty to remove",
      style = discord.TextStyle.short,
      required = False
    )
    self.add_item(self.prompt)

  async def on_submit(self, interaction : discord.Interaction) -> None:
    new_value : str = str(self.prompt)
    match self.embed_property:
      case "Title":
        self.embed.title = new_value
    await interaction.response.edit_message(
      embed = self.embed
    )

  async def on_error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

class EmbedPropertySelect(ui.Select):
  def __init__(self) -> None:
    super().__init__(
      custom_id = "embed_property_select",
      max_values = 1,
      min_values = 1,
      placeholder = "Select an embed property to edit",
      options = [
        discord.SelectOption(label = "Title")
      ]
    )

  async def callback(self, interaction : discord.Interaction) -> None:
    embed_property : str = self.values[0]
    await interaction.response.send_modal(PropertyEditModal(interaction.message.embeds[0], embed_property))

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
    await interaction.followup.send(
      embed = embed,
      view = ui.View(
        timeout = None
      ).add_item(
        EmbedPropertySelect()
      )
    )

  @embed_create.error
  async def error(self, interaction : discord.Interaction, error) -> None:
    traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(EmbedBuilder(bot))