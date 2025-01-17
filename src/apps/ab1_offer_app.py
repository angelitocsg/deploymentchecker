import json

from src.core.checker import Checker, Result


class AB1OfferApp(Checker):
    def get_app(self) -> str:
        return self.settings.apps.ab1_offer_app.name

    def check(self, event):
        return Result("200", "Ok")
