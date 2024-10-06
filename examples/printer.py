from typing import List, Tuple

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def print_colored(text: str) -> None:
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.CYAN]
    rainbow_text = ''
    for i, char in enumerate(text.split()):
        color = colors[i % len(colors)]
        rainbow_text += f"{color}{char} "
    print(f"{rainbow_text}{Colors.RESET}")

print_colored("Welcome to this brave new world")