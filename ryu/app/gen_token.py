from threading import Timer
import time
#max_token = 1000
#token_num = 0
class token:
    #max_token = 1000
    #token_num = 0
    def __init__(self,interval):
        self.max_token = 1000
        self.token_num = self.max_token
        self.execute_gen(interval,self.token_gen)
    def token_gen(self):
        if self.token_num < self.max_token:
            self.token_num += 1
    def token_getnum(self):
        return self.token_num
    def token_consume(self,token_num):
        if self.token_num >= token_num:
            self.token_num -= token_num
    def execute_gen(self,interval,callback):
        def f():
            callback()
            t = Timer(interval,f)
            t.start()
        def stop():
            t.cancel()
        t = Timer(interval,f)
        t.start()
        return stop
    #execute_gen(2,token_gen)
        
