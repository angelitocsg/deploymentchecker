from src.core.interfaces.checker import Checker


class AB1OfferComponentChecker(Checker):
    def get_app(self) -> str:
        return "Offer"

    def check(self):
        pass
