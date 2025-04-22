from .packages import packages, desktop_packages, terminal_packages, other_packages
from modules.commonconstants import HOME, USER, PWD
import time
import os

def PackageSetup():
    os.system("sudo apt update")
    for i in packages:
        os.system("sudo apt install -y " + i)
    os.system('chsh -s /usr/bin/zsh')

def installEnviroment(desktop):
    for i in desktop_packages[desktop]:
        os.system("sudo apt install -y " + i)
    if desktop == 'bspwm':
        os.system(f"cp image/* {HOME}/.local/share/fondos/")

def setUpRust():
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
    os.system(f"source {HOME}/.cargo/env")
    os.system("rustup update")

def installYazi():
    os.system(f"source {HOME}/.cargo/env")
    os.system("git clone https://github.com/sxyazi/yazi.git")
    os.chdir("yazi")
    os.system(f"{HOME}/.cargo/bin/cargo build --release --locked")
    time.sleep(1)
    os.system("mv target/release/yazi target/release/ya $HOME/.local/bin")
    os.chdir(PWD)

def installNvim():
    os.chdir(f'{HOME}/.local')
    os.system("wget https://github.com/neovim/neovim/releases/download/v0.10.4/nvim-linux-x86_64.tar.gz")
    os.system("tar -xzvf nvim-linux-x86_64.tar.gz -C nvim")
    os.system("rm nvim-linux-x86_64.tar.gz")
    os.system(f"ln -s {HOME}/.local/nvim/nvim-linux-x86_64/bin/nvim {HOME}/.local/bin/nvim")
    os.system(PWD)
    os.system("git clone https://github.com/NvChad/starter ~/.config/nvim")

def installTerminal(terminal):
    if terminal == 'kitty':
        __kittyInstall()
    if terminal in terminal_packages:
        os.system("sudo apt install -y " + " ".join(terminal_packages[terminal]))

def __kittyInstall():
    os.system("curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin")
    os.system(f"ln -sf {HOME}/.local/kitty.app/bin/kitty {HOME}/.local/kitty.app/bin/kitten {HOME}/.local/bin/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty.desktop {HOME}/.local/share/applications/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty-open.desktop {HOME}/.local/share/applications/")
    os.system(f'sed -i "s|Icon=kitty|Icon=$(readlink -f {HOME})/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f'sed -i "s|Exec=kitty|Exec=$(readlink -f {HOME})/.local/kitty.app/bin/kitty|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f"echo 'kitty.desktop' > {HOME}/.config/xdg-terminals.list")

def installWallust():
    os.system(f"{HOME}/.cargo/bin/cargo install wallust")
    if 'wallust' not in open(f'{HOME}/.zshrc').read():
        with open(f'{HOME}/.zshrc','a')as file:
            file.write('\n\n')
            file.write(f'wallust run {HOME}/.local/share/fondos/fondo.png >/dev/null &')

def installOptionalPKG(groups):
    for group in groups:
        os.system("sudo apt install -y " + " ".join(other_packages[group.split(':')[0]]))