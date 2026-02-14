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

		If tags where already requested, return the cached tags `_cache_tags`.
		```
		"""
		if self._cache_tags is not None:
			return self._cache_tags

		request: requests.Response = requests.get(
			f"{self.parent.url}tags"
		)

		content: dict[str, list[dict[str, object]]] = json.loads(request.content)
		self._cache_tags = content
		return content
	
	def list_models_name(self) -> list[str]:
		"""
		List the models `name`'s only.
		"""
		return [str(model["name"]) for model in self.get_tags()['models']]


	def display_models(self) -> str:
		"""
		Return a readable list of the models.
		"""
		lines: list[str] = ["Models:"]
		for index, model in enumerate(self.get_tags()['models']):
			lines.append(f" {index}. {model['name']} ({model['model']}) - \
{model['details']['parameter_size']}, {model['details']['quantization_level']}")   # type: ignore
			
		return "\n".join(lines)