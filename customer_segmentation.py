def segment_customer(spending):
    if spending >= 5000:
        return "VIP"
    elif spending >= 1000:
        return "Regular"
    else:
        return "At Risk"


customers = [
    ["Alice", 7500],
    ["Bob", 2300],
    ["Charlie", 450],
    ["Diana", 5200],
    ["Eve", 1800],
    ["Frank", 12000],
    ["Grace", 650],
]


vip_total = 0
regular_total = 0
at_risk_total = 0

vip_count = 0
regular_count = 0
at_risk_count = 0


for customer in customers:
    segment = segment_customer(customer[1])

    if segment == "VIP":
        vip_total += customer[1]
        vip_count += 1
    elif segment == "Regular":
        regular_total += customer[1]
        regular_count += 1
    else:
        at_risk_total += customer[1]
        at_risk_count += 1
if vip_count > 0:
    vip_average = vip_total / vip_count
else:
    vip_average = 0

if regular_count > 0:
    regular_average = regular_total / regular_count
else:
    regular_average = 0

if at_risk_count > 0:
    at_risk_average = at_risk_total / at_risk_count
else:
    at_risk_average = 0

print("=== CUSTOMER SEGMENTATION REPORT ===")
print()

print(f"VIP Customers: {vip_count}")
print(f"Total Spending: ${vip_total:,}")
print(f"Average Spending: ${vip_average:,.0f}")
print()

print(f"Regular Customers: {regular_count}")
print(f"Total Spending: ${regular_total:,}")
print(f"Average Spending: ${regular_average:,.0f}")
print()

print(f"At Risk Customers: {at_risk_count}")
print(f"Total Spending: ${at_risk_total:,}")
print(f"Average Spending: ${at_risk_average:,.0f}")
print()

print("=== OVERALL SUMMARY ===")
total_customers = vip_count + regular_count + at_risk_count
total_revenue = vip_total + regular_total + at_risk_total
print(f"Total Customers: {total_customers}")
print(f"Total Revenue: ${total_revenue:,}")
