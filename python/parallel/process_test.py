import psutil
import time
import multiprocessing

def hello():
    # time.sleep(20)
    print(psutil.Process().cpu_num())

pool = multiprocessing.Pool()
jobs = []
for j in range(10):
    p = multiprocessing.Process(target = hello)
    jobs.append(p)
    p.start()