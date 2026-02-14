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
	settings,
)

class App:
	"""
	# `App`.
	Contains the whole state of the app.
	"""
	user_chat: chat.Chat
	prompter: prompts.Prompter
	settings_manager: settings.Settings
	host: str
	port: int
	url: str
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
		
		host: str | None = os.getenv("HHN_OLLAMA_HOST")
		self.host = host if host is not None else defaults.HOST
		
		port: str | None = os.getenv("HHN_OLLAMA_PORT")
		self.port = int(port) if port is not None else defaults.PORT
		
		self.url = f"http://{self.host}:{self.port}/api/"

		self.text_encoding = defaults.TEXT_ENCODING
		self.debug_level = debug_level

		self.user_chat = chat.Chat(self)
		self.prompter = prompts.Prompter(self)
		self.settings_manager = settings.Settings(self)


	def start(self) -> None:
		print("## Settings.")
		print(f"Host: {self.host}")
		print(f"Port: {self.port}")
		print(f"Text encoding: {self.text_encoding}")
		print(self.settings_manager.display_models())
		
		print("\n## Current.")
		print(f"Model: {self.model}")
		
		self.user_chat.loop()
