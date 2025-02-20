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

kind = questionary.select(
    "Quieres copiar mis dotfiles o los de d3vjh?",
    choices=[
        'Michael',
        'd3vjh'
    ]
).ask()

rust = questionary.confirm("instalar rust? (esto permitirá instalar yazi)").ask()
yazi = False
if rust:
    yazi = questionary.confirm("instalar yazi?").ask()


script.SetUpDirectories()
script.PackageSetup()
desktop != 'Ninguno' and script.installEnviroment(desktop)
fonts and script.InstallFonts()
script.setUpDotfilesFor(desktop, kind=kind)
rust and script.setUpRust()
rust and yazi and script.installYazi()
script.installPowerLevel10K()
script.installNvim()
