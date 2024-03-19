import logging
import os
import shutil
import traceback

from requests import Response
from datetime import datetime


log_file_path = 'logs/csv_transition.log'

# Check if the log file exists
if os.path.exists(log_file_path):
    # Create a backup name for the existing log file
    backup_name = f"logs/csv_transition_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    # Rename the existing log file to create a backup
    shutil.move(log_file_path, backup_name)


class LoggerObject:
    log = logging.getLogger()

    @staticmethod
    def response(response: Response):
        LoggerObject.log.info(f"{response}: {response.text}")

    @staticmethod
    def test_error(error_text: str = ''):
        LoggerObject.log.error('!' * 93)
        LoggerObject.log.error(error_text[:1_000])

    @staticmethod
    def raised_error(e: Exception, error_message: str = ''):
        LoggerObject.log.error('!' * 93)
        LoggerObject.log.error((traceback.format_exc() + '\n' + error_message)[:1_000])
        LoggerObject.log.warning('<' * 93)

    @staticmethod
    def start_test(log_message: str = '') -> None:
        LoggerObject.log.warning('>' * 93)
        LoggerObject.log.warning(log_message)

    @staticmethod
    def finish_test(log_message: str = '') -> None:
        LoggerObject.log.warning(log_message)
        LoggerObject.log.warning('<' * 93)

    @staticmethod
    def class_name(self) -> None:
        LoggerObject.log.warning('*' * 93)
        LoggerObject.log.warning(f"{self.__class__.__name__}: {self.__class__.__doc__}")
        LoggerObject.log.warning('*' * 93)

    @staticmethod
    def log_success(response: Response):
        LoggerObject.log.info(f"{response} - {response.url}")
        LoggerObject.log.info(f"response: {response.text}")

    @staticmethod
    def log_error(response: Response, error_text=''):
        LoggerObject.log.warning('^' * 93)
        LoggerObject.log.info(f"{response} - {response.url}")
        LoggerObject.log.info(f"response: {response.text[:1000]}")
        LoggerObject.log.error(error_text[:1000])


logger = LoggerObject()
