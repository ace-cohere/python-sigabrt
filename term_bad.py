import os
import time

def main():
    try:
        while(True):
            time.sleep(1)
    except Exception as e:
        print("Error handled by Python")
        print('Exception:', e)

if __name__ == "__main__":
    main()
