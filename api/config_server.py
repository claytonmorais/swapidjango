from spring_config import ClientConfigurationBuilder
from spring_config.client import SpringConfigClient
from setup.settings import CONFIG_SERVER_URL
from setup.settings import NODE_PROFILES_ACTIVE

def get_url():


    config = (
        ClientConfigurationBuilder()
        .app_name('swapidjango')
        .address(CONFIG_SERVER_URL)
        .profile(NODE_PROFILES_ACTIVE)
        .authentication(("develop", "develop"))
        .build()
    )
    config_server = SpringConfigClient(config)
    return config_server.get_attribute('backend.swapi.endpoint')

