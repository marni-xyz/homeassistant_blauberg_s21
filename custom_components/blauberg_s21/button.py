from __future__ import annotations
from homeassistant.components.button import ButtonEntity
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
        BlaubergS21ResetFilterButton(client, config_entry),
        BlaubergS21ResetAlarmButton(client, config_entry),
    ])


class BlaubergS21ResetFilterButton(ButtonEntity):
    _attr_icon = "mdi:filter-remove"
    _attr_translation_key = "blauberg_s21_reset_filter"

    def __init__(self, client: S21Client, config_entry: ConfigEntry) -> None:
        self._client = client
        self._config_entry = config_entry
        self._attr_unique_id = f"blauberg_s21_{config_entry.unique_id}_reset_filter"

    async def async_press(self) -> None:
        await self._client.reset_filter_change_timer()

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
        )


class BlaubergS21ResetAlarmButton(ButtonEntity):
    _attr_icon = "mdi:alarm-off"
    _attr_translation_key = "blauberg_s21_reset_alarm"

    def __init__(self, client: S21Client, config_entry: ConfigEntry) -> None:
        self._client = client
        self._config_entry = config_entry
        self._attr_unique_id = f"blauberg_s21_{config_entry.unique_id}_reset_alarm"

    async def async_press(self) -> None:
        await self._client.reset_alarm()

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
        )
