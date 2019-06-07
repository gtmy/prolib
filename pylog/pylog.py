# coding: utf-8 

from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG, INFO

class Logger:
	def __init__(self, name=__name__, level=INFO, fname="log.log"):
		self.logger = getLogger(name)
		self.logger.setLevel(level)
		formatter = Formatter("[%(asctime)s][%(levelname)s] [%(name)s] %(message)s")
        # formatter = Formatter("[%(asctime)s] [%(process)d] [%(pathname)s] [%(levelname)s] %(message)s")

		# stdout
		handler = StreamHandler()
		handler.setLevel(level)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

		# file
		handler = handlers.RotatingFileHandler(filename=fname, mode="a")
		handler.setLevel(level)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

	def debug(self, msg):
		self.logger.debug(msg)

	def info(self, msg):
		self.logger.info(msg)

	def warn(self, msg):
		self.logger.warning(msg)

	def error(self, msg):
		self.logger.error(msg)

	def critical(self, msg):
		self.logger.critical(msg)
