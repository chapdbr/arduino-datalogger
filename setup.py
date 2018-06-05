from setuptools import setup

setup(
    name='arduino-datalogger',
    version='1.0',
    packages=['arduino-datalogger'],
    install_requires=['pyserial'],
    url='https://github.com/chapdbr/arduino-datalogger.git',
    license='MIT',
    author='Bruno Chapdelaine',
    author_email='bruno.chapdelaine@gmail.com',
    description='This software logs incoming data from an Arduino microcontroller connected via a serial port to a computer.',
    include_package_data=True
)
