rate = float(input("Enter the rate of exchange: "))

amoutns = [5, 50, 500, 5000]

def convert_to_npr(amount, rate):
    return amount * rate

for amount in amoutns:
    print(f"{amount}$ is equal to {convert_to_npr(amount, rate)} in NPR") 