from .packages import packages, desktop_packages
from modules.commons import HOME, USER, PWD
import time
import os

def SetUpDirectories():
    dirs = [
        f"{HOME}/.local",
        f"{HOME}/.local/bin",
        f"{HOME}/.local/share",
        f"{HOME}/.local/share/fondos/"
        f"{HOME}/.local/.nvim"
    ]
    os.system("mkdir -p "+" ".join(dirs))
    os.system("sudo mkdir -p /usr/share/fonts/truetype")
    
def PackageSetup():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo apt install -y " + " ".join(packages))

def installEnviroment(desktop):
    os.system("sudo apt install -y " + " ".join(desktop_packages[desktop]))
    if desktop == 'bspwm':
        os.system(f"cp image/* {HOME}/.local/share/fondos/")

def InstallFonts():
    os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Meslo.zip")
    os.system("unzip Meslo.zip -d meslo")
    os.system("sudo cp meslo/MesloLGSNerdFontMono-Regular.ttf /usr/share/fonts/truetype/")

def setUpDotfilesFor(desktop, kind=None):
    path = 'dotfiles'
    if kind=='d3vjh':
        os.system("git clone https://github.com/d3vjh/Dotfiles.git")
        path = 'Dotfiles'
    if desktop == 'bspwm':
        os.system(f'cp -r {path}/* {HOME}/.config/')
    os.system(f'cp {path}/.zshrc {HOME}/.zshrc')

def setUpRust():
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
    os.system(f"source {HOME}/.cargo/env")
    os.system("rustup update")

def installYazi():
    os.system("git clone https://github.com/sxyazi/yazi.git")
    os.chdir("yazi")
    os.system("cargo build --release --locked")
    time.sleep(1)
    os.system("mv target/release/yazi target/release/ya $HOME/.local/bin")
    os.chdir(PWD)

def installPowerLevel10K():
    os.chdir(HOME)
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k")
    os.system("echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")
    os.chdir(PWD)

def installNvim():
    os.chdir(f'{HOME}/.local')
    os.system("wget https://github.com/neovim/neovim/releases/download/v0.10.4/nvim-linux-x86_64.tar.gz")
    os.system("tar -xzvf nvim-linux-x86_64.tar.gz -C nvim")
    os.system("rm nvim-linux-x86_64.tar.gz")
    os.system(f"ln -s {HOME}/.local/nvim/nvim-linux-x86_64/bin/nvim {HOME}/.local/bin/nvim")
    os.system(PWD)
    os.system("git clone https://github.com/NvChad/starter ~/.config/nvim")