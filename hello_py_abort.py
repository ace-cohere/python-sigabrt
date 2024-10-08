import os

def main():
    try:
        os.abort()
    except Exception as e:
        print("SIGABRT handled by Python")
        print('Exception:', e)


if __name__ == "__main__":
    main()
