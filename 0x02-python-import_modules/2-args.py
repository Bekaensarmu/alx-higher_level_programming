#!/usr/bin/python3
import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(":")
    else:
        if num_args == 1:
            print("Number of argument(s): 1, argument:")
        else:
            print("Number of argument(s): {}, arguments:".format(num_args))
        
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    print_arguments()
