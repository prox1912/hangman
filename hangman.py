import random
from hangmanword import word_list
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
end_of_game=False
no_of_lives=6
from hangmanart import logo
print(logo)


display=[]
for _ in chosen_word:
    display+='_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already chosen {guess}")
    if guess not in  chosen_word:
        print(f"{guess} is not in the word.You lose a life.")
        no_of_lives-=1
    
    else:
        for x in range(len(display)):
            if(chosen_word[x]==guess):
                display[x]=guess
    print(f"{''.join(display)}")
    if '_' not in display:
        end_of_game=True
        print("You win.")
    if(no_of_lives==0):
        end_of_game=True
        print("You lose.")
    from hangmanart import stages
    print(stages[no_of_lives])