from functools import wraps


class ServiceLocator:
    def __init__(self):
        self.service_map = {}
        self.service_instances = {}

    def register(self, abstraction: str, implementation):
        if abstraction in self.service_map:
            current = self.service_map[abstraction]
            current.append(implementation)
            self.service_map[abstraction] = current
        else:
            self.service_map[abstraction] = [implementation]

    def register_instance(self, abstraction: str, implementation, instance):
        if abstraction not in self.service_map:
            self.service_map[abstraction] = [implementation]

        if abstraction in self.service_instances:
            current = self.service_instances[abstraction]
            current.append(instance)
            self.service_instances[abstraction] = current
        else:
            self.service_instances[abstraction] = [instance]

    def resolve(self, abstraction: str):
        if abstraction not in self.service_map:
            raise Exception(f"No service of this abstraction has been registered. {abstraction}")

        if abstraction not in self.service_instances:
            implementation_list = self.service_map[abstraction]
            for implementation in implementation_list:
                print(">> new instance", abstraction)
                self.register_instance(abstraction, implementation, implementation())

        if len(self.service_instances[abstraction]) == 1:
            return self.service_instances[abstraction][0]

        return self.service_instances[abstraction]

def injector(*injectors):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decorator


def inject(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped

