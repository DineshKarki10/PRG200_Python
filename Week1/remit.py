# take input earning
earn_in_usd = float(input("Enter earned amount in USD: "))
# convert to nepali
earn_in_nrp= earn_in_usd*150
# input service charge
service_charge = float(input("Entert the service rate: "))
# Output actual earning
print((f"Actual earning in NRP: {earn_in_nrp}"))
# calculate reduced amt
reduce_amt= (service_charge/100)*earn_in_nrp
# final outputs
print((f"Deduction : {reduce_amt}"))
print((f"You will recevive: {earn_in_nrp-reduce_amt}"))

# yearly
nrp = earn_in_nrp*12
reduce = reduce_amt*12
# Output
print((f"Total one year deduction : {reduce}"))
print((f"Total One year receiving amount : {nrp - reduce}"))