from src.core.interfaces.checker import Checker


class AB1SimulationComponentChecker(Checker):
    def get_app(self) -> str:
        return "Simulation"

    def check(self):
        pass
