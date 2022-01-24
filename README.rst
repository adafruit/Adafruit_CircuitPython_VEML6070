
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-veml6070/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/veml6070/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_VEML6070/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_VEML6070/actions/
    :alt: Build Status

CircuitPython driver for the `VEML6070 UV Index Sensor Breakout <https://www.adafruit.com/product/2899>`_

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-veml6070/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-veml6070

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-veml6070

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-veml6070

Usage Example
=============

.. code-block:: python3

    import time
    import board
    from adafruit_veml6070 import VEML6070

    with board.I2C() as i2c:
        uv = VEML6070(i2c)
        # Alternative constructors with parameters
        #uv = VEML6070(i2c, 'VEML6070_1_T')
        #uv = VEML6070(i2c, 'VEML6070_HALF_T', True)

        # take 10 readings
        for j in range(10):
            uv_raw = uv.uv_raw
            risk_level = uv.get_index(uv_raw)
            print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))
            time.sleep(1)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/veml6070/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_VEML6070/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
