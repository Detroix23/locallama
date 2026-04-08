"""
# Locallama.
/src/locallama_detroix23/modules/defaults.py
"""

from typing import Final

HOST: Final[str] = "127.0.0.0"
PORT: Final[int] = 11434
TEXT_ENCODING: Final[str] = "utf-8"

HELP_CHAT_COMMANDS: str = """
### Chat commands: HELP.
`/models [name]`:
- With no argument `name`, returns the current model.
- Else, switch to `name`.

`/list [r | running | a | all]`
- With no arguments or `a` or `all`, display all available models.
- With `r` or `running`, show the currently running models. 
"""