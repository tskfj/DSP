import rcp
import stk


def main():
    input_order()
    process()
    output()

def input_order():
    print('calculate raw materials for ...')
    print('1.solar panel or 2.carrier rocket')

    item = input('select product (input 1 or 2): ')
    if item == '1':
        item = 'solar_sail'
    elif item == '2':
        item = 'small_carrier_rocket'
    else:
        print('input 1 or 2!')
        return

    quantity = input('input quantity (1-1,000,000): ')
    quantity = int(quantity)
    OrderSheet.order_sheet.append((item, quantity))

class OrderSheet:
    order_sheet = []

def process():
    while True:
        if not OrderSheet.order_sheet:
            break
        manufacture()
        stock_keep()
        procure()

def manufacture():
    order = OrderSheet.order_sheet.pop(0)
    item, quantity = order
    recipe = rcp.recipes.get(item)
    X, A, B, C, _, XX, AA, BB, CC, _ = recipe

    # run_factory
    P = 1800 / max(XX, AA, BB, CC)
    out = XX * P
    in1 = AA * P
    in2 = BB * P
    in3 = CC * P

    Fout = out * (quantity / out)
    Fin1 = in1 * (quantity / out) * -1
    Fin2 = in2 * (quantity / out) * -1
    Fin3 = in3 * (quantity / out) * -1

    # ship
    Container.container = [
        (X, Fout),
        (A, Fin1),
        (B, Fin2),
        (C, Fin3)]

class Container:
    container = []

def stock_keep():
    for X in Container.container:
        item, quantity = X
        stk.stock[item] = stk.stock[item] + quantity
    Container.container.clear()

def procure():
    for item in stk.stock:
        quantity = stk.stock[item]
        if quantity < 0:
            OrderSheet.order_sheet.append((item, quantity *-1))
            stk.stock[item] = 0
        else:
            pass

def output():
    print('raw materials:')
    items = []
    for X in rcp.recipes:
        Y = rcp.recipes[X]
        type = Y[4]
        if type == 'raw material':
            items.append(X)
    for item in stk.stock:
        if item in items:
            if stk.stock[item] > 0:
                print(item, ': ', stk.stock[item])

if __name__ == '__main__':
    main()
