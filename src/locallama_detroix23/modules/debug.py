"""
# Locallama.
/src/locallama_detroix23/modules/debug.py
"""

import sys

def log(level: int, current: int, message: str, end: str = "\n", flush: bool = True) -> None:
	"""
	Debug prints and logs to the console `message` if `current` >= `level`.
	"""
	if current >= level:
		sys.stdout.write(f"{message}{end}")
		if flush:
			sys.stdout.flush()
	