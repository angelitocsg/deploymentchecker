import json
from abc import ABC, abstractmethod

from src.core.settings import Settings


class Result:
    code: str
    message: str

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    @staticmethod
    def empty():
        return Result("-1", "Undefined")

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=None)


class Checker(ABC):
    Name = "Checker"
    settings: Settings

    def set_settings(self, settings):
        self.settings = settings

    @abstractmethod
    def get_app(self) -> str:
        return "App not set"

    @abstractmethod
    def check(self, event) -> Result:
        return Result.empty()
