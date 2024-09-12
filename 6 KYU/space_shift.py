def get_order(order):
    order = order.lower()
    menu = ['Burger','Fries','Chicken','Pizza','Sandwich','Onionrings','Milkshake','Coke']
    new_order = ''
    while order != '':
        for i in menu:
            while i.lower() in order:
                new_order += ' ' + i
                order = order.replace(i.lower(),'',1)
    return new_order[1:]

print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"))