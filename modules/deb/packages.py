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
    "bat"
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
    ]
}


terminal_packages = {
    'blackbox': ['blackbox-terminal'],
    'gnome-terminal': ['gnome-terminal']
}


other_packages = {
    'red':[
        'nmap',
        'wireshark',
        'hydra',
        'sqlmap',
        'bettercap',
        'netcat'
    ],
    'web': [
        'wfuzz',
        'whatweb'
    ],
    'hash' : ['hashcat'],
    'db': ['sqlitebrowser']
}