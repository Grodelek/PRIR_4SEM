import threading
import time


def function(i, k):
    print("start Thread %i\n" % i)
    time.sleep(k)
    print("end Thread %i\n" % i)
    return

#Watki gdzie Powloka czasowa 2s
t1 = threading.Thread(target=function, args=(1, 2))
t2 = threading.Thread(target=function, args=(2, 2))
#Watki gdzie powloka czasowa 3s
t3 = threading.Thread(target=function, args=(3, 3))
t4 = threading.Thread(target=function, args=(4, 3))
t5 = threading.Thread(target=function, args=(5, 3))
t1.start()
t2.start()
t1.join()
t2.join()
t3.start()
t4.start()
t5.start()
t3.join()
t4.join()
t5.join()

print("End program")
# Wniosek: Wykonanie wszystkich watkow zajmuje ok. 5 sekund,
# dzieki metodzie join() watki oczekuja na zakonczenie swojego wykonania

