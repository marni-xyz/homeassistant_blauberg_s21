"""Models for the Blauberg S21 integration."""

from homeassistant.components.climate import FAN_OFF, FAN_LOW, FAN_MEDIUM, FAN_HIGH
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity

from .device import build_device_info

ALARM_STATES: dict[int] = {
    0: "No",
    1: "Alarm",
    2: "Warning"
}

FILTER_STATES: dict[int] = {
    0: "Clean",
    1: "The intake supply filter is clogged,",
    2: "The extract filter is clogged,",
    3: "Both filters are clogged or the filter replacement timer has gone off"
}

S21_TO_HA_FAN_MODE = {
    0: FAN_OFF,
    1: FAN_LOW,
    2: FAN_MEDIUM,
    3: FAN_HIGH,
    255: "custom"
}

class S21Entity(Entity):
    _attr_should_poll = False

    """Representation of a S21 entity."""
    async def async_added_to_hass(self) -> None:
        """Subscribe to coordinator updates."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def available(self) -> bool:
        if self.coordinator.data is None:
            return False

        return self.coordinator.data.get("available", False)

    @property
    def device_info(self) -> DeviceInfo | None:
        entry_unique_id = (
            self._config_entry.unique_id
            or self.coordinator.data.get("unique_id", "unknown")
        )
        return build_device_info(self.coordinator, entry_unique_id, self._config_entry.title)


###TODO ALIGN WITH BIRDIE1
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

TEMP_CELSIUS: str = "°C"

class ClimateEntityFeature(int, Enum):
    TARGET_TEMPERATURE = 1
    FAN_MODE = 8

class HVACMode(str, Enum):
    OFF =       "off"
    HEAT =      "heat"
    COOL =      "cool"
    AUTO =      "auto"
    FAN_ONLY =  "fan_only"

class HVACAction(str, Enum):
    COOLING =   "cooling"
    FAN =       "fan"
    HEATING =   "heating"
    IDLE =      "idle"
    OFF =       "off"

class BypassType(int, Enum):
    NOT_AVAILABLE      = 0
    BYPASS_TWO_POINT   = 1  # Discrete open/closed bypass damper control
    BYPASS_ANALOGUE    = 2  # Bypass damper position controlled 0-100%
    ROTOR_DISCRETE     = 3  # Discrete on/off rotary heat exchanger control
    ROTOR_ANALOGUE     = 4  # Rotary heat exchanger speed controlled 0-100%
    BYPASS_THREE_POINT = 5  # Bypass damper driven open/closed via timed pulses

class BypassMode(int, Enum):
    CLOSED = 0  # Close the bypass / start the rotor
    OPEN   = 1  # Open the bypass / stop the rotor (discrete), or manual % (analogue)
    AUTO   = 2  # Device controls bypass/rotor automatically based on temperature

@dataclass
class ClimateDevice:
    available:                  bool
    name:                       str
    unique_id:                  str
    temperature_unit:           str
    precision:                  float
    current_temperature:        float
    target_temperature:         float
    target_temperature_step:    float
    max_temp:                   float
    min_temp:                   float
    hvac_mode:                  str
    hvac_action:                str
    hvac_modes:                 List[str]
    supported_features:         int
    manufacturer:               str
    is_boosting:                bool
    current_intake_temperature: float
    manual_fan_speed_percent:   int
    max_fan_level:              int
    filter_state:               int
    alarm_state:                int
    supply_fan_rpm:             int
    extract_fan_rpm:            int

    # birdie1 additions
    engine_running_time: int
    supply_airflow:      int
    extract_airflow:     int
    supply_fan_speed:    int
    extract_fan_speed:   int
    # EO birdie1 additions

    current_supply_temperature:  float
    current_extract_temperature: float
    current_exhaust_temperature: float
    is_timer:                    bool
    is_schedule_mode:            bool
    bypass_position:             int
    bypass_position_manual:      int
    bypass_type:                 BypassType
    bypass_mode:                 BypassMode
    alarm_codes:                 list[int] = field(default_factory=list)

    current_humidity: Optional[float] = None
    fan_mode:         Optional[int] = None
    fan_modes:        Optional[List[int]] = None
    model:            Optional[str] = None
    sw_version:       Optional[str] = None

    filter_countdown_days:   Optional[int] = None
    filter_countdown_hrs:    Optional[int] = None
    filter_countdown_min:    Optional[int] = None
    timer_countdown:         Optional[str] = None
    supply_pressure:         Optional[int] = None
    extract_pressure:        Optional[int] = None
    fan_level_schedule_mode: Optional[int] = None
    fan_level_manual_mode:   Optional[int] = None
