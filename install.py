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
        'blackbox-terminal',
        'Ninguna'
    ]
).ask()

wallust = None
if rust or rust_:
    wallust = questionary.confirm("Instalar wallust?").ask()

list_pk = script.other_packages
pk_inst=questionary.checkbox(
f"Paquetes {opcion} a instalar", choices=[f'{i}:{" ".join(list_pk[i])}' for i in list_pk]
).ask()

list_pk = script.pipx_packages
pipx_inst=questionary.checkbox(
f"Paquetes pipx a instalar", choices=[f'{i}:{" ".join(list_pk[i])}' for i in list_pk]
).ask()

if __name__ == '__main__':

    script.SetUpDirectories()

    script.PackageSetup()

    desktop != 'Ninguno' and script.installEnviroment(desktop)

    fonts and script.InstallFonts()

    script.setUpDotfilesFor(desktop, kind=kind)

    script.installPowerLevel10K()

    script.installNvim()

    terminal != 'Ninguna' and script.installTerminal(terminal, desktop)

    rust and script.setUpRust()
    (rust or rust_) and yazi and script.installYazi()

    (rust or rust_) and wallust and script.installWallust()

    script.installOptionalPKG(pk_inst)
    script.installPipxPKG(pipx_inst)


    script.end(desktop)