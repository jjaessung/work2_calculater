# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def subtract(x, y):
    return x-y

def times(x, y):
    return x*y

def divide(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: subtract, 3: times, 4: divide")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
        elif check == 2:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", subtract(x,y))
        elif check == 3:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", times(x,y))
        elif check == 4:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", divide(x,y))
        else:
            print("Thank you!")

if __name__ == "__main__":
    main()
