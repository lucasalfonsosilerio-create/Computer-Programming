item = ["breakfast burrito", "cheeseburger", "hot dog", "teriyaki", "chips", "fries", "soda", "water"]
price = [4.50, 4.00, 3.00, 5.00, 1.00, 2.50, 1.75, 1.50]
taxable = [False, False, False, False, True, True, True, True]
card_balance = int(100)
total_price = int(0)

order = []
order_price = []
quantity = []

while True:
    new_item = input("What item would you like to order?")

    if new_item.strip().lower().startswith("n"):
        break

    if new_item.strip().lower() in item:
        itemAdded = item[item.index(new_item.strip().lower())]
        itemAddedPrice = int(price[item.index(new_item.strip().lower())])
        isItTaxable = taxable[item.index(new_item.strip().lower())]

        quantity_of_item = input("How many?")
        quantity.append(int(quantity_of_item.strip()))
        # print(quantity)

        if isItTaxable == True:
            order_price.append(itemAddedPrice*1.1)
        else:
            order_price.append(itemAddedPrice)

        order.append(itemAdded.strip().lower())

        # print(itemAdded)
    else:
        print("Invalid item")

    for y in order_price:
        # print(y,total_price, quantity[order_price.index(y)])
        total_price = total_price + (y*quantity[order_price.index(y)])
    
    # print(order, order_price, quantity)
    # print(total_price)

print("ITEM QUANTITY BASE AMOUNT TOTAL AMOUNT")
for x in range(0, len(order)):
    print(order[x], quantity[x], order_price[x], total_price)

payment_method = input("Will you be using cash or Cub Cash?")

if payment_method.strip().lower().startswith("cash"):
    payment = int(input("How much cash do you have?"))
    print(f"You have {payment-total_price} currently.")
elif payment_method.strip().lower().startswith("cub"):
    print(f"You have {card_balance-total_price} currently.")
print("Thank you.")