import time

def displayWelcomeMessage():
    messages = [
        'Welcome to the Cornish drinks vending machine!',
        'This vending machine serves several drinks.',
        'Coins accepted: 1p, 2p, 5p, 10p, 20p, 50p, £1, £2'
    ]

    for message in messages:
        print('\n' + '*' * 49) # visual separation between lines
        print(message)
        print('*' * 49 + '\n')
        # time.sleep(1.3) # delays execution to allow reading time
    

def insertCoins():
    validCoins = {
        '1p': 1, '2p': 2, '5p': 5, '10p': 10,
        '20p': 20, '50p': 50, '£1': 100, '£2': 200
    }

    while True:
        coin = input('\nPlease insert coins: ')

        if coin in validCoins:
            return validCoins[coin] # returns int value of coin in pennies
        else: 
            print("Error. Please enter a valid coin to continue") # prevents erroneous inputs
            break

def formatMoney(amountInPennies):
    amountInPounds = amountInPennies / 100
    amountInPounds = round(amountInPounds, 2) # rounds to 2dp

    pennieString = str(amountInPennies) + 'p'
    poundString = '£' + str(amountInPounds)

    if amountInPennies < 100:
        return pennieString
    elif amountInPennies >= 100:
        return poundString

def transaction(fullyPaidOff, outstandingTotal):
    while not fullyPaidOff:
        print('Amount remaining:', formatMoney(outstandingTotal))
        insertedAmount = insertCoins()
        outstandingTotal -= insertedAmount

        if outstandingTotal == 0: # exact amount inserted, no change given
            fullyPaidOff = True
            print('No change due. Have a nice day!')
        elif outstandingTotal < 0: # customer has inserted more than required
            fullyPaidOff = True
            overpayment = (outstandingTotal * -1) # amount owed to customer in pennies
            print('Change due:', calculateChange(overpayment)) # amount owed in specific coins
        else: 
            continue # loops again if money still owed


def calculateChange(leftoverMoney):
    changeDue = [] # correct change will be returned from list

    while leftoverMoney != 0: # loops until correct change given
        if leftoverMoney >= 200:
            changeDue.append('£2') 
            leftoverMoney -= 200
        elif leftoverMoney >= 100:
            changeDue.append('£1')
            leftoverMoney -= 100
        elif leftoverMoney >= 50:
            changeDue.append('50p')
            leftoverMoney -= 50
        elif leftoverMoney >= 20:
            changeDue.append('20p')
            leftoverMoney -= 20
        elif leftoverMoney >= 10:
            changeDue.append('10p')
            leftoverMoney -= 10
        elif leftoverMoney >= 5:
            changeDue.append('5p')
            leftoverMoney -= 5
        elif leftoverMoney >= 2:
            changeDue.append('2p')
            leftoverMoney -= 2
        elif leftoverMoney >= 1: 
            changeDue.append('1p')
            leftoverMoney -= 1
        else:
            print('Error: Money not in correct format')

    return changeDue

def getDrinkSelection():
    print('\nDrinks available:')
    print('1A) KernowCoke: £1.25')
    print('1B) Diet KernowCoke: £1')
    print('1C) TruroTango: £1.50')
    print('2A) St Ives Sprite: £2')
    print('2B) Porthleven Pepsi: £1.75')

    while True:
        drinkCode = input('\nSelect drink code: ').upper() # upper allows inputs to be upper or lowercase

        drinkNames = {
            '1A': 'KernowCoke', '1B': 'Diet KernowCoke',
            '1C': 'TruroTango', '2A': 'St Ives Sprite',
            '2B': 'Porthleven Pepsi' 
        }

        if drinkCode in drinkNames:
            return drinkNames[drinkCode] # returns name of drink selected
        else:
            print('Error: Please choose one of the drinks on offer.')
            continue

def getDrinkPrice(drinkSelected):
    drinkPrices = {
        'KernowCoke': 125, 'Diet KernowCoke': 100,
        'TruroTango': 150, 'St Ives Sprite': 200,
        'Porthleven Pepsi': 175
    }

    return drinkPrices[drinkSelected] # returns the price in pennies

def main():
    displayWelcomeMessage()

    drinkSelected = getDrinkSelection()
    print('\nYou have selected:', drinkSelected, '\n') 
    priceOfDrink = getDrinkPrice(drinkSelected)

    outstandingTotal = priceOfDrink
    fullyPaidOff = False

    transaction(fullyPaidOff, outstandingTotal)

main()