"""
# Locallama.
/src/locallama_detroix23/__main__.py
"""

import os

import requests
import dotenv

from locallama_detroix23.modules import support

try:
	from locallama_detroix23.modules import app
except ModuleNotFoundError:
	print("(X) __main__.py No module named 'locallama_detroix23'.")
	print("\nTips:")
	print("  - Enable Python virtual environment.")
	print("  - Install the package locally with `pip install --editable .`.")
	exit(support.ExitCode.MODULE_ERROR)

def main() -> None:
	print("# Locallama.")

	dotenv.load_dotenv()

	try:
		main_app = app.App(
			debug_level=1,
		)

		main_app.start()

	except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout as connection_error:
		print("(X) __main__.main() Connection error !")
		print("Full message: ")
		print("```")
		print(connection_error)
		print("```")

		print("\nTips:")
		print("  - Ensure that the server is running.")
		print("  - Verify your environment variables: ")
		print(f"    - `HHN_OLLAMA_HOST` = {os.getenv("HHN_OLLAMA_HOST")}")
		print(f"    - `HHN_OLLAMA_PORT` = {os.getenv("HHN_OLLAMA_PORT")}")
		exit(support.ExitCode.CONNECTION_ERROR)

main()
