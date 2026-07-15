def recharge_cost(gb):
    rate = 0
    if gb <=1:
        rate = 30
    elif gb <= 2:
        rate = 50
    elif gb <= 5:
        rate = 100      
    else:
        return "Invalid data usage"
    
    return rate

gb = float(input("Enter the data usage in GB (1,2,5): "))
print(f"The recharge cost for {gb} GB is: {recharge_cost(gb)}")