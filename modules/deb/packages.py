packages = [
    "flatpak",
    "vim",
    "zsh",
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
    "python3-venv",
    "python3-pip",
    "git",
    "pipx",
    "ffmpeg",
    "7zip",
    "jq",
    "poppler-utils",
    "fd-find",
    "ripgrep",
    "fzf",
    "zoxide",
    "imagemagick",
    "make",
    "unzip",
    "bat",
    "jq"
]

desktop_packages = {
    'bspwm':[
        "bspwm",
        "sxhkd",
        "picom",
        "rofi",
        "polybar",
        "feh",
        "gnome-terminal"
        ],
    'gnome':[
        'gnome-shell',
        'ubuntu-gnome-desktop',
        'gnome-tweaks',
        'language-pack-gnome-es',
        'gnome-shell-extensions'
    ]
}


terminal_packages = {
    'blackbox-terminal': ['blackbox-terminal'],
    'gnome-terminal': ['gnome-terminal']
}


other_packages = {
    'contendores':['podman'],
    'redes':[
        'nmap',
        'wireshark',
        'bettercap'
    ],
    'web': [
        'wfuzz',
        'whatweb',
        'ffuf'
    ],
    'hash' : ['hashcat','hydra'],
    'db': ['sqlitebrowser','sqlmap'],
    'Directorio Activo': ['smb-client']
}

pipx_packages = {
    'git':['git-dumper'],
    'Directorio Activo': [
        'ensurepath',
        'bloodhound-ce'
        ]
}