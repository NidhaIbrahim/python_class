def printDetails( item, price = 100 ):
    print('%s costs %d'%(item, price))
    return

printDetails(item = 'Keyboard')
printDetails('Mouse')
printDetails(price = 50, item = 'Keyboard')