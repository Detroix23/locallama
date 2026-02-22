"""
# Locallama.
/src/locallama_detroix23/__main__.py
"""

import requests

from locallama_detroix23.modules import app

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