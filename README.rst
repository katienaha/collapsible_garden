==================
collapsible_garden
==================


.. image:: https://img.shields.io/pypi/v/collapsible_garden.svg
        :target: https://pypi.python.org/pypi/collapsible_garden

.. image:: https://img.shields.io/travis/katienaha/collapsible_garden.svg
        :target: https://travis-ci.com/katienaha/collapsible_garden

.. image:: https://readthedocs.org/projects/collapsible-garden/badge/?version=latest
        :target: https://collapsible-garden.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A Raspberry Pi-automated garden for terrible plant owners


* Free software: MIT license
* Documentation: https://collapsible-garden.readthedocs.io.


Features
--------

* TODO

Components
--------

* TODO

Instructions
--------

On the Raspberry Pi:

Install the module for controlling Raspberry Pi GPIO channels:
sudo apt-get install python-rpi.gpio

Add the garden's startup script to the Raspberry Pi's rc.local by adding the line:
sudo python /path/to/collapsible_garden/collapsible_garden.py &

Reset the Raspberry Pi, wait for it to boot, and follow the LCD display's prompts.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _keypad: https://www.adafruit.com/product/3845
.. _lcd: https://www.adafruit.com/product/1447
.. _power_relay: https://www.adafruit.com/product/2935
.. _liquid_level_sensor: https://www.amazon.com/gp/product/B072QCHQ2P/

