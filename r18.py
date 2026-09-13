inventory = {
    "pen": 20,
    "book": 15,
    "bag": 5,
    "pencil": 30,
    "eraser": 12
}
n = input("enter the product :")
c = int(input("enter the quantity :"))
if n in inventory:
    if inventory.get(n) > c:
        print("purchase complated")
        b = inventory[n]-c
        inventory.__setitem__(n,b)
        print(inventory)
    elif inventory[n] < c:
        print("not enough stock ")
if n not in inventory:
    print("product not found")