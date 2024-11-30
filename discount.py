price = int(input('Enter price of Item: '))
discount_input = input('Enter the discount: ')

if '%' in discount_input:
    discount_percent = int(discount_input.replace('%', '').strip())
else:
    discount_percent = int(discount_input)


def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        final_price = price
    else:
        final_price = price * (100 - discount_percent)/100

    print('Final price is: ', final_price)


calculate_discount(price, discount_percent)
