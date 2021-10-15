Using a Raspberry Pi to bridge between a USB keyboard connected to the Pi, and then behave like a bluetooth keyboard for clients.


# Setup

Install:
```bash
sudo apt install bluez libbluetooth-dev libgirepository1.0-dev
pip install -r requirements.txt
```

# Arch Setup

```
pacman -Sy python-pip python-gobject python-dbus python-evdev python-pybluez python-pyusb python-pyudev python-simplejson python-yaml bluez bluez-plugins bluez-utils bluez-tools
systemctl start bluetooth
sudo systemctl enable bluetooth
```

