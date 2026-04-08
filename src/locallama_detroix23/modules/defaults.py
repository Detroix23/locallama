"""
# Locallama.
/src/locallama_detroix23/modules/defaults.py
"""

from typing import Final

HOST: Final[str] = "127.0.0.0"
PORT: Final[int] = 11434
TEXT_ENCODING: Final[str] = "utf-8"

COMMAND_CHARACTER: str = "/"

HELP_CHAT_COMMANDS: str = """
### Chat commands: HELP.
`/model [<name>]`:
- With no argument `name`, returns the current model.
- Else, switch to `name`.

`/list [r | running | a | all]`
- With no arguments or `a` or `all`, display all available models.
- With `r` or `running`, show the currently running models. 

`/details <name>`
- Returns details about the model named `name`.
"""