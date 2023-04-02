import logging
import logging.handlers
import os
import colorlog

class MyLogger():
    def __init__(self,name, **kwargs):
        # # checkin if folder is exists in the root of the app.Creates a new one if False
        self.message = "App initialization"
        if kwargs:
            if kwargs["message"]:
                self.message = kwargs["message"]
            else:
                self.message = "App initialization"
        log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logging')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Output log will be formatted to this formatter
        formatter = logging.Formatter('%(asctime)s || %(name)s || %(levelname)s || %(funcName)s || %(message)s',
                                      datefmt='%m-%d %H:%M')
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages, keeps only five last files
        fh = logging.handlers.RotatingFileHandler(f"{log_dir}"+"\\logger.log", maxBytes=1024 * 1024, backupCount=5)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # Disable the root logger to prevent console output

        # "App initialization you have to have five line of log messages if you want to have color coded lines in the log
        # (it appears only color coded lines can be seen while opening in pycharm
        for i in range(4):
            self.logger.info(self.message)

    # different types of log messages is applied is defined below
    def debug(self, value):
        self.logger.debug(msg=value)

    def info(self, value):
        self.logger.info(msg=value)

    def warning(self, value):
        self.logger.warning(msg=value)

    def error(self, value):
        self.logger.error(msg=value)

    def critical(self, value):
        self.logger.critical(msg=value)

    def exception(self, value):
        self.logger.exception(msg=value)


