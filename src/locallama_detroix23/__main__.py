"""
# Locallama.
/src/locallama_detroix23/__main__.py
"""

import requests

try:
	from locallama_detroix23.modules import app
except ModuleNotFoundError:
	print("(X) __main__.py No module named 'locallama_detroix23'.")
	print("\nTips:")
	print("  - Enable Python virtual environment.")
	print("	 - Install the package locally with `pip install --editable .`.")
	exit(1)

def main() -> None:
	print("# Locallama.")

	try:
		main_app = app.App(
			debug_level=1,
		)

		main_app.start()

	except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout as connection_error:
		print("(X) __main__.main() Connection error !")
		print("Full message:\n```")
		print(connection_error)
		print("```")

		print("\nTips:")
		print("  - Check that the server is running.\n")

main()
