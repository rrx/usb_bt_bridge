default:

start:
	sudo -E ~/.asdf/shims/python -m usb_bt_bridge config.yaml

start_bluetooth:
	sudo systemctl stop bluetooth
	sudo bluetoothd --compat -n -d -P "*"

up:
	sudo bash ./up.sh

