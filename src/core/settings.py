import json


class Settings:
    Name = "Settings"

    def __init__(self, in_dict: dict):
        self.apps = None
        self.environment = None
        self.version = None
        assert isinstance(in_dict, dict)
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
                setattr(self, key, [Settings(x) if isinstance(x, dict) else x for x in val])
            else:
                setattr(self, key, Settings(val) if isinstance(val, dict) else val)

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=None)