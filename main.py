#!/usr/bin/env python3

from parser import Parser
import threading

parser = Parser()

if __name__ == '__main__':
    thd = threading.Thread(target = parser.run)
    thd.start()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        parser.stop()
        
    
    
