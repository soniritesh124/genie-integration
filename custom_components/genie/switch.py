import requests
from homeassistant.components.switch import SwitchEntity
from .const import ADDON_URL

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([GenieSwitch()])

class GenieSwitch(SwitchEntity):
    name = "Genie Device"

    def __init__(self):
        self._state = False

    @property
    def is_on(self):
        return self._state

    async def async_turn_on(self, **kwargs):
        requests.post(ADDON_URL, json={"state": 1})
        self._state = True

    async def async_turn_off(self, **kwargs):
        requests.post(ADDON_URL, json={"state": 0})
        self._state = False
