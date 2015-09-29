import time
import numpy as np


def run_loop():
    ''' 
    print some random shuffles

    '''

    arr = np.arange(10)

    while True:
        np.random.shuffle(arr)
        print arr

        time.sleep(5)

if __name__ == "__main__":
    print "Minial app V2 for Poc Booting"
    run_loop()