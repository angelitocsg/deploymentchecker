from service_locator import inject
from src.core.interfaces.checker import Checker
from src.core.register import locator
from typing import List


@inject
def main(
        logger=locator.resolve('Logger'),
        checkers: List[Checker] = locator.resolve("Checker")):
    print("main executed")

    for c in checkers:
        if c.get_app() == "Offer":
            print("offer found")

    logger.log("ola")


print("calling main")

main()
