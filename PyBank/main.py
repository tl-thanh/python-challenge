import pandas as pd

data_file = "budget_data_1.csv"

financials = pd.read_csv(data_file)

total_months = financials["Date"].count()

total_revenue = financials["Revenue"].sum()
total_revenue = "${:,.2f}".format(total_revenue)

print('Financial Analysis')
print('------------------------------')
print('Total Months: ' + total_months)
print('Total Revenue: ' + total_revenue)
print('Average Revenue Change: ')
print('Greatest Increase in Revenue: ')
print('Greatest Decrease in Revenue: ')
