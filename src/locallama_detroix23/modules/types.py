"""
# Locallama.
/src/locallama_detroix23/modules/settings.py
"""

import enum

class ConnectionError(Exception):
	"""
	# `ConnectionError` to the Ollama server.
	"""
	message: str

	def __init__(self, message: str, *args: object) -> None:
		super().__init__(*args)
		self.message = message

	def get_message(self) -> str:
		return self.message


class ResponseType(enum.Enum):
	"""
	# Chat `ResponseType`. 
	"""
	NONE = 0
	AI_RESPONSE = 1
	COMMAND = 2

class AiResponse:
	"""
	# `AiResponse`, in a readable way.
	"""
	think: str
	response: str
	model: str
	date: str

	def __init__(self, think: str, response: str, model: str, date: str) -> None:
		self.think = think
		self.response = response
		self.model = model
		self.date = date
	