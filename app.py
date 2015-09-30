import os, time
import numpy as np


def run_loop():
    ''' 
    print some random shuffles

    '''

    length = os.getenv('TEST_LENGTH', 10)

    arr = np.arange(length)

    while True:
        np.random.shuffle(arr)
        print arr

        time.sleep(5)

if __name__ == "__main__":
    print "Minial app V2 for Poc Booting"
    run_loop()