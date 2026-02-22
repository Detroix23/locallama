"""
# Locallama.
/src/locallama_detroix23/modules/settings.py
"""

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
