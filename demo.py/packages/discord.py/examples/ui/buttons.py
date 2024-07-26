from discord import (
  Interaction,
  ButtonStyle
)
from discord.ui import (
  button,
  Button,
  View
)

# via discord.ui.Button class

class SampleButton(Button):
  def __init__(
    self,
    **kwargs
  ) -> None:
    super().__init__(
      **kwargs
    )

  async def callback(
    self,
    interaction : Interaction
  ) -> None:
    await interaction.response.send_message(
      "Button pressed !"
    )

@bot.tree.command()
async def sample(
  interaction : Interaction
) -> None:
  sample_button : Button = SampleButton(
    label = "Sample Button",
    style = ButtonStyle.primary
  )
  sample_view : View = View(
    timeout = None
  )
  smaple_view.add_item(sample_button)
  await interaction.response.send_message(
    view = sample_view
  )


# via @discord.ui.button decorator

class SampleView(View):
  def __init__(
    self
  ) -> None:
    super().__init__(
      timeout = None
    )

  @button(
    label = "Sample Button",
    style = ButtonStyle.primary
  )
  async def sample_button(
    self,
    interaction : Interaction,
    button : Button
  ) -> None:
    await interaction.response.send_message(
      "Button pressed !"
    )

@bot.tree.command()
async def sample(
  interaction : Interaction
) -> None:
  sample_view : View = SampleView()
  await interaction.response.send_message(
    view = sample_view
  )