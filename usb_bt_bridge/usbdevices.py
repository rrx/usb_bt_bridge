import logging

import pyudev
import simplejson as json
import yaml


log = logging.getLogger(__name__)


def hex(s):
    if s is None:
        return 0

    return int(s, 16)


def extract_device_id(device):
    return "%04x:%04x" % (hex(device.get('ID_VENDOR_ID')), hex(device.get('ID_MODEL_ID')))


def generator(usbs):
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    paths = {}

    # add existing devices
    for device in context.list_devices(subsystem='usb'):
        yield transform_device('add', device, paths, usbs)

    for device in iter(monitor.poll, None):
        yield transform_device(device.action, device, paths, usbs)


def transform_device(action, device, paths, usbs):
    # for k, v in device.items():
        # print(k,v)

    path = device.sys_path
    d = None
    if action == 'add':
        # print('add', path)
        paths[path] = device
        d = device

    elif action == 'remove':
        d = paths.get(path)
        # if d:
            # print('remove', path)
        # else:
            # print('?', path)
    else:
        return {}

    if d is None:
        return {}

    # print(action, device, devid)
    devid = extract_device_id(d)
    config = usbs.get(devid, {})
    name = config.get('name') or d.get('ID_MODEL') or d.get('DEVPATH')

    # if not config:
        # continue
    # if devid not in usbs:
        # continue

    args = {
        'name': name,
        'sys_name': d.sys_name,
        'action': action,
        'usb_id': devid,
        'device_path': d.device_path,
        'sys_path': d.sys_path,
        'device_type': d.device_type,

    }
    return args


def load_config_data(data):
    return dict([(d['usb'], d) for d in data['devices']])


def main(filename):
    data = yaml.safe_load(open(filename))
    try:
        for args in generator(load_config_data(data)):
            if args:
                print(json.dumps(args))
    except KeyboardInterrupt:
        print("Interrupt")

    log.info('exit')



