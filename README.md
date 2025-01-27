# Dancer
Don't worry about it.

## Install wlrctl
```
sudo apt install git libwayland-dev libinput-devbuild-essential cmake meson ninja-build scdoc libxkbcommon-dev 
git clone https://git.sr.ht/~brocellous/wlrctl
cd wlrctl
meson setup --prefix=/usr/local build
sudo ninja -C build install
```

## Install and Run
```
git clone https://github.com/unclegravity/dancer
cd dancer
uv run python dancer.py
```

## Extra: wlrctl commands

### Mouse
Move the cursor 50 pixels right and 70 pixels up
```
wlrctl pointer move 50 -70
```

### Keyboard
```
wlrctl keyboard type 'Hello, world!'
```

### Focus
Focus firefox if it is running, otherwise start firefox```
wlrctl window focus firefox || swaymsg exec firefox
```
