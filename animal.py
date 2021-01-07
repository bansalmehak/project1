import sys

def cat():
    print('Meow')

def default():
    print('Hello')
def dog():
    print('BOWBOW')
def main():
    if sys.argv[1] == 'cat':
        cat()
    else if sys.argv[1] == 'dog':
        dog()
    else:
        default()
if __name__ == '__main__':
    main()
