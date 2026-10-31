
# Progressive Electricity Billing System

bills = []
units_list = []

n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units: "))

    # Calculate progressive slab charges
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50

    surcharge = energy_charge * 0.05

    # Calculate rebate
    if units < 100:
        rebate = energy_charge * 0.02
    else:
        rebate = 0

    total_bill = energy_charge + fixed_charge + surcharge - rebate

    units_list.append(units)
    bills.append(total_bill)

# Display monthly bills
print("\n===== ELECTRICITY BILL DETAILS =====")

for i in range(n):
    print("Month", i + 1)
    print("Units Consumed:", units_list[i])
    print("Total Bill: Rs.", round(bills[i], 2))

# Compare monthly bills
print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(1, n):

    increase = bills[i] - bills[i - 1]

    percentage = (increase / bills[i - 1]) * 100

    print("\nMonth", i + 1)

    if percentage > 30:
        print("Unusual Increase Detected!")
        print("Increase Percentage:", round(percentage, 2), "%")

    else:
        print("Normal Bill Change")
        print("Change Percentage:", round(percentage, 2), "%")

print("\nBilling Calculation Completed!")

