from src.core.checker import Checker, Result


class AB1SimulationApp(Checker):
    def get_app(self) -> str:
        return self.settings.apps.ab1_simulation_app.name

    def check(self, event):
        return Result("500", "Failed")
