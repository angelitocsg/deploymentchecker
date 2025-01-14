from src.apps.ab1_offer_component_cheker import AB1OfferComponentChecker
from src.apps.ab1_simulation_component_cheker import AB1SimulationComponentChecker
from src.core.logger import Logger
from src.core.service_locator import ServiceLocator
import yaml

with open('src/config.yml', 'r') as f:
    config = yaml.safe_load(f)

prefix = config['logging']['prefix']
version = config['version']

locator = ServiceLocator()
locator.register("Checker", AB1OfferComponentChecker)
locator.register("Checker", AB1SimulationComponentChecker)
locator.register_instance("Logger", Logger, Logger(prefix, version))
