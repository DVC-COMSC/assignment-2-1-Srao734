num_males = input('Enter num males: ')
num_females = input("Enter num females: ")
sum = int(num_males) + int(num_females)
m_perc = (int(num_males) / int(sum)) * 100
f_perc = (int(num_females) / int(sum)) * 100
print ("The total number of students: 		%d" % (sum))
print ("The number of males and females: 	%s 	   %s" % (num_males, num_females))
print (f'The percentage of males and females \t {m_perc:.2f} \t {f_perc:.2f}')

return m_perc, f_perc

