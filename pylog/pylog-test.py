# coding: utf-8 

from pylog import Logger
from datetime import datetime as dtime

# global
LOG_NAME = "{0:}.log".format(dtime.now().strftime("%Y%m%d-%H%M%S"))

def main():
	log = Logger(name=__name__, fname=LOG_NAME)
	for i in range(10):
		if i % 2 == 0:
			log.info("output:{0:}".format(i))

	log = Logger(name="test", fname=LOG_NAME)
	for i in range(10):
		if i % 3 == 0:
			log.info("output:{0:}".format(i))

if __name__ == '__main__':
	main()