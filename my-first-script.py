import os


class myclass:
    ' Sample definition '
    count = 0
    myvar = 1

    def __init__(self, msg):
        myclass.count += 1
        self.message = msg

    def myfunc1(self):
        myvar = 100
        print("Message from {}: {}".format(__name__, self.message))
        print("Local variable: {}".format(myvar))
        print(os.getcwd())

    @classmethod
    def incrCount(self):
        print("Incrementing count...")


obj1 = myclass("HELLO!!!")
obj1.myfunc1()
print(myclass.myvar)

obj2 = myclass("HELLO AGAIN!!!")
obj2.myfunc1()
print(myclass.myvar)
