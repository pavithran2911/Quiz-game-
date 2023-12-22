print("Welcome To My Quiz Game\nAn Interesting Game to Play")
player = input("Do you want to play the game?\n")

if player.lower() != 'yes':
    print("Good Bye")
    quit()

name_player = input("Enter Your Name: ")
print("Let's Start the Game :)", name_player)

questions = [
    ('What does CPU stand for?', 'central processing unit'),
    ('What does GPU stand for?', 'graphical processing unit'),
    ('What does RAM stand for?', 'random access memory'),
    ('What does ROM stand for?', 'read only memory'),
    ('Is a mouse an input device or output device?', 'input device')
]

score = 0

for question, correct_answer in questions:
    answer = input(f'{question}\n')
    if answer.lower() == correct_answer:
        print("Correct")
        score += 1
    else:
        print('Wrong')

print(f"You got {score} correct answers")
percentage = (score / len(questions)) * 100
print(f"You got {percentage}% correct answers")
