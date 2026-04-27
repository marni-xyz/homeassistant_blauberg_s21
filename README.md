# Home Assistant - Blauberg S21 (Extended) Custom Component

## Overview

This custom component enables local control and monitoring of your Blauberg S21 HVAC system directly within Home Assistant.

It is an extended version of **[jvitkauskas' original development](https://github.com/jvitkauskas/homeassistant_blauberg_s21)**. Many thanks for laying the foundation!

The major differences include:
- Expanded attributes: All temperatures, scheduler status
- New control functions: Timer mode, boost mode, alarm reset


## Installation and Configuration

**Please note:** This extended repo is not yet included in HACS. Hence, manual installation is required.

### Manual install
1. Copy the `blauberg_s21_ext` folder from this repository to `custom_components` directory of your Home Assistant installation.
2. Restart your HA instance.

### Setup
1. Navigate to Configuration → Integrations in the Home Assistant web interface.
2. Click the + button and select "Blauberg S21 (Extended)".
3. After configuration, your device will appear in Settings → Devices & Services.


## Development

This component is built on top of the [underlying pybls21 library](https://github.com/marni-xyz/pybls21)
