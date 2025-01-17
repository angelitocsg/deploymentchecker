import json
from typing import List

from src.apps.register import locator
from src.core.checker import Checker, Result

from src.core.logger import Logger
from src.core.settings import Settings


def main(application: str, event,
         settings=locator.resolve(Settings.Name),
         logger=locator.resolve(Logger.Name),
         checkers: List[Checker] = locator.resolve(Checker.Name)) -> Result:
    logger.info("[Checker] > started")

    for c in checkers:
        c.set_settings(settings)
        if c.get_app() == application:
            logger.info(f"[Checker] {application} found")
            result = c.check(event)
            logger.info("[Checker] < finished")
            return result

    logger.warn(f"[Checker] '{application}' not found")
    logger.info("[Checker] < finished")
    return Result("404", f"'{application}' not found")


print(main("ab1-offer-app", {}).to_json())
print(main("ab1-simulation-app", {}).to_json())
print(main("other", {}).to_json())
