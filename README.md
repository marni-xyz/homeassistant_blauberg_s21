# Home Assistant - Blauberg S21 (Extended) Custom Component

# What This Is

This is a custom component that allows you to control and monitor your Blauberg S21 HVAC system locally within Home Assistant.

It is an extended version of [jvitkauskas' development](https://github.com/jvitkauskas/homeassistant_blauberg_s21)). Without their efforts, this would not have been possible.

The major differences include:
- More attributes (all temperatures, scheduler status)
- Additional functions to change settings (timer, boost mode)

# Installation and Configuration

Please note: This extended repo is not yet included in HACS. Hence, manual installation is required.

## Manual install
Copy `blauberg_s21_ext` folder from this repository to `custom_components` of your Home Assistant instalation. Restart your HA instance.

To configure this integration, go to Home Assistant web interface Configuration -> Integrations and then press "+" button and select "Blauberg S21 (Extended)".

When you are done with configuration you should see your device in Settings -> Devices & Services

# Development

See [underlying pybls21 library](https://github.com/marni-xyz/pybls21)
