from prompt_toolkit.shortcuts import ProgressBar
import time
import threading

with ProgressBar() as pb:
    def task_1():
        for i in pb(range(100)):
            time.sleep(.05)

    def task_2():
        for i in pb(range(150)):
            time.sleep(.08)

    t1 = threading.Thread(target=task_1)
    t2 = threading.Thread(target=task_2)
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()

    for t in [t1, t2]:
        while t.is_alive():
            t.join(timeout=.5)
