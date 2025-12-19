def setup(hass, config):
    hass.helpers.discovery.load_platform("switch", "genie", {}, config)
    return True