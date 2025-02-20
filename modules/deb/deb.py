from .packages import packages, desktop_packages, terminal_packages
from modules.commons import HOME, USER, PWD
import time
import os

def SetUpDirectories():
    dirs = [
        f"{HOME}/.local",
        f"{HOME}/.local/bin",
        f"{HOME}/.local/share",
        f"{HOME}/.local/share/fondos/",
        f"{HOME}/.local/nvim"
    ]
    os.system("mkdir -p "+" ".join(dirs))
    os.system("sudo mkdir -p /usr/share/fonts/truetype")
    
def PackageSetup():
    os.system("sudo apt update > /dev/null")
    os.system("sudo apt upgrade -y > /dev/null")
    os.system("sudo apt install -y " + " ".join(packages))
    os.system('chsh -s /usr/bin/zsh')

def installEnviroment(desktop):
    os.system("sudo apt install -y " + " ".join(desktop_packages[desktop]))
    if desktop == 'bspwm':
        os.system(f"cp image/* {HOME}/.local/share/fondos/")

def InstallFonts():
    os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Meslo.zip")
    os.system("unzip Meslo.zip -d meslo")
    os.system("sudo cp meslo/MesloLGSNerdFontMono-Regular.ttf /usr/share/fonts/truetype/")
    os.system("sudo cp meslo/MesloLGSNerdFont-Regular.ttf /usr/share/fonts/truetype/")

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
    os.system(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {HOME}/powerlevel10k")
    os.system(f"echo 'source {HOME}/powerlevel10k/powerlevel10k.zsh-theme' >>{HOME}/.zshrc")
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
        __LoadConfigForTerminal(terminal)

def __kittyInstall():
    os.system("curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin")
    os.system(f"ln -sf {HOME}/.local/kitty.app/bin/kitty {HOME}/.local/kitty.app/bin/kitten {HOME}/.local/bin/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty.desktop {HOME}/.local/share/applications/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty-open.desktop {HOME}/.local/share/applications/")
    os.system(f'sed -i "s|Icon=kitty|Icon=$(readlink -f {HOME})/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f'sed -i "s|Exec=kitty|Exec=$(readlink -f {HOME})/.local/kitty.app/bin/kitty|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f"echo 'kitty.desktop' > {HOME}/.config/xdg-terminals.list")

def __LoadConfigForTerminal(terminal, desktop):
    match terminal:
        case 'gnome-terminal':
            os.system("dconf load /org/gnome/terminal/ < dotfiles/terminal/gnome-terminal")
        case 'blackbox-terminal':
            os.system("dconf load /com/raggesilver/blackbox < dotfiles/terminal/blackbox")
    if desktop == 'bspwm':
        tmpcnf = open(f"{HOME}/.config/sxhkd/sxhkdrc", "r").readlines()
        with open(f"{HOME}/.config/sxhkd/sxhkdrc", "w") as file:
            for line in tmpcnf:
                if "gnome-terminal" in line:
                    file.write(line.replace("gnome-terminal", terminal))
                else:
                    file.write(line)

def installWallust():
    os.system("cargo install wallust")
    if 'wallust' not in open(f'{HOME}/.zshrc').read():
        with open(f'{HOME}/.zshrc','a')as file:
            file.write('\n\n')
            file.write(f'wallust run {HOME}/.local/share/fondos/fondo.png >/dev/null &')

def end(desktop):
    print(
    f"""
    Los archivos de configuración se encuentran en {HOME}/.config
    La imagen de fondo por defecto está en {HOME}/.local/share/fondos
    si deseas cambiarla recuerda modificar .zshrc {'Y el entorno de escritorio '+desktop if desktop != 'Ninguno' else ''}
    """
    )