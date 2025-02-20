import os

HOME = os.environ.get("HOME")
USER = os.environ.get("USER")

if USER == 'root' and os.environ.get("SUDO_USER") != 'root':
    USER = os.environ.get("SUDO_USER")
    HOME = '/home/' + USER

PWD = os.environ.get("PWD")