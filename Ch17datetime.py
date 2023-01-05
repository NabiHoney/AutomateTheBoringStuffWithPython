import datetime #quick example
print('Employee Name: ')
input()

startTime = datetime.datetime.now()
print(startTime)


def totalTime():
    input()
    endTime = datetime.datetime.now()
    print(endTime)
    tot = (endTime - startTime)
    print('Total time worked: ', tot)
      
totalTime()
