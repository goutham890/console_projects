#Q14 — Shopping Cart Analyzer
#Ask the user for N products.
#For each product, store:
#Product name
#Price
#Quantity
#Finally display:
#Complete cart
#Total cost
#Most expensive product
#Cheapest product
#Total number of items
#Products costing more than ₹500

n = int(input("enter the number :"))

i = 0
total = 0
cheap = 1000
exp = 0

cart = {}

while(i < n):

    name = input("enter product name :")
    price = int(input("enter the price of the product :"))
    quant = int(input("enter the quantity of the product :"))

    cart[name] = {
        price: quant
    }

    total = total + (price * quant)

    if price > exp:
        exp = price
        m = name

    if price < cheap:
        cheap = price
        c = name

    i = i + 1


for name in cart:

    for price in cart[name]:

        quant = cart[name][price]

        print(f"product : {name}")
        print(f"price : {price}")
        print(f"quantity : {quant}")
        print("-" * 35)


print("total cost :", total)
print("expensive product :", m)
print("cheap product :", c)


for name in cart:

    for price in cart[name]:

        if price >= 500:
            print("product greater than 500 :", name)