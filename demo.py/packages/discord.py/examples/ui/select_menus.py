from discord import (
  Interaction,
  SelectOption
)
from discord.ui import (
  select,
  Select,
  View
)

# via discord.ui.Select class

class SampleSelect(Select):
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
    selected : str = self.values[0]
    await interaction.response.send_message(
      f"You selected : {selected}"
    )

@bot.tree.command()
async def sample(
  interaction : Interaction
) -> None:
  sample_select : Select = SampleSelect(
    max_values = 1,
    min_values = 1,
    options = [
      SelectOption(
        label = "apple"
      ),
      SelectOption(
        label = "banana"
      ),
      SelectOption(
        label = "orange"
      )
    ],
    placeholder = "Select a fruit :"
  )
  sample_view : View = View(
    timeout = None
  )
  sample_view.add_item(sample_select)
  await interaction.response.send_message(
    view = sample_view
  )