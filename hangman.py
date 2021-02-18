import random
def hangman():
    wordList = ['batman', 'cat', 'dog', 'owl', 'business', 'computer', 'insurrection']
    randomNum = random.randint(0,len(wordList)-1)
    word = wordList[randomNum]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    print("Type ! at any time to quit")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char == "!":
            break
        elif char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0 : wrong]))
        print("You lost. The correct word was {}.".format(word))

hangman()
