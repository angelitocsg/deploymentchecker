import json
import os

import yaml

from src.core.logger import Logger, LogLevel
from src.core.service_locator import ServiceLocator
from src.core.settings import Settings

environment = os.environ.get("ENV")
log_level: str = os.environ.get("LOG_LEVEL", "Debug")

if environment is None:
    with open(f'src/settings.yml', 'r') as f:
        settings = Settings(yaml.safe_load(f))
else:
    with open(f'src/settings-{environment}.yml', 'r') as f:
        settings = Settings(yaml.safe_load(f))

environment = settings.environment
version = settings.version

logger = Logger(environment, version, LogLevel[log_level])

locator = ServiceLocator(logger)
locator.register_instance(Settings.Name, Settings, settings)
locator.register_instance(Logger.Name, Logger, logger)
