#!/usr/bin/env python3
from parser import Parser
import threading
from logger import Logger

parser = Parser()

if __name__ == '__main__':
    thd = threading.Thread(target = parser.run)
    thd.start()
    Logger.log(Logger.INFO,"Bot Running ...")
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        parser.stop()