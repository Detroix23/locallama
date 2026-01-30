"""
# Locallama.
/src/locallama_detroix23/modules/app.py
"""

import os
import dotenv

from locallama_detroix23.modules import (
	defaults,
	chat,
	prompts,
)

class App:
	"""
	# `App`.
	Contains the whole state of the app.
	"""
	user_chat: chat.Chat
	prompter: prompts.Prompter
	host: str
	port: int
	model: str
	text_encoding: str
	debug_level: int

	def __init__(
		self, 
		model: str,
		debug_level: int,
	) -> None:
		dotenv.load_dotenv()

		self.model = model
		host = os.getenv("HHN_OLLAMA_HOST")
		self.host = host if host is not None else defaults.HOST
		port = os.getenv("HHN_OLLAMA_PORT")
		self.port = int(port) if port is not None else defaults.PORT
		self.text_encoding = defaults.TEXT_ENCODING
		self.debug_level = debug_level

		self.user_chat = chat.Chat(self)
		self.prompter = prompts.Prompter(self)


	def start(self) -> None:
		print("## Settings.")
		print(f" - Model: {self.model}")
		print(f" - Host: {self.host}")
		print(f" - Port: {self.port}")
		print(f" - Text encoding: {self.text_encoding}")
		
		self.user_chat.loop()
