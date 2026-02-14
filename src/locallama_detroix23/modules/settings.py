"""
# Locallama.
/src/locallama_detroix23/modules/settings.py
"""

import requests
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from locallama_detroix23.modules import app

class Settings:
	"""
	# `Settings` class for the chat.
	"""
	parent: 'app.App'
	models_name: list[str]
	_cache_tags: dict[str, list[dict[str, object]]] | None

	def __init__(self, parent: 'app.App') -> None:
		self.parent = parent

		self._cache_tags = None
		self.get_tags()
		self.models_name = self.list_models_name()

	def get_tags(self) -> dict[str, list[dict[str, object]]]:
		"""
		Return a detailed list of the available models. Runs: 
		```
		api/tags
		```
		If tags where already requested, return the cached tags `_cache_tags`.

		Reference: https://docs.ollama.com/api/tags
		"""
		if self._cache_tags is not None:
			return self._cache_tags

		request: requests.Response = requests.get(
			f"{self.parent.url}tags"
		)

		content: dict[str, list[dict[str, object]]] = json.loads(request.content)
		self._cache_tags = content
		return content
	
	def get_running(self) -> dict[str, list[dict[str, object]]]:
		"""
		Return a detailed list of the currently running models. Runs: 
		```
		api/ps
		```
		Reference: https://docs.ollama.com/api/ps
		"""
		request: requests.Response = requests.get(
			f"{self.parent.url}ps"
		)

		content: dict[str, list[dict[str, object]]] = json.loads(request.content)
		return content
	
	def command(self, command: str) -> None:
		"""
		Execute the given `command`. 
		"""
		arguments: list[str] = command.split(" ")
		index: int = 0
		while index < len(arguments):
			if arguments[index] == "/model":
				if index >= len(arguments) - 1:
					print(f"Current model: {self.command_model('')}")
				else:
					if self.command_model(arguments[index + 1]) == "":
						print(f"(!) Model: {arguments[index + 1]}")
					
					index += 1

			elif arguments[index] == "/list":
				if index >= len(arguments) - 1:
					self.command_list()
				else:
					self.command_list(arguments[index + 1])
					index += 1

			else:
				print(f"(!) Argument: {arguments[index]}")	
			
			index += 1

	def command_model(self, model: str) -> str:
		"""
		Set the current model to `model`.   
		Return the empty string if the model is incorrect.  
		If `model` is empty, return the current model name.
		"""
		if model == "":
			return self.parent.model

		if model not in self.models_name:
			return ""
		
		self.parent.model = model

		return self.parent.model

	def command_list(self, option: str | None = None) -> None:
		"""
		Prints the model list. 
		Options:
		- `running` | `r`: only running models. 
		"""
		if option is None or option in {"a", "all"}:
			print(self.display_models())
		
		elif option in {'r', 'running'}:
			print(self.list_running_name())

		else:
			print(f"(!) Option: {option}")


	def list_models_name(self) -> list[str]:
		"""
		List the models `name`'s only.
		"""
		return [str(model["name"]) for model in self.get_tags()['models']]
	
	def list_running_name(self) -> list[str]:
		"""
		List the running models `name`'s only.
		"""
		return [str(model["name"]) for model in self.get_running()['models']]

	def display_models(self) -> str:
		"""
		Return a readable list of the models.
		"""
		lines: list[str] = ["Models:"]
		for index, model in enumerate(self.get_tags()['models']):
			lines.append(f" {index}. {model['name']} ({model['model']}) - \
{model['details']['parameter_size']}, {model['details']['quantization_level']}")   # type: ignore
			
		return "\n".join(lines)
	
	