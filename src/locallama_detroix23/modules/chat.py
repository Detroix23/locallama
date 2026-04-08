"""
# Locallama.
/src/locallama_detroix23/modules/chat.py
"""

import sys
import pprint
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
	from locallama_detroix23.modules import app
from locallama_detroix23.modules import types, debug, controls

COMMAND: str = "/"

class Chat:
	"""
	# `Chat`.
	Holds the main chat and UI. 
	"""
	parent: 'app.App'
	prompt: str
	history_ai_responses: list[str]
	history_prompt: list[str]
	shell: str

	def __init__(self, parent: 'app.App') -> None:
		self.parent = parent
		self.prompt = ""
		self.history_ai_responses = list()
		self.history_prompt = list()
		self.shell = "[locallama]"

	def loop(self) -> None:
		"""
		Execute the main chat loop, user interaction.
		"""
		try:
			while True:
				sys.stdout.write("\n\n")
				controls.move_up(1)
				sys.stdout.write(f"{self.shell} ")
				sys.stdout.flush()

				self.prompt = self.listen()

				debug.log(2, self.parent.debug_level, f"(?) modules.chat.Chat.loop() Prompt: {self.prompt}")

				result = self.on_prompt()
				pprint.pprint(result)

				sys.stdout.flush()

				self.history_prompt.append(self.prompt)

		except KeyboardInterrupt:
			print("\n(!) modules.chat.Chat.loop() Keyboard interruption.")


	def listen(self) -> str:
		"""
		Listen `stdin` for prompts and sanitize.
		"""
		accepted: str = ""

		for prompt in sys.stdin:
			if prompt.strip() != "":
				accepted = prompt.strip()
				break
			
			else:
				controls.move_up(1)
				sys.stdout.write(f"{self.shell} ")
				sys.stdout.flush()
		
		return accepted

	def on_prompt(self) -> tuple[types.ResponseType, Optional[list[dict[str, object]]]]:
		"""
		Reaction on a valid prompt.
		Returns a `tuple` containing:
		- 0. The `ResponseType`.
		- 1. The prompt result content, `None` if there isn't.
		"""
		if self.prompt.startswith(COMMAND):
			return (types.ResponseType.COMMAND, self.parent.settings_manager.command(self.prompt))
		else:
			return (types.ResponseType.AI_RESPONSE, self.parent.prompter.send(self.prompt))


