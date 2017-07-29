import pandas as pd
import os

data_file = "election_data_2.csv"
os.system("touch election_results.txt")

election = pd.read_csv(data_file)
                                                                                                                                                                                                                
total_votes = election['Voter ID'].count()
denominator = float(total_votes)
total_votes = "{:,.0f}".format(total_votes)


candidates_list = election.Candidate.unique()
num = len(candidates_list)

candidates_count = election.groupby(['Candidate']).count()

my_file = open('election_results.txt', 'w')

my_file.write('Election Results\n------------------------------\n')
my_file.write('Total Votes: ' + str(total_votes) + '\n')
my_file.write('------------------------------\n')


print()
print('Election Results\n------------------------------')
print('Total Votes: ' + str(total_votes))
print('------------------------------')

i=0
win = 0

while i < num:
	a = candidates_list[i]
	c_locate = candidates_count.loc[a,['Voter ID']]
	b = float(c_locate['Voter ID'])
	if b > win:
		win = b
		winner = a
	percentage = b / denominator * 100
	percentage = "{0:.1f}%".format(percentage)
	b = "{:,.0f}".format(b)
	print(a + ': ' + percentage + ' (' + str(b) + ') ')
	my_file.write(a + ': ' + percentage + ' (' + str(b) + ') ' + '\n')
	i = i + 1

print('------------------------------')
print('Winner: ' + winner)
print('------------------------------')

my_file.write('------------------------------\n')
my_file.write('Winner: ' + winner + '\n')
my_file.write('------------------------------')

my_file.close()
