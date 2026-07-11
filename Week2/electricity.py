units =[]
shops = []
number_of_shops = int(input("Enter the number of shops: "))
for i in range(number_of_shops):  
    shop = input(f"Enter the name of the shop {i+1}: ")
    unit= float(input(f"Enter the units consumed by {shop}: "))
    shops.append(shop)
    units.append(unit)

while len(units)>0:
    for u in range(len(units)):
        if(units[u]>=100):
            print(f"{shops[u]} : NRP 100 per unit")
            print(f"{shops[u]} : {units[u]*100}")
        elif(units[u]>=50):
            print(f"{shops[u]} : NRP 50 per unit")
            print(f"{shops[u]} : {units[u]*50}")
        else:
            print(f"{shops[u]} : NRP 35 per unit")
            print(f"{shops[u]} : {units[u]*35}")
    break