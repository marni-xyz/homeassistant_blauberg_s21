"""The Blauberg S21 integration."""
# MaNi + birdie1 additions
# birdie1 PR #15 - Change to use the Homeassistant DataUpdateCoordinator

from __future__ import annotations
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .client import S21Client
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
PLATFORMS: list[Platform] = [
    Platform.CLIMATE,
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.SELECT,
    Platform.SWITCH,
]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up Blauberg S21 from a config entry."""

    ###hass.data.setdefault(DOMAIN, {})
    async def _async_update_data():
        """Fetch the latest sensor data from the device."""
        client = hass.data[DOMAIN][config_entry.entry_id]["client"]
        data = await client.poll()
        return data

    async def _async_reset_maintenance_timer(call: ServiceCall) -> None:
        """Reset the maintenance timer."""
        client = hass.data[DOMAIN][config_entry.entry_id]["client"]
        await client.reset_filter_change_timer()

    async def _async_reset_alarm(call: ServiceCall) -> None:
        """Reset the maintenance timer."""
        client = hass.data[DOMAIN][config_entry.entry_id]["client"]
        await client.reset_alarm()

    ###host = entry.data[CONF_HOST]
    host = config_entry.options.get(
        CONF_HOST,
        config_entry.data[CONF_HOST],
    )

    ###port = entry.data[CONF_PORT]
    port = config_entry.options.get(
        CONF_PORT,
        config_entry.data.get(CONF_PORT, 502),
    )

    try:
        client = S21Client(host, port)
        ###await client.poll()
    except Exception as ex:
        raise ConfigEntryNotReady(
            f"Failed to connect to modbusTCP://{host}:{port}"
        ) from ex

    ###hass.data[DOMAIN][entry.entry_id] = client
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="Blauberg S21 Sensor",
        config_entry=config_entry,
        update_method=_async_update_data,
        update_interval=timedelta(seconds=30)
    )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = {
        "client": client,
        "coordinator": coordinator,
    }

    await coordinator.async_config_entry_first_refresh()


    ###await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    #entry.async_on_unload(entry.add_update_listener(update_listener))

    # Reload the integration when options change
    config_entry.async_on_unload(
        config_entry.add_update_listener(async_reload_entry)
    )

    hass.services.async_register(
        DOMAIN,
        "reset_maintenance_timer",
        _async_reset_maintenance_timer,
    )
    hass.services.async_register(
        DOMAIN,
        "reset_alarm",
        _async_reset_alarm,
    )
    return True


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload the integration when options change."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
        hass.services.async_remove(DOMAIN, "reset_maintenance_timer")
        hass.services.async_remove(DOMAIN, "reset_alarm")

    return unload_ok
