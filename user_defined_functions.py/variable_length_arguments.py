def printDetails( item, *components):
    print('Componenets of %s are'%(item))
    for component in components:
        print("-",component)
    return

printDetails('Computer', 'CPU', 'Monitor', 'Motherboard', 'Mouse')