import questionary
from modules.commonconstants import HOME, USER
from modules.pipxpackages import pipx_packages
from modules.installer import Installer
from modules.print_mod import info, warning

warning("""
      No se recomienda ejecutar este script como superusuario.
      """)

info(f"""
    Se instalará como {USER} en {HOME}.
    """)


class Config:
    def __init__(self):
        self.pm = None
        self.desktop = None
        self.polybar = None
        self.fonts = None
        self.rust = None
        self.rustAlreadyInstalled = None
        self.yazi = None
        self.terminal = None
        self.wallust = None
        self.pk_inst = None
        self.pipx_inst = None
    
    def __repr__(self):
        return str(getattr(self, '__dict__'))

class Menu:
    def __init__(self):
        self.config = Config()
        if not questionary.confirm("Continuar la instalación?").ask():
            return  
    
    def run(self):
        self.getPM()
        self.getDesktop()
        self.getFonts()
        self.getRust()
        self.getTerminal()
        self.getPK()
        self.getPipx()

        installer = Installer(self.config)
        installer.run()
    
    def getPM(self):
        self.config.pm = questionary.select(
            "seleccione la distro",
            choices=[
                'debian'
            ]
        ).ask()
    
    def getDesktop(self):
        self.config.desktop = questionary.select(
            "Que entorno quiere utilizar",
            choices=[
                'bspwm',
                'Ninguno'
            ]
        ).ask()
        if self.config.desktop == 'Ninguno':
            self.config.desktop = None
        if self.config.desktop == 'bspwm':
            self.getPolybar()

    def getPolybar(self):
        self.config.polybar = questionary.select(
            "Diseño de la polybar?",
            choices=[
                'Un solo panel',
                'Varios paneles'
            ]
        ).ask()
    
    def getFonts(self):
        self.config.fonts = questionary.confirm("Instalar fuentes Nerd Fonts?").ask()

    def getRust(self):
        self.config.rust = questionary.confirm("Instalar rust? (esto permitirá instalar yazi)").ask()
        self.config.rustAlreadyInstalled = False
        if not self.config.rust:
            self.config.rustAlreadyInstalled = questionary.confirm("Ya está instalado rust?").ask()
        
        if self.config.rust or self.config.rustAlreadyInstalled:
            self.config.yazi = questionary.confirm("Instalar yazi?").ask()
            self.config.wallust = questionary.confirm("Instalar wallust?").ask()

    def getTerminal(self):
        self.config.terminal = questionary.select(
            "Quieres instalar una terminal?",
            choices=[
                'gnome-terminal',
                'kitty',
                'blackbox-terminal',
                'Ninguna'
            ]
        ).ask()
    
    def getPK(self):
        pm_packages = None
        pm = self.config.pm
        packages = []
        if pm == 'debian':
            import modules.deb.deb as pm_packages
        list_pk = pm_packages.other_packages
        for package in list_pk:
            packages.extend(questionary.checkbox(
            f"Paquetes adicionales del grupo {package} a instalar", choices=list_pk[package]).ask())
        self.config.pk_inst = packages

    def getPipx(self):
        list_pk = pipx_packages
        packages = []
        for package in list_pk:
            packages.extend(questionary.checkbox(
            f"Paquetes pipx del grupo {package}", choices=list_pk[package]).ask())
        self.config.pipx_inst = packages

if "__main__"==__name__:
    menu = Menu()
    menu.run()
    print(menu.config)
