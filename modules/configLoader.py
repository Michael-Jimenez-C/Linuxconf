import os
from modules.commons import HOME, USER, PWD

def InstallFonts():
    os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Meslo.zip")
    os.system("unzip Meslo.zip -d meslo")
    os.system("sudo cp meslo/MesloLGSNerdFontMono-Regular.ttf /usr/share/fonts/truetype/")
    os.system("sudo cp meslo/MesloLGSNerdFont-Regular.ttf /usr/share/fonts/truetype/")

def LoadConfigForTerminal(terminal, desktop):
    match terminal:
        case 'gnome-terminal':
            os.system(f"dconf load /org/gnome/terminal/ < {PWD}/dotfiles/terminal/gnome-terminal")
        case 'blackbox-terminal':
            os.system(f"dconf load /com/raggesilver/blackbox < {PWD}/dotfiles/terminal/blackbox")
        case 'kitty':
            os.system(f'git clone https://github.com/d3vjh/Dotfiles.git')
            os.system(f'cp -r Dotfiles/kitty {HOME}/.config/')
    if desktop == 'bspwm':
        tmpcnf = open(f"{HOME}/.config/sxhkd/sxhkdrc", "r").readlines()
        with open(f"{HOME}/.config/sxhkd/sxhkdrc", "w") as file:
            for line in tmpcnf:
                if "gnome-terminal" in line:
                    file.write(line.replace("gnome-terminal", terminal))
                else:
                    file.write(line)

def installPowerLevel10K():
    os.chdir(HOME)
    os.system(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {HOME}/powerlevel10k")
    os.system(f"echo 'source {HOME}/powerlevel10k/powerlevel10k.zsh-theme' >>{HOME}/.zshrc")
    os.chdir(PWD)

def setUpDotfilesFor(desktop):
    path = 'dotfiles'
    if desktop == 'bspwm':
        for i in ['bspwm','sxhkd','picom','rofi']:
            os.system(f'cp -r {path}/{i} {HOME}/.config/')
        os.system(f'chmod +x {HOME}/.config/rofi/powermenu/powermenu.sh')
    os.system(f'cp {path}/.zshrc {HOME}/.zshrc')

def setUpPolybar(type):
    if type=='Un solo panel':
        os.system(f'cp -r dotfiles/polybar {HOME}/.config/polybar')
    elif type=='Varios paneles':
        os.system(f'cp -r dotfiles/polybar2 {HOME}/.config/polybar')