import math
import tabulate

def GetInput():
    global raw_input
    global raw_cents
    raw_input = input("Enter the ammount:")
    try:
        if raw_input.find(",")!=-1:                  #input contains ","
            raw_cents=int(raw_input.replace(",",""))  #remove ","
        elif raw_input.find(".")!=-1:                #input contains "."
            raw_cents=int(raw_input.replace(".",""))  #remove "."
        else:                                       #input is in Euro only format(5=500cents)
            raw_cents=int(raw_input)*100              #add "00" to the end
    except:
        print("Invalid input")                      #if input is invalid print error and reask for input
        GetInput()

GetInput()

#[Value, Remaing ammount/value, rest of ammount/value]
headers = ["Value", "Quantity", "Missing"]
five_hundred = ["500€", math.trunc(raw_cents/50000), raw_cents%50000]
two_hundred = ["200€", math.trunc(five_hundred[2]/20000), five_hundred[2]%20000]
one_hundred = ["100€", math.trunc(two_hundred[2]/10000), two_hundred[2]%10000]
fifty = ["50€", math.trunc(one_hundred[2]/5000), one_hundred[2]%5000]
twenty = ["20€", math.trunc(fifty[2]/2000), fifty[2]%2000]
ten = ["10€", math.trunc(twenty[2]/1000), twenty[2]%1000]
five = ["5€", math.trunc(ten[2]/500), ten[2]%500]
two = ["2€", math.trunc(five[2]/200), five[2]%200]
one = ["1€", math.trunc(two[2]/100), two[2]%100]
fifty_cents = ["50c", math.trunc(one[2]/50), one[2]%50]
twenty_cents = ["20c", math.trunc(fifty_cents[2]/20), fifty_cents[2]%20]
ten_cents = ["10c", math.trunc(twenty_cents[2]/10), twenty_cents[2]%10]
five_cents = ["5c", math.trunc(ten_cents[2]/5), ten_cents[2]%5]
two_cents = ["2c", math.trunc(five_cents[2]/2), five_cents[2]%2]
one_cents = ["1c", math.trunc(two_cents[2]/1), two_cents[2]%1]


table = [headers, five_hundred, two_hundred, one_hundred, fifty, twenty, ten, five, two, one, fifty_cents, twenty_cents, ten_cents, five_cents, two_cents, one_cents] #,remainder]

print(tabulate.tabulate(table, tablefmt='fancy_grid', headers='firstrow'))
print(f"\n{raw_input}€ is equal to {raw_cents} cents")
