#btmgmt --index hci0 power on
#btmgmt --index hci0 power off
#btmgmt --index hci0 public-addr 00:01:02:03:04:06
btmgmt --index hci0 power on
btmgmt --index hci0 class 5 64
btmgmt --index hci0 name KBD3 kbd3
btmgmt --index hci0 connectable on
bluetoothctl discoverable on
