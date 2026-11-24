#--------------------------------------------------------
#
#
#
#--------------------------------------------------------

# reports.py
import matplotlib.pyplot as plt

#----------------------------------------------
# Creates a report summarizing the recorded shifts.
#----------------------------------------------

def shift_report(transactions):
    print("\n========== SHIFT REPORT ==========")

    if len(transactions) == 0:
        print("No transactions available to create a report.")
        return

    total_shifts = len(transactions)
    total_customers = 0
    total_sales = 0

    sales_by_season = {}
    customers_by_day = {}
#----------------------------------------------
    # Adds together customers and sales from every shift.
    for transaction in transactions:
        total_customers += transaction["customers"]
        total_sales += transaction["total_sales"]

        season = transaction["season"]
        day = transaction["day"]

        if season in sales_by_season:
            sales_by_season[season] += transaction["total_sales"]
        else:
            sales_by_season[season] = transaction["total_sales"]

        if day in customers_by_day:
            customers_by_day[day] += transaction["customers"]
        else:
            customers_by_day[day] = transaction["customers"]

    average_customers = total_customers / total_shifts
    average_sales = total_sales / total_shifts
#----------------------------------------------
    # Finds the shift with the most customers.
    busiest_shift = transactions[0]

    for transaction in transactions:
        if transaction["customers"] > busiest_shift["customers"]:
            busiest_shift = transaction

    print("Shifts recorded:", total_shifts)
    print("Total customers:", total_customers)
    print(f"Total sales: ${total_sales:.2f}")
    print(f"Average customers per shift: {average_customers:.2f}")
    print(f"Average sales per shift: ${average_sales:.2f}")

    print("\nBusiest shift:")
    print("Date:", busiest_shift["date"])
    print("Customers:", busiest_shift["customers"])
    print("Season:", busiest_shift["season"])
    print("Day:", busiest_shift["day"])

    print("\nSales by season:")

    for season, sales in sales_by_season.items():
        print(f"{season}: ${sales:.2f}")

    print("\nCustomers by day:")

    for day, customers in customers_by_day.items():
        print(f"{day}: {customers}")


#----------------------------------------------
# Creates and saves two charts from the recorded shifts.
#----------------------------------------------

def create_charts(transactions):
    if len(transactions) == 0:
        print("No transactions available to create charts.")
        return

    customers_by_day = {}
    sales_by_season = {}
#----------------------------------------------
    # Groups customers by day and sales by season.
    for transaction in transactions:
        day = transaction["day"]
        season = transaction["season"]

        if day in customers_by_day:
            customers_by_day[day] += transaction["customers"]
        else:
            customers_by_day[day] = transaction["customers"]

        if season in sales_by_season:
            sales_by_season[season] += transaction["total_sales"]
        else:
            sales_by_season[season] = transaction["total_sales"]
#----------------------------------------------
    # Organizes days in calendar order.
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

    day_names = []
    customer_totals = []

    for day in days:
        if day in customers_by_day:
            day_names.append(day)
            customer_totals.append(customers_by_day[day])
#----------------------------------------------
    # Chart 1: Customers by day of the week.
#-----------------------
    plt.figure(figsize=(8, 5))
    plt.bar(day_names, customer_totals)
    plt.title("Total Customers by Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Total Customers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("customers_by_day.png")
    plt.show()
#----------------------------------------------
    # Organizes seasons in calendar order.
    seasons = ["Winter", "Spring", "Summer", "Fall"]

    season_names = []
    sales_totals = []

    for season in seasons:
        if season in sales_by_season:
            season_names.append(season)
            sales_totals.append(sales_by_season[season])
#----------------------------------------------
    # Chart 2: Sales by season.
#-----------------------
    plt.figure(figsize=(8, 5))
    plt.plot(season_names, sales_totals, marker="o")
    plt.title("Total Sales by Season")
    plt.xlabel("Season")
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.savefig("sales_by_season.png")
    plt.show()

    print("Charts have been saved successfully!")

