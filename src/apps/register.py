from src.apps.ab1_offer_app import AB1OfferApp
from src.apps.ab1_simulation_app import AB1SimulationApp
from src.core.checker import Checker
from src.core.service_register import locator

locator.register(Checker.Name, AB1OfferApp)
locator.register(Checker.Name, AB1SimulationApp)
