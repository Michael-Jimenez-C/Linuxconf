import questionary
from modules.commons import HOME, USER
import sys

print("""
      No se recomienda ejecutar este script como superusuario.
      """)

print(f"""
    Se instalará como {USER} en {HOME}.
    """)

if not questionary.confirm("Continuar la instalación?").ask():
    sys.exit(0)

opcion = questionary.select(
    "Que gestor de paquetes se está utilizando?",
    choices=[
        'apt',
        'pacman'
    ]
).ask()

match opcion:
    case 'apt':
        from modules import deb as script
    case 'pacman':
        pass

desktop = questionary.select(
    "Que entorno quiere utilizar",
    choices=[
        'bspwm',
        'Ninguno'
    ]
).ask()

fonts = questionary.confirm("Instalar fuentes Nerd Fonts?").ask()

kind = None
'''= questionary.select(
    "Quieres copiar mis dotfiles o los de d3vjh?",
    choices=[
        'Michael',
        'd3vjh'
    ]
).ask()'''

rust = questionary.confirm("Instalar rust? (esto permitirá instalar yazi)").ask()
rust_ = False
if not rust:
    rust_ = questionary.confirm("Ya está instalado rust?").ask()

yazi = False
if rust or rust_:
    yazi = questionary.confirm("Instalar yazi?").ask()

terminal = questionary.select(
    "Quieres instalar una terminal?",
    choices=[
        'gnome-terminal',
        'kitty',
        'blackbox',
        'Ninguna'
    ]
).ask()

if rust or rust_:
    wallust = questionary.confirm("Instalar wallust?").ask()

if __name__ == '__main__':

    script.SetUpDirectories()

    script.PackageSetup()

    desktop != 'Ninguno' and script.installEnviroment(desktop)

    fonts and script.InstallFonts()

    script.setUpDotfilesFor(desktop, kind=kind)

    script.installPowerLevel10K()

    script.installNvim()

    terminal != 'Ninguna' and script.installTerminal(terminal)

    wallust and script.installWallust()

    rust and script.setUpRust()
    (rust or rust_) and yazi and script.installYazi()

    (rust or rust_) and wallust and script.installWallust()

    script.end(desktop)