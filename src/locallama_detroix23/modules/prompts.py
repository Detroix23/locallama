"""
# Locallama.
/src/locallama_detroix23/modules/prompts.py
"""
import requests
import json
from typing import TYPE_CHECKING, Any, Final

if TYPE_CHECKING:
	from locallama_detroix23.modules import app
from locallama_detroix23.modules import debug

THINKING: Final[str] = "thinking"
RESPONSE: Final[str] = "response"
LOAD_NO_MESSAGE: Final[str] = "[locallama] load with no message."

class Prompter:
	"""
	# `Prompter`.
	Manage sending and receiving prompts.
	"""
	parent: 'app.App'

	def __init__(self, parent: 'app.App') -> None:
		self.parent = parent

	def send(self, prompt: str) -> list[dict[str, Any]]:
		"""
		Send a prompt to Ollama:
		- url: `http://{self.host}:{self.port}/api/generate`
		- Returns: `list` of JSON (Python `dict`).
		"""
		result: list[dict[str, Any]] = list()

		request: requests.Response = requests.post(
			f"http://{self.parent.host}:{self.parent.port}/api/generate",
			json={
				"model": self.parent.model,
				"prompt": prompt
			},
			stream=True,
		)

		building: list[str] = list()
		for chunk in request.iter_content(chunk_size=128):
			building.append(chunk.decode(self.parent.text_encoding))

			if building[-1][-1] in {"\n", "\r"}:

				load: dict[str, Any] = json.loads("".join(building))
				result.append(load)
				
				print(f"{self.extract_message(load)}", end="", flush=True)

				debug.log(3, self.parent.debug_level, f"Dict: {load}")

				building = list()

		print()

		return result
	
	def extract_message(self, load: dict[str, Any]) -> str:
		"""
		Get from a `load` what is to be printed to the user.
		"""
		message: str

		if THINKING in load.keys() and load[THINKING] != "":
			message = load[THINKING]
		elif RESPONSE in load.keys():
			message = load[RESPONSE]
		else:
			message = LOAD_NO_MESSAGE

		return message
