#Simple unit converter
def km_miles(km):
    return km*0.6217
def miles_km(miles):
    return miles/0.6217
def cel_fehr(cel):
    return (9*cel/5) + 32
def fehr_cel(fehr):
    return 5*(fehr -32)/9

print("1. convert km to miles")
print("2. convert miles to km ")
print("3. convert celsius to fehrenheit")
print("4. convert fehrenheit to celsius")
 
choose= int(input("ENTER FROM THE ABOVE NUMBER SEQUENCE TO PROCEED: "))

if choose == 1:
    km=float(input("ENTER NUMBER TO CONVERT IT INTO MILES"))
    print(f"{km} km = {km_miles(km)} miles")
elif choose == 2:
    miles=float(input("ENTER NUMBER TO CONVERT IT INTO KM"))
    print(f"{miles} miles = {miles_km(miles)} km")
elif choose == 3:
    cel=float(input("ENTER NUMBER TO CONVERT IT INTO FEHRENHEIT"))
    print(f"{cel} celsius = {cel_fehr(cel)} fehrenheit")
elif choose == 4:
    fehr=float(input("ENTER NUMBER TO CONVERT IT INTO CELSIUS"))
    print(f"{fehr} fehrenheit = {fehr_cel(fehr)} celsius")
else:
    print("INVALID OPTION!.")


    