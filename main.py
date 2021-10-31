import random
import words
import art
# Step 1

word_list = words.word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = art.stages

print(logo)

chosen_word = random.choice(word_list)
lives = 6
cur_stage = len(stages) - 1

blank_list = []
for letter in chosen_word:
    blank_list.append("_")
tried = []

first_round = True
while lives != 0:

    guess = input("guess a letter : ")
    guess.lower()
    guess = guess[0]
    if guess in tried:
        print(f"You already this guessed {guess}.")
        continue
    tried.append(guess)

    if guess not in chosen_word:
        cur_stage -= 1
        print(stages[cur_stage])
        lives -= 1
        print("Wrong")
        print(f"{' '.join(blank_list)}")
        continue
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                blank_list[position] = letter
                print(stages[cur_stage])

    str1 = ""

    # traverse in the string
    for ele in blank_list:
        str1 += str(ele)
    if lives != 0 and str1 == chosen_word:
        print(stages[lives])
        print(blank_list)
        print("You win")
        break

    print(f"{' '.join(blank_list)}")
if lives <= 0:
    print("--------")
    print("You lose")
    print("--------")
    print(f"The Word is {chosen_word} . ")

