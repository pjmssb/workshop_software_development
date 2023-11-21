from abc import ABC, abstractmethod
from datetime import datetime

class LoggerPort(ABC):

    @abstractmethod
    def log(self, tipo_de_evento: str, timestamp: datetime, info: str):
        pass
