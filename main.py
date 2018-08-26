#!/usr/bin/env python3
import threading

from logger import Logger
from parser import Parser


if __name__ == '__main__':
    parser = Parser()
    thd = threading.Thread(target = parser.run)
    thd.start()
    Logger.log(Logger.INFO,"Bot Running ...")
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        parser.stop()