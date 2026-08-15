#Q11 — Inventory System
#Create an inventory containing products and quantities.
#The user should be able to:
#Add a product
#Search for a product
#Remove a product
#Display all products
#Display the total number of products
#Keep the program running until the user chooses to stop.

inv = {'beef':10, 'chicken':15, 'mutton':8, 'fish':20, 'pork':12}

while True:
    print("1. Add product")
    print("2. Increase quantity")
    print("3. Search product")
    print("4. Remove product")
    print("5. Display all products")
    print("6. Display total number of products")
    print("7. Exit")

    n = int(input("Enter choice: "))

    if n == 1:
        p = input("enter product :")
        n = int(input("enter the quantity :"))
        inv[p] = n

    elif n == 2:
        l = input("enter the product :")
        k = int(input("enter the value for increase :"))

        if l in inv:
            inv[l] = inv[l] + k
        else:
            print("Product not found")

    elif n == 3:
        s = input("enter the product for search :")

        if s in inv:
            print("product found")
        else:
            print("product not found")

    elif n == 4:
        r = input("enter the product for removing :")

        if r in inv:
            inv.pop(r)
        else:
            print("Product not found")

    elif n == 5:
        for i in inv:
            print(i, inv[i])

    elif n == 6:
        y = len(inv)
        print("total number of product is :", y)

    elif n == 7:
        break