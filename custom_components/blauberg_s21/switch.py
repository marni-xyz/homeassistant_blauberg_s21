from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from pybls21.client import S21Client
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    client: S21Client = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([
        BlaubergS21BoostSwitch(client, config_entry),
        BlaubergS21TimerSwitch(client, config_entry),
    ])


class BlaubergS21BoostSwitch(SwitchEntity):
    _attr_icon = "mdi:fan-plus"
    _attr_translation_key = "blauberg_s21_boost_switch"
    _attr_name = "Boost Mode"

    def __init__(self, client: S21Client, config_entry: ConfigEntry) -> None:
        self._client = client
        self._config_entry = config_entry
        self._attr_unique_id = f"{config_entry.unique_id}_boost_switch"

    @property
    def is_on(self) -> bool | None:
        if self._client.device:
            return self._client.device.is_boosting
        return None

    async def async_turn_on(self, **kwargs) -> None:
        await self._client.set_boost_on()

    async def async_turn_off(self, **kwargs) -> None:
        await self._client.set_boost_off()

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
        )


class BlaubergS21TimerSwitch(SwitchEntity):
    _attr_icon = "mdi:timer"
    _attr_translation_key = "blauberg_s21_timer_switch"
    _attr_name = "Timer Mode"

    def __init__(self, client: S21Client, config_entry: ConfigEntry) -> None:
        self._client = client
        self._config_entry = config_entry
        self._attr_unique_id = f"{config_entry.unique_id}_timer_switch"

    @property
    def is_on(self) -> bool | None:
        if self._client.device:
            return self._client.device.is_timer
        return None

    async def async_turn_on(self, **kwargs) -> None:
        await self._client.set_timer_on()

    async def async_turn_off(self, **kwargs) -> None:
        await self._client.set_timer_off()

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
        )
