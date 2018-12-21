
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-veml6070/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/veml6070/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord
    
.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_VEML6070.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_VEML6070
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

Usage Example
=============

.. code-block:: python

    import time
    import board
    import busio
    from adafruit_veml6070 import VEML6070

    with busio.I2C(board.SCL, board.SDA) as i2c:
        uv = VEML6070(i2c)
        # Alternative constructors with parameters
        #uv = VEML6070(i2c, 'VEML6070_1_T')
        #uv = VEML6070(i2c, 'VEML6070_HALF_T', True)

        # take 10 readings
        for j in range(10):
            uv_raw = uv.read
            risk_level = uv.get_index(uv_raw)
            print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))
            time.sleep(1)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_VEML6070/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-veml6070 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
