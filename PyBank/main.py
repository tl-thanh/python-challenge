import pandas as pd
import os

data_file = "budget_data_1.csv"
os.system("touch financials.txt")
# output_file = financials.txt

financials = pd.read_csv(data_file)

financials ['Monthly_Change'] = pd.rolling_apply(financials['Revenue'], 2, lambda x: x[1] - x[0])

total_months = financials['Date'].count()

total_revenue = financials['Revenue'].sum()
total_revenue = "${:,.2f}".format(total_revenue)

avg_chg = financials['Monthly_Change'].mean()
avg_chg = "${:,.2f}".format(avg_chg)

max_increase = financials.loc[financials['Monthly_Change'].idxmax()]
max_date = max_increase['Date']
max_chg = max_increase['Monthly_Change']
max_chg = "${:,.2f}".format(max_chg)

max_decrease = financials.loc[financials['Monthly_Change'].idxmin()]
min_date = max_decrease['Date']
min_chg = max_decrease['Monthly_Change']
min_chg = "${:,.2f}".format(min_chg)

print()
print('Financial Analysis')
print('----------------------------------------------------')
print('Total Months: ' + str(total_months))
print('Total Revenue: ' + str(total_revenue))
print('Average Revenue Change: ' + str(avg_chg))
print('Greatest Increase in Revenue: ' + str(max_date) + ' ' + str(max_chg))
print('Greatest Decrease in Revenue: ' + str(min_date) + ' ' + str(min_chg))

my_file = open('financials.txt', 'w')

my_file.write('Financial Analysis\n')
my_file.write('----------------------------------------------------\n')
my_file.write('Total Months: ' + str(total_months) + '\n')
my_file.write('Total Revenue: ' + str(total_revenue) + '\n')
my_file.write('Average Revenue Change: ' + str(avg_chg) + '\n')
my_file.write('Greatest Increase in Revenue: ' + str(max_date) + ' ' + str(max_chg) + '\n')
my_file.write('Greatest Decrease in Revenue: ' + str(min_date) + ' ' + str(min_chg) + '\n')

my_file.close()
