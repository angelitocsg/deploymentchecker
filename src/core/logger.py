import datetime
from enum import Enum


class LogLevel(Enum):
    Debug = 1
    Info = 2
    Warning = 3
    Error = 4


class Logger:
    Name = "Logger"

    def __init__(self, environment="none", version=0.0, log_level: LogLevel = LogLevel.Debug):
        self.environment = environment
        self.version = version
        self.log_level = log_level

    def __log(self, log_type: str, message: str):
        timestamp = datetime.datetime.now()
        print(
            {
                "timestamp": f"{timestamp}",
                "version": self.version,
                "type": log_type,
                "env": self.environment,
                "message": message,
            }
        )

    def debug(self, message: str):
        if self.log_level.value <= LogLevel.Debug.value:
            self.__log("DEBUG", message)

    def info(self, message: str):
        if self.log_level.value <=  LogLevel.Info.value:
            self.__log("INFO", message)

    def warn(self, message):
        if self.log_level.value <= LogLevel.Warning.value:
            self.__log("WARN", message)

    def error(self, message):
        if self.log_level.value <= LogLevel.Error.value:
            self.__log("ERROR", message)
