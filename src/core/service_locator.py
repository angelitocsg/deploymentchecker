from src.core.logger import Logger, LogLevel


class ServiceLocator:
    def __init__(self, logger: Logger):
        self.service_map = {}
        self.service_instances = {}
        self.logger = logger

    def register(self, abstraction: str, implementation):
        self.logger.debug(f"[DI] Register abstraction: {abstraction} for implementation: {implementation.__name__}")
        if abstraction in self.service_map:
            current = self.service_map[abstraction]
            current.append(implementation)
            self.service_map[abstraction] = current
        else:
            self.service_map[abstraction] = [implementation]

    def register_instance(self, abstraction: str, implementation, instance):
        self.logger.debug(
            f"[DI] Register instance for abstraction: {abstraction} and implementation: {implementation.__name__}")
        if abstraction not in self.service_map:
            self.service_map[abstraction] = [implementation]
        if abstraction in self.service_instances:
            current = self.service_instances[abstraction]
            current.append(instance)
            self.service_instances[abstraction] = current
        else:
            self.service_instances[abstraction] = [instance]

    def resolve(self, abstraction: str):
        self.logger.debug(
            f"[DI] Resolving instance for abstraction: {abstraction}")
        if abstraction not in self.service_map:
            raise Exception(f"[DI] No service for this abstraction {abstraction} has been registered.")
        if abstraction not in self.service_instances:
            implementation_list = self.service_map[abstraction]
            for implementation in implementation_list:
                self.register_instance(abstraction, implementation, implementation())
        if len(self.service_instances[abstraction]) == 1:
            return self.service_instances[abstraction][0]
        return self.service_instances[abstraction]
