"""
# Locallama.
/src/locallama_detroix23/modules/chat.py
"""

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from locallama_detroix23.modules import app
from locallama_detroix23.modules import (
	debug,
	controls,
)

COMMAND: str = "/"

class Chat:
	"""
	# `Chat`.
	Holds the main chat and UI. 
	"""
	parent: 'app.App'
	prompt: str
	history: list[str]
	shell: str

	def __init__(self, parent: 'app.App') -> None:
		self.parent = parent
		self.prompt = ""
		self.history = list()
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

				self.on_prompt()

				sys.stdout.flush()


				self.history.append(self.prompt)

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

	def on_prompt(self) -> None:
		"""
		Reaction on a valid prompt.
		"""
		if self.prompt.startswith(COMMAND):
			self.parent.settings_manager.command(self.prompt)
		else:
			self.parent.prompter.send(self.prompt)

