### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture shutil module -- 1:27:35

# shutil module is used for high-level operations, such as copy, remove, archive files. 
#   MANAGING THREADS: 
# 1. Threads are streams that can be scheduled by the OS and executed across a single core
# processor concurrently, or in parallel across multiple cores in the procesor 
# 2. threading module: constructs higher-level threading intefaces on top of the lower level thread module

# threading module contains Thread() class that we nee to extend to create our own execution thread
# Thread class constructor accepts 5 types of arguments 
    # group: a special parameter that is reserved for future extensions 
    # target: callable object to be involved in run()
    # name: thread's name 
    # args: an argument tuple for target invocation 
    # kwargs: dictionary of keyword argument to invoke the base class constructor 
    
# run() : execute the threads 
# thread.join() : used to wait for the thread to finish. it blocks the thread until the thread finishes its execution 

# two types of threads
    # kernel-level threads: low-lvl threads. users do not interact with this. 
    # user-level threads: high-lvl threads. users can interact. 
    
# in python shell, use help(thread.Thread) command 

# exp 12: create 4 threads using threading module 

import threading
import time 

num_threads = 4 

def thread_message(message):
    global num_threads
    num_threads -= 1 
    print("message from thread %s\n" %message)
    
while num_threads > 0: 
    print ("i am the %s thread" %num_threads)
    threading.Thread(target = thread_message("i am the %s thread" %num_threads)).start()
    time.sleep(0.1)
    
    