default:

cleanup:
	sudo sdptool del 0x10000
	sudo sdptool del 0x10001
	sudo sdptool del 0x10002
	sudo sdptool del 0x10003
	sudo sdptool del 0x10004
	sudo sdptool del 0x10005
	sudo sdptool del 0x10006
	sudo sdptool del 0x10007
	sudo sdptool del 0x10008

start:
	sudo -E ~/.asdf/shims/python -m usb_bt_bridge config.yaml

start_bluetooth:
	sudo systemctl stop bluetooth
	sudo pulseaudio -k || true
	sudo bluetoothd --compat -n -d -P input

up:
	sudo bash ./up.sh

