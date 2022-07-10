import logging
import usb
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


def generator(data):
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='input')
    paths = {}

    def transform_device(action, device):
        if not device.device_node:
            return {}, None

        path = device.device_node

        d = None
        if action == 'add':
            paths[path] = device
            d = device

        elif action == 'remove':
            d = paths.pop(path, None)
        else:
            return {}, None

        if d is None:
            return {}, None

        devid = extract_device_id(d)
        config = data.get(devid, {})
        name = config.get('name') or d.get('ID_MODEL') or d.get('DEVPATH')

        args = {
            'name': name,
            'sys_name': d.sys_name,
            'action': action,
            'usb_id': devid,
            'device_path': d.device_path,
            'sys_path': d.sys_path,
            'device_type': d.device_type,
            'known': devid in data,
            'device_node': d.device_node,
            'init': d.is_initialized,
            'subsystem': d.subsystem
        }
        return args, d

    # add existing devices
    for device in context.list_devices(subsystem='input'):
        yield transform_device('add', device)

    for device in iter(monitor.poll, None):
        yield transform_device(device.action, device)


def load_config_data(data):
    return dict([(d['usb'], d) for d in data['devices']])


def main(kbd, filename):
    data = yaml.safe_load(open(filename))
    try:
        for args, device in generator(load_config_data(data)):
            if args and args['known']:
                if args['action'] == 'add':
                    kbd.device_add(args, device)
                # elif args['action'] == 'remove':
                    # kbd.device_remove(args, device)

    except KeyboardInterrupt:
        log.error("Interrupt")

    log.info('exit')



