# NewRelic Indicator Applet

_A indicator applet to monitor metrics from newrelic for [Ubuntu's Unity Desktop](https://unity.ubuntu.com/)_

[![Build Status](https://travis-ci.org/Zizaco/newrelic-indicator.svg?branch=master)](https://travis-ci.org/Zizaco/newrelic-indicator)
[![License MIT](http://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

![NewRelic Indicator Screenshot](https://cloud.githubusercontent.com/assets/777635/25009105/ef94a794-203b-11e7-9745-c9720d94fc9e.png)

## Quick start

**1.** Download files

    $ git clone git@github.com:Zizaco/newrelic-indicator.git .newrelic-indicator
    $ cd .newrelic-indicator

**2.** Add your **API Key** and your **App ID** to `config.json`

**3.** Install the dependencies

    $ sudo make

**4.** Add the indicator to run at startup.

    $ make install
    Do you wish to run Newrelic Indicator at startup? [yn] y
    ...
    Added Newrelic Indicator to system startup

## Troubleshooting

You may need to install **Appindicator** in order to run the Indicator properly:

    sudo apt-get install python-appindicator

Any execution error will be written to `output.log`.

## License

Newrelic Indicator Applet is free software distributed under the terms of the [MIT license](http://opensource.org/licenses/MIT)

## Aditional information

Any questions, feel free to contact me

Any issues, please [report here](https://github.com/Zizaco/newrelic-indicator/issues)
