import pyinputplus as pyip

custch = []
 
def order():
    bread = pyip.inputMenu(['Rye', 'Sourdough', 'Herb'], numbered=True)
    custch.append(bread)
    protein = pyip.inputMenu(['Beef', 'Egg', 'Lamb', 'Tofu', 'Chickpea'], numbered=True)
    custch.append(protein)
    chezYa = pyip.inputYesNo(prompt="Cheese? Enter 'y' for yes, 'n' for no: ")
    for i in chezYa:
        if i == 'y':
            chezKind = pyip.inputMenu(['Mercan', 'Stinky', 'Tasteless'], numbered=True)
            custch.append(chezKind)  
        else:
            next
    mayoYa = pyip.inputYesNo("Mayo - y/n: ")
    for i in mayoYa:
        if i == 'y':
            custch.append('mayo')
        else:
            next 
    goYa = pyip.inputYesNo("Gochujang - y/n: ")
    for i in goYa:
        if i == 'y':
            custch.append('gochujang')
        else:
            next 
    letYa = pyip.inputYesNo("Lettuce - y/n: ")
    for i in letYa:
        if i == 'y':
            custch.append('lettuce')
        else:
            next 
    materYa=pyip.inputYesNo("Tomato - y/n: ")
    for i in materYa:
        if i == 'y':
            custch.append('tomato')
        else:
            next 

order()
howManySammy = pyip.inputInt('Enter number of Sammies: ', min=1)

rtot = len(custch)
total = int(rtot) * int(howManySammy) 

print(custch)
print(rtot)
print('$' + format(total, ',.2f'))
