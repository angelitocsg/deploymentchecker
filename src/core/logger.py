import datetime


class Logger:
    def __init__(self, prefix, version):
        print("returning new instance for LogEntry")
        self.timestamp = datetime.datetime.now()
        self.prefix = prefix
        self.version = version

    def log(self, message):
        # Simulate logging by printing to console
        print(
            {
                "timestamp": f"{self.timestamp}",
                "version": self.version,
                "type": "INFO",
                "env": self.prefix,
                "message": message,
            }
        )
