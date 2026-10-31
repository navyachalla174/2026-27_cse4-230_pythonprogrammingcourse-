
import math

# Input details
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Fixed and variable costs
fixed_cost = venue + equipment

variable_cost = catering + transport + certificate

# Total event cost
total_cost = fixed_cost + (variable_cost * participants)

# Participant contributions
participant_contribution = registration_fee * participants

# Sponsorship shortfall
sponsorship_shortfall = max(total_cost - sponsorship, 0)

# Total available funds
total_funds = participant_contribution + sponsorship

# Break-even registrations
if registration_fee > variable_cost:
    required = math.ceil(
        max(fixed_cost - sponsorship, 0) /
        (registration_fee - variable_cost)
    )
    print("Minimum registrations needed:", required)
else:
    print("Break-even is not possible with this registration fee.")

# Display results
print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
print("Fixed Cost:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", participant_contribution)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", sponsorship_shortfall)
print("Total Available Funds:", total_funds)

if total_funds >= total_cost:
    print("Result: Event is financially successful.")
else:
    print("Result: Additional funds are required.")

