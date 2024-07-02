import discord
import traceback
from discord import app_commands, ui
from discord.ext import commands
from typing import Literal

class CardSelect(ui.Select):
  def __init__(self, card : str, options : list[str]) -> None:
    super().__init__(
      custom_id = "guild.profile.card_select",
      disabled = False,
      max_values = 1,
      min_values = 1,
      options = [
        discord.SelectOption(
          label = option,
          default = True if option == card else False
        )
        for option in options
      ],
      placeholder = "Select a card :"
    )
    self.cards : dict = {
      "profile": self.profile_card
    }

  async def profile_card(self, guild : discord.Guild) -> discord.Embed:
    embed : discord.Embed = discord.Embed(
      title = guild.name,
      description = f"{f"{"\n".join([f"> {line}" for line in guild.description.split("\n")])}\n\n" if guild.description else ""}" \
        f"**Created** : <t:{int(guild.created_at.timestamp())}:R>\n" \
        f"**Members** : ` {len(guild.members):,} `\n" \
        f"**Emojis** : ` {len(guild.emojis):,} | {guild.emoji_limit:,} `\n" \
        f"**Stickers** : ` {len(guild.stickers):,} | {guild.sticker_limit:,} `\n" \
        f"**Roles** : ` {len(guild.roles):,} `",
      color = 0x2b2d31
    ).add_field(
      name = f"Channels : {len(guild.channels):,}",
      value = f"> **Categories** : ` {len(guild.categories):,} `\n" if guild.categories else "" \
        f"> **Forums** :  ` {len(guild.forums):,} `\n" if guild.forums else "" \
        f"> **Stages** : ` {len(guild.stage_channels):,} `\n" if guild.stage_channels else "" \
        f"> **Texts** : ` {len(guild.text_channels):,} `\n" if guild.text_channels else "" \
        f"> **Voices** : ` {len(guild.voice_channels):,} `" if guild.voice_channelse else "",
      inline = True
    ).set_footer(
      text = f"Guild ID : {guild.id}"
    )
    if guild.owner:
      embed.set_author(
        name = guild.owner.name,
        icon_url = guild.owner.display_avatar
      )
    if guild.banner:
      embed.set_image(
        url = guild.banner.url
      )
    if guild.icon:
      embed.set_thumbnail(
        url = guild.icon.url
      )
    return embed

  async def callback(
    self,
    interaction : discord.Interaction
  ) -> None:
    value = self.values[0]
    for option in self.options:
      if option.label == value:
        option.default = True
        continue
      option.default = False
    embed : discord.Embed = await self.cards[value](interaction.guild)
    await interaction.response.edit_message(
      embed = embed,
      view = self.view
    )

class GuildInfo(commands.Cog):
  def __init__(self, bot : commands.Bot) -> None:
    self.bot : commands.Bot = bot

  guild : app_commands.Group = app_commands.Group(
    name = "guild",
    description = "/guild",
    allowed_contexts = app_commands.AppCommandContext(
      guild = True,
      dm_channel = False,
      private_channel = False
    ),
    allowed_installs = app_commands.AppInstallationType(
      guild = True,
      user = False
    )
  )

  @guild.command(
    name = "profile",
    description = "Profile card of the current guild"
  )
  async def guild_info(
    self,
    interaction : discord.Interaction,
    card : Literal["profile"] = "profile"
  ) -> None:
    guild : discord.Guild = interaction.guild
    embed : discord.Embed = discord.Embed(
      title = guild.name,
      description = f"{f"{"\n".join([f"> {line}" for line in guild.description.split("\n")])}\n\n" if guild.description else ""}" \
        f"**Created** : <t:{int(guild.created_at.timestamp())}:R>\n" \
        f"**Members** : ` {len(guild.members):,} `\n" \
        f"**Emojis** : ` {len(guild.emojis):,} | {guild.emoji_limit:,} `\n" \
        f"**Stickers** : ` {len(guild.stickers):,} | {guild.sticker_limit:,} `\n" \
        f"**Roles** : ` {len(guild.roles):,} `",
      color = 0x2b2d31
    ).add_field(
      name = f"Channels : {len(guild.channels):,}",
      value = f"> **Categories** : ` {len(guild.categories):,} `\n" if guild.categories else "" \
        f"> **Forums** :  ` {len(guild.forums):,} `\n" if guild.forums else "" \
        f"> **Stages** : ` {len(guild.stage_channels):,} `\n" if guild.stage_channels else "" \
        f"> **Texts** : ` {len(guild.text_channels):,} `\n" if guild.text_channels else "" \
        f"> **Voices** : ` {len(guild.voice_channels):,} `" if guild.voice_channels else "",
      inline = True
    ).set_footer(
      text = f"Guild ID : {guild.id}"
    )
    if guild.owner:
      embed.set_author(
        name = guild.owner.name,
        icon_url = guild.owner.display_avatar
      )
    if guild.banner:
      embed.set_image(
        url = guild.banner.url
      )
    if guild.icon:
      embed.set_thumbnail(
        url = guild.icon.url
      )
    view : ui.View = ui.View(
      timeout = None
    ).add_item(
      CardSelect(
        card,
        [
          "profile"
        ]
      )
    )
    await interaction.response.send_message(
      embed = embed,
      ephemeral = True,
      view = view
    )

  @guild_info.error
  async def error(
    self,
    interaction : discord.Interaction,
    error : Exception
  ) -> None:
    traceback.print_exc()

async def setup(bot : commands.Bot) -> None:
  await bot.add_cog(GuildInfo(bot))