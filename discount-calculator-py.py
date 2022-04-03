def priceCalculator():
    priceInput = float(input('What is the price of your item?: $'))
    discount = float(0.3 * priceInput)
    discount = round(discount, 3)
    priceOutput = priceInput - discount
    priceOutput = round(priceOutput, 3)
    print()
    print(f'The base price of your item is ${priceInput}\n')
    print(f'The 20% discounted price on your item is ${discount}\n')
    print(f'Your damage is ${priceOutput}')


priceCalculator()

