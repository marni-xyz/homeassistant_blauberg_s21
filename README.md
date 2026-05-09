# Home Assistant - Blauberg S21 (Extended) - Custom Component

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

## Overview

This custom component enables local control and monitoring of your Blauberg S21 HVAC system directly within Home Assistant.

It is an extended version of **[jvitkauskas' original development](https://github.com/jvitkauskas/homeassistant_blauberg_s21)**. Many thanks for laying the foundation!

The major differences include:
- Expanded attributes: All temperatures, scheduler status
- New control functions: Timer mode, boost mode, alarm reset


## Installation and Configuration

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=marni-xyz&repository=homeassistant_blauberg_s21&category=integration)

### Manual install
1. Copy the `blauberg_s21_ext` folder from this repository to `custom_components` directory of your Home Assistant installation.
2. Restart your HA instance.

### Setup
Configuration is done in the UI

1. Navigate to Configuration → Integrations in the Home Assistant web interface.
2. Click the + button and select "Blauberg S21 (Extended)".
3. After configuration, your device, buttons, switches will appear in Settings → Devices & Services.


## Report issues

If you have any issues with this integration, please [open an issue](https://github.com/marni-xyz/homeassistant_blauberg_s21).

Make sure to include debug logs. See https://www.home-assistant.io/integrations/logger/ for more information on how to enable debug logs.

```
logger:
  default: info
  logs:
    custom_components.blauberg_21_ext: debug
```

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)


## Dependency

This component is built on top of the [underlying pybls21 library](https://github.com/marni-xyz/pybls21)

---

[buymecoffee]: https://www.buymeacoffee.com/marnixyz
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/marni-xyz/homeassistant_blauberg_s21.svg?style=for-the-badge
[commits]: https://github.com/marni-xyz/homeassistant_blauberg_s21/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/marni-xyz/homeassistant_blauberg_s21.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40marni-xyz.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/v/release/marni-xyz/homeassistant_blauberg_s21.svg?style=for-the-badge
[releases]: https://github.com/marni-xyz/homeassistant_blauberg_s21/releases
[user_profile]: https://github.com/marni-xyz
