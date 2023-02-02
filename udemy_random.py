#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 
#Write the rest of your code below this line 👇

usr_ans = str(input('"Heads" or "Tail" \n'))
x = usr_ans.capitalize()
print (f'You selected {x}')

comp_ans = random.randint(0, 1)
if comp_ans == 0:
    comp_ans = 'Heads'
else:
    comp_ans = 'Tails'
print (f'Computer answer is {comp_ans}')
