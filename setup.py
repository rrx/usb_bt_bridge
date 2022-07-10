
from distutils.core import setup

setup(name='usb_bt_bridge',
      version='0.0.1',
      description='Bridge between USB and Bluetooth',
      author='Ryan Sadler',
      author_email='ryan@aifuzz.com',
      url='https://github.com/rrx/usb_bt_bridge',
      packages=['usb_bt_bridge'],
      install_requires=[
          'pybluez',
          'evdev',
          'dbus-python',
          'pygobject'
      ]
     )
