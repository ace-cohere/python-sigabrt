import os
import signal
import time

def exit_gracefully(signum, frame):
    print("Exiting gracefully")
    exit(0)

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)

def main():
    try:
        while(True):
            time.sleep(1)
    except Exception as e:
        print("Error handled by Python")
        print('Exception:', e)

if __name__ == "__main__":
    main()
