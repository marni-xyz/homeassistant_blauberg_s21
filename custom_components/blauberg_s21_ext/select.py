from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from pybls21.client import S21Client
from .const import DOMAIN

BYPASS_MODE_OPTIONS = ["close", "open", "auto"]

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    client: S21Client = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([
        BlaubergS21BypassModeSelect(client, config_entry),
    ])


class BlaubergS21BypassModeSelect(SelectEntity):
    _attr_icon = "mdi:swap-horizontal"
    _attr_translation_key = "blauberg_s21_bypass_mode"
    _attr_name = "Bypass Mode"

    def __init__(self, client: S21Client, config_entry: ConfigEntry) -> None:
        self._client = client
        self._config_entry = config_entry
        self._attr_unique_id = f"blauberg_s21_{config_entry.unique_id}_bypass_mode"
        self._attr_options = BYPASS_MODE_OPTIONS

    @property
    def available(self) -> bool:
        if self._client.device is None:
            return False
        return self._client.device.bypass_type is not None and self._client.device.bypass_type > 0

    @property
    def current_option(self) -> str | None:
        if self._client.device is None or self._client.device.bypass_mode is None:
            return None
        return BYPASS_MODE_OPTIONS[self._client.device.bypass_mode]

    async def async_select_option(self, option: str) -> None:
        mode = BYPASS_MODE_OPTIONS.index(option)
        await self._client.set_bypass_mode(mode)

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
        )