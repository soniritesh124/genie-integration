from homeassistant.helpers.discovery import load_platform

def setup(hass, config):
    load_platform(hass, "switch", "genie", {}, config)
    return True
