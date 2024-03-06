import threading
import time

event1 = threading.Event()
event2 = threading.Event()

def function(i, event):
    print("start Thread %i\n" % i)
    event.wait()
    print("end Thread %i\n" % i)
    return


t1 = threading.Thread(target=function, args=(1, event1))
t2 = threading.Thread(target=function, args=(2, event1))

t3 = threading.Thread(target=function, args=(3, event2))
t4 = threading.Thread(target=function, args=(4, event2))
t5 = threading.Thread(target=function, args=(5, event2))
t1.start()
t2.start()
event1.set() #sygnalizacja eventu
t1.join()
t2.join()

t3.start()
t4.start()
t5.start()

event2.set()
t3.join()
t4.join()
t5.join()


print("End program")
# wątek może zareagować zarówno na jakies wydarzenie , jak i na upływ czasu.
