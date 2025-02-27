import os
from .deb import deb

from modules.commons import HOME
from modules.pipxpackages import pipx_packages

import configLoader as cl


class Installer:
    def __init__(self, config):
        self.config = config
        self.PM = None
        if self.config.pm == 'apt':
            self.PM = deb
    
    def SetUpDirectories(self):
        dirs = [
            f"{HOME}/.local",
            f"{HOME}/.local/bin",
            f"{HOME}/.local/share",
            f"{HOME}/.local/share/fondos/",
            f"{HOME}/.local/nvim"
        ]
        os.system("mkdir -p "+" ".join(dirs))
        os.system("sudo mkdir -p /usr/share/fonts/truetype")
    
    def installPipxPKG(self):
        for group in self.pipx_inst:
            os.system(f"pipx install {' '.join(pipx_packages[group.split(':')[0]])}")
    

    def run(self):
        self.SetUpDirectories()
        self.PM.PackageSetup()
        self.PM.installEnviroment(self.config.desktop)
        cl.InstallFonts()
        cl.LoadConfigForTerminal(self.config.terminal, self.config.desktop)
        cl.installPowerLevel10K()
        cl.setUpDotfilesFor(self.config.desktop)
        if self.config.polybar:
            cl.setUpPolybar(self.config.polybar)
        self.PM.setUpRust()
        if self.config.yazi:
            self.PM.installYazi()
        if self.config.wallust:
            self.PM.installWallust()
        self.PM.installNvim()
        self.PM.installTerminal(self.config.terminal)
        self.PM.installOptionalPKG(self.config.pk_inst)
        self.installPipxPKG(self.config.pipx_inst)
        print("Instalación completada")
        