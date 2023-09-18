def printDetails( item, **kwargs):
    print('Item name is %s'%(item))
    for key, value in kwargs.items():
        print('- %s is %s' %(key, value))
    return

printDetails("Monitor", price = 70, Quantity = 85)