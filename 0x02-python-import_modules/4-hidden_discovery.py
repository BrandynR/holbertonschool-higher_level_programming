#!/usr/bin/python3
def main():
    import hidden_4
    for i in dir(hidden_4):
        if ("__" not in i):
            print(i)

if (__name__ == "__main__"):
    main()
