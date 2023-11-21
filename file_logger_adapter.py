import os
from datetime import datetime
from logger_port import LoggerPort

class FileLoggerAdapter(LoggerPort):

    def __init__(self, log_name: str) -> None:
        self.log_name = log_name

    def log_event(self, tipo_de_evento: str, timestamp: datetime, info: str):
        date_str = timestamp.strftime("%Y-%m-%d")
        filename = f"{self.log_name}-{date_str}.log"
        with open(filename, 'a') as log_file:
            log_file.write(f"{timestamp} - {tipo_de_evento} - {info}\n")
