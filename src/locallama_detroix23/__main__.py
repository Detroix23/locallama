"""
# Locallama.
/src/locallama_detroix23/__main__.py
"""

from locallama_detroix23.modules import app

def main() -> None:
	print("# Locallama.")

	main_app = app.App(
		"deepseek-r1:7b",
		1
	)

	main_app.start()

main()