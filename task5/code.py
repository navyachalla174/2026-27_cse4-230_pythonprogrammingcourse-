
# Multi-Plan Telecommunications Cost Optimization

plans = []
eligible_plans = []

print("===== MOBILE PLAN OPTIMIZATION =====")

# User requirements
data_required = float(input("Enter required data (GB): "))
calls_required = int(input("Enter required call minutes: "))
sms_required = int(input("Enter required SMS: "))
validity_required = int(input("Enter required validity days: "))
budget = float(input("Enter maximum budget: "))

n = int(input("Enter number of mobile plans: "))

for i in range(n):

    print("\nEnter details of Plan", i + 1)

    name = input("Enter plan name: ")
    cost = float(input("Enter plan cost: "))
    data = float(input("Enter data limit (GB): "))
    calls = int(input("Enter call minutes: "))
    sms = int(input("Enter SMS limit: "))
    validity = int(input("Enter validity days: "))

    # Calculate excess charges
    extra_data = max(0, data_required - data) * 10
    extra_calls = max(0, calls_required - calls) * 1
    extra_sms = max(0, sms_required - sms) * 0.50

    total_cost = cost + extra_data + extra_calls + extra_sms

    plan = {
        "name": name,
        "cost": cost,
        "total": total_cost,
        "validity": validity,
        "extra_data": extra_data,
        "extra_calls": extra_calls,
        "extra_sms": extra_sms
    }

    plans.append(plan)

    # Check eligibility
    if validity >= validity_required and total_cost <= budget:
        eligible_plans.append(plan)


# Display plan comparison
print("\n===== PLAN COMPARISON =====")

for p in plans:
    print("\nPlan:", p["name"])
    print("Base Cost: Rs.", round(p["cost"], 2))
    print("Excess Data Charge: Rs.", round(p["extra_data"], 2))
    print("Excess Call Charge: Rs.", round(p["extra_calls"], 2))
    print("Excess SMS Charge: Rs.", round(p["extra_sms"], 2))
    print("Total Cost: Rs.", round(p["total"], 2))

# Find economical plan
print("\n===== BEST MOBILE PLAN =====")

if eligible_plans:

    best = min(eligible_plans, key=lambda p: p["total"])

    print("Most Economical Plan:", best["name"])
    print("Total Cost: Rs.", round(best["total"], 2))
    print("Validity:", best["validity"], "days")

else:
    print("No eligible plan found within your budget.")

print("\nPlan Comparison Completed!")

