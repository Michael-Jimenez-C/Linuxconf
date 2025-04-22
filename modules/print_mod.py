class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[33m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def error(msg: str):
    print(f"{Colors.RED}[Error] {msg}{Colors.RESET}")

def success(msg: str):
    print(f"{Colors.GREEN}[Success]{Colors.RESET} {msg}")

def warning(msg: str):
    print(f"{Colors.YELLOW}[Warning] {msg}{Colors.RESET}")

def info(msg: str):
    print(f"{Colors.BLUE}[Info] {msg}{Colors.RESET}")