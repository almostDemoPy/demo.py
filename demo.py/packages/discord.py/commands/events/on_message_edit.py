import discord
import json
import traceback
from datetime import datetime
from discord import app_commands, ui
from discord.ext import commands

class ShowHideOriginal(ui.Button):
  def __init__(self) -> None:
    super().__init__(
      custom_id = "on_message_edit.buttons.show_hide_original",
      label = "Show Original",
      style = discord.ButtonStyle.gray
    )

  async def callback(
    self,
    interaction : discord.Interaction
  ) -> None:
    embed : discord.Embed = self.view.get_message(self.view.before if self.label == "Show Original" else self.view.after)
    self.label : str = "Hide Original" if self.label == "Show Original" else "Show Original"
    self.style : discord.ButtonStyle = discord.ButtonStyle.primary if self.label == "Show Original" else discord.ButtonStyle.gray
    await interaction.response.edit_message(
      embed = embed,
      view = self.view
    )

class DeleteMessage(ui.Button):
  def __init__(self) -> None:
    super().__init__(
      custom_id = "on_message_edit.buttons.delete_message",
      label = "Delete Message",
      style = discord.ButtonStyle.red
    )

  async def callback(
    self,
    interaction : discord.Interaction
  ) -> None:
    try:
      await self.view.before.delete()
    except discord.Forbidden:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = "I don't have permission to delete this message",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.cliennt.user.display_avatar
        ),
        ephemeral = True
      )
      return
    except discord.NotFound:
      self.label : str = "Deleted"
      self.disabled : bool = True
      await interaction.message.edit(
        view = self.view
      )
      await interaction.response.send_message(
        embed = discord.Embed(
          description = "The message has already been deleted",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      return
    except:
      await interaction.response.send_message(
        embed = discord.Embed(
          description = "Something went wrong",
          color = 0xff3131
        ).set_author(
          name = interaction.client.user.name,
          icon_url = interaction.client.user.display_avatar
        ),
        ephemeral = True
      )
      traceback.print_exc()
      return
    self.label : str = "Deleted"
    self.disabled : bool = True
    await interaction.message.edit(
      view = self.view
    )
    await interaction.response.send_message(
      embed = discord.Embed(
        description = "Successfully deleted the message",
        color = 0x39ff14
      ).set_author(
        name = interaction.client.user.name,
        icon_url = interaction.clietn.user.display_avatar
      ),
      ephemeral = True
    )

class OnMessageEditView(ui.View):
  def __init__(
    self,
    before : discord.Message,
    after : discord.Message
  ) -> None:
    super().__init__(
      timeout = None
    )
    self.before : discord.Message = before
    self.after : discord.Message = after
    self.add_item(ShowHideOriginal())
    self.add_item(DeleteMessage())

  def get_message(self, message : discord.Message) -> discord.Embed:
    embed : discord.Embed = discord.Embed(
      description = message.description if message.description else "",
      color = 0x2b2d31,
      timestamp = datetime.now()
    ).set_author(
      name = message.author.name,
      icon_url = message.author.display_avatar
    ).set_footer(
      text = f"Message ID : {message.id}"
    ).add_field(
      name = "Created",
      value = f"> <t:{int(message.created_at.timestamp())}:R>",
      inline = True
    ).add_field(
      name = "Is Pinned",
      value = f"> ` {str(message.pinned)} `",
      inline = True
    )
    if message.attachments:
      embed.add_field(
        name = f"Attachments ( {len(message.attachments):,} )",
        value = f"{"\n".join([f"> [{attachment.filename}](<{attachment.url}>)" for attachment in message.attachments])}",
        inline = False
      )
    return embed

  async def on_error(
    self,
    interaction : discord.Interaction,
    error : Exception
  ) -> None:
    traceback.print_exc()

class OnMessageEditEvent(commands.Cog):
  def __init__(self, bot : commands.Bot) -> None:
    self.bot : commands.Bot = bot
    self.default_data : dict[str, int | None] = {
      "on_message_edit": None
    }

  @commands.Cog.listener()
  async def on_message_edit(
    self,
    before : discord.Message,
    after : discord.Message
  ) -> None:
    try:
      if before.author == self.bot.user: return
      with open('json/events.json', 'r') as f:
        file : TextIO = json.load(f)
      guild_data : dict[str, int | None] = file.get(
        str(before.guild.id),
        self.default_data
      )
      if not guild_data["on_message_edit"]:
        return
      log_channel : discord.TextChannel = self.bot.get_channel(guild_data["on_message_edit"])
      view : ui.View = OnMessageEditView(before, after)
      editted_embed : discord.Embed = discord.Embed(
        description = after.description if after.description else "",
        color = 0x2b2d31,
        timestamp = datetime.now()
      ).set_author(
        name = before.author.name,
        icon_url = before.author.display_avatar
      ).set_footer(
        text = f"Message ID : {before.id}"
      ).add_field(
        name = "Created",
        value = f"> <t:{int(after.created_at.timestamp())}:R>",
        inline = True
      ).add_field(
        name = "Is Pinned",
        value = f"> ` {str(after.pinned)} `",
        inline = True
      )
      if after.attachments:
        editted_embed.add_field(
          name = f"Attachments ( {len(after.attachments):,} )",
          value = f"{"\n".join([f"> [{attachment.filename}](<{attachment.url}>)" for attachment in after.attachments])}",
          inline = False
        )
      await log_channel.send(
        embed = editted_embed,
        view = view
      )
    except:
      traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(OnMessageEditEvent(bot))