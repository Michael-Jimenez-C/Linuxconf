# Resultado

Este script es para instalar las herramientas que requiero de forma rapida y de forma semi automatica, aqui los ejemplos con bspwm.

<img src='docs/imagenes/Captura de pantalla 2025-02-20 124010.png'></img>

<img src='docs/imagenes/Captura de pantalla 2025-02-20 124426.png'></img>

# Uso
## Base Debian y Ubuntu
Requiere `python3-venv`
```sh
python3 -m venv .venv
source .venv
pip install -r requirements.txt
python install.py
```

Esto abrirá el siguiente menu en la terminal:
```
? Continuar la instalación? Yes
? Que gestor de paquetes se está utilizando? apt
? Que entorno quiere utilizar bspwm
? Instalar fuentes Nerd Fonts? Yes
? Instalar rust? (esto permitirá instalar yazi) Yes
? Instalar yazi? Yes
? Quieres instalar una terminal? kitty
? Instalar wallust? Yes
```