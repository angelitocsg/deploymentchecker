from abc import ABC, abstractmethod


class Checker(ABC):

    @abstractmethod
    def get_app(self) -> str:
        return "App not set"

    @abstractmethod
    def check(self):
        return True
