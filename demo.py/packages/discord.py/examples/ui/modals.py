from discord import (
  Interaction,
  TextStyle
)
from discord.ui import (
  Modal,
  TextInput
)

class SampleModal(Modal):
  def __init__(
    self
  ) -> None:
    super().__init__(
      title = "Modal title"
    )

  text : TextInput = TextInput(
    label = "field label",
    style = TextStyle.long,
    placeholder = "field placeholder"
  )

  async def on_submit(
    self,
    interaction : Interaction
  ) -> None:
    text_value : str = self.text.value
    await interaction.response.send_message(
      f"text : {text_value}"
    )

@bot.tree.command()
async def sample(
  interaction : Interaction
) -> None:
  await interaction.response.send_modal(SampleModal())