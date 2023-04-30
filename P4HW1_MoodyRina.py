#CTI-110
#P4HW1 - Score List
#Rina Moody
#April 19, 2023
#This program calculate and display lowest score, modified list, scores average, and grade.

#Ask user "How many scores do you want to enter? "
#Input Score Amount
#Ask user "Enter the score: "
#Input Score
#The score should be between 0 and 100
#If it is not, notify the user and ask for a valid score to be entered

#Display lowest Score
#Display Modified List
#Display Scores Average
#Display Grade



scoreAmount = int(input('How many scores do you want to enter? '))
print()
count = 0
scoreList = []
for count in range(scoreAmount):
    count = count + 1
    score = float(input(f'Enter the score #{count}: '))
    if score >= 0 and score <= 100:
       scoreList.append(score) 
    else:
        print('\nINVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score = float(input(f'Enter the score #{count} again:  '))
        scoreList.append(score)

lowestScore = min(scoreList)
sum = sum(scoreList)
scoreList.remove(min(scoreList))
average = sum/scoreAmount


        
print('\n\n--------------Results--------------')


print(f'{"Lowest Score  : "}{lowestScore}')
print(f'{"Modified List : "}{scoreList}')
print(f'{"Scores Average: "}{average:.2f}')

if average >= 90:
    print(f'{"Grade         : "}A')
elif average >= 80:
    print(f'{"Grade         : "}B')
elif average >= 70:
    print(f'{"Grade         : "}C')
    
print('----------------------------------------')
        
