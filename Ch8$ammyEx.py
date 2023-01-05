"""Makin' Sammiches Pylint improved."""
import pyinputplus as pyip
custch = []
def order():
    """Order inputs."""
    bread = pyip.inputMenu(['Rye', 'Sourdough', 'Herb'], numbered=True)
    custch.append(bread)
    protein = pyip.inputMenu(['Beef', 'Egg', 'Lamb', 'Tofu', 'Chickpea'], numbered=True)
    custch.append(protein)
    chezya = pyip.inputYesNo(prompt="Cheese? Enter 'y' for yes, 'n' for no: ")
    for i in chezya:
        if i == 'y':
            chezkind = pyip.inputMenu(['Mercan', 'Stinky', 'Tasteless'], numbered=True)
            custch.append(chezkind)
    mayoya = pyip.inputYesNo("Mayo - y/n: ")
    for i in mayoya:
        if i == 'y':
            custch.append('mayo')
    goya = pyip.inputYesNo("Gochujang - y/n: ")
    for i in goya:
        if i == 'y':
            custch.append('gochujang')
    letya = pyip.inputYesNo("Lettuce - y/n: ")
    for i in letya:
        if i == 'y':
            custch.append('lettuce')
    materya=pyip.inputYesNo("Tomato - y/n: ")
    for i in materya:
        if i == 'y':
            custch.append('tomato')
order()
how_many_sammy = pyip.inputInt('Enter number of Sammies: ', min=1)
R = len(custch)
T = int(R) * int(how_many_sammy)
print(custch)
print(R)
print('$' + format(T, ',.2f'))
