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
        'ubuntu-desktop-minimal',
        'gnome-tweaks'
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
        'bettercap',
        'netcat'
    ],
    'web': [
        'wfuzz',
        'whatweb'
    ],
    'hash' : ['hashcat','hydra'],
    'db': ['sqlitebrowser','sqlmap']
}

pipx_packages = {
    'git':['git-dumper'],
    'directorio activo': [
        'ensurepath',
        'bloodhound-ce'
        ]
}