
# Railway Fare and Reservation Calculator

passengers = []
total_amount = 0

print("===== RAILWAY FARE CALCULATOR =====")

n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    travel_class = input(
        "Enter class (Sleeper/AC3/AC2): "
    ).lower()

    # Validate inputs
    if age < 0 or distance <= 0:
        print("Invalid passenger details!")
        continue

    # Calculate distance slab fare
    if distance <= 100:
        basic_fare = distance * 1.5

    elif distance <= 300:
        basic_fare = (100 * 1.5) + (distance - 100) * 1.2

    else:
        basic_fare = (100 * 1.5) + (200 * 1.2) + (distance - 300)

    # Apply class multiplier
    if travel_class == "sleeper":
        multiplier = 1

    elif travel_class == "ac3":
        multiplier = 2

    elif travel_class == "ac2":
        multiplier = 3

    else:
        print("Invalid travel class!")
        continue

    basic_fare = basic_fare * multiplier

    # Apply age concession
    if age < 5:
        concession = basic_fare
    elif age >= 60:
        concession = basic_fare * 0.40
    else:
        concession = 0

    fare_after_concession = basic_fare - concession

    # Reservation fee
    reservation_fee = 40

    final_fare = fare_after_concession + reservation_fee

    # Cancellation option
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = final_fare * 0.20
        refund = final_fare - penalty
        status = "Cancelled"
    else:
        penalty = 0
        refund = 0
        status = "Confirmed"

    # Store passenger details
    passenger = {
        "name": name,
        "fare": final_fare,
        "concession": concession,
        "fee": reservation_fee,
        "penalty": penalty,
        "refund": refund,
        "status": status
    }

    passengers.append(passenger)

    total_amount += final_fare

# Display passenger details
print("\n===== RAILWAY RESERVATION STATEMENT =====")

for p in passengers:

    print("\nPassenger Name:", p["name"])
    print("Basic Ticket Fare:", round(p["fare"] - p["fee"], 2))
    print("Concession:", round(p["concession"], 2))
    print("Reservation Fee:", p["fee"])
    print("Final Fare:", round(p["fare"], 2))
    print("Cancellation Penalty:", round(p["penalty"], 2))
    print("Refund Amount:", round(p["refund"], 2))
    print("Ticket Status:", p["status"])

print("\nTotal Ticket Amount: Rs.", round(total_amount, 2))
print("Railway Calculation Completed!")

