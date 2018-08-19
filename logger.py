import time

class Logger:
    READ = 0
    SEND = 1
    ERROR = 2
    INFO = 3
    
    color_code = {
        "clear": "\033[1;m",
        "red":   "\033[1;31m",
        "green": "\033[1;32m",
        "blue":  "\033[1;34m"
    }

    @classmethod
    def log(cls,tp,msg,*args):
        msg = msg % args
        prep = "info"
        if tp == cls.READ:
            prep = cls.color_code["blue"] + "read" + cls.color_code["clear"]
        elif tp == cls.SEND:
            prep = cls.color_code["green"] + "send" + cls.color_code["clear"]
        elif tp == cls.ERROR:
            prep = cls.color_code["red"] + "error" + cls.color_code["clear"]
        
        print(time.ctime() + " [" + prep + "] " + msg)