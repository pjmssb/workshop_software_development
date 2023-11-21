import boto3
from datetime import datetime
from logger_port import LoggerPort
from botocore.exceptions import ClientError

class CloudWatchLoggerAdapter(LoggerPort):
    def __init__(self, log_group:str, stream_name:str) -> None:
        self.client = boto3.client('logs')
        self.log_group = log_group
        self.stream_name = stream_name
        self.sequence_token = None  # Initially, the sequence token is unknown

    def _get_sequence_token(self):
        # Retrieve the next sequence token for the log stream
        try:
            response = self.client.describe_log_streams(
                logGroupName=self.log_group,
                logStreamNamePrefix=self.stream_name,
                limit=1
            )
            streams = response.get('logStreams')
            if streams:
                return streams[0].get('uploadSequenceToken')
        except ClientError as error:
            print(f"Error retrieving sequence token: {error}")
            return None

    def log(self, tipo_de_evento: str, timestamp: datetime, info: str):
        if self.sequence_token is None:
            self.sequence_token = self._get_sequence_token()

        log_event = {
            'timestamp': int(timestamp.timestamp() * 1000),  # milliseconds
            'message': f"{timestamp} - {tipo_de_evento} - {info}"
        }

        try:
            kwargs = {
                'logGroupName': self.log_group,
                'logStreamName': self.stream_name,
                'logEvents': [log_event]
            }
            if self.sequence_token:
                kwargs['sequenceToken'] = self.sequence_token

            response = self.client.put_log_events(**kwargs)

            # Update the sequence token for the next put
            self.sequence_token = response['nextSequenceToken']

        except ClientError as error:
            print(f"Error putting log event: {error}")

            # Reset the sequence token if it's invalid
            if error.response['Error']['Code'] in ('InvalidSequenceTokenException', 'DataAlreadyAcceptedException'):
                self.sequence_token = self._get_sequence_token()
