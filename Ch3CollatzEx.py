num = int(input()) 

def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = num // 2 
        elif num % 2 == 1:
            num = num * 3 + 1           
    print(num)        

collatz(num)
