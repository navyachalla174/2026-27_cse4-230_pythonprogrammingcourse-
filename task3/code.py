
# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")

age = int(input("Enter patient age: "))

category = input("Enter patient category (Student/Other): ").lower()

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing charges
if (consultation < 0 or diagnostic < 0 or treatment < 0):
    print("Invalid charges! Charges cannot be negative.")

else:

    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply conditional concession
    if age >= 60:
        concession = total_bill * 0.10

    elif category == "student":
        concession = total_bill * 0.05

    else:
        concession = 0

    final_bill = total_bill - concession

    print("\nTotal Bill:", round(total_bill, 2))
    print("Concession:", round(concession, 2))
    print("Final Bill:", round(final_bill, 2))

    # Payment details
    paid = float(input("Enter amount paid: "))

    # Validate payment
    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:

        balance = final_bill - paid

        # Patient classification
        if paid == final_bill:
            status = "Fully Paid"

        elif paid > 0:
            status = "Partial Payment"

        else:
            status = "Pending Payment"

        # Display final details
        print("\n===== PATIENT BILL DETAILS =====")
        print("Patient Name:", name)
        print("Patient Age:", age)
        print("Total Bill:", round(total_bill, 2))
        print("Concession:", round(concession, 2))
        print("Final Bill:", round(final_bill, 2))
        print("Amount Paid:", round(paid, 2))
        print("Remaining Balance:", round(balance, 2))
        print("Payment Status:", status)

        print("\nBilling Completed!")

