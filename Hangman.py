def main():
    import time
    start_time = time.time()
    greeting()
    list_of_pairs = file_load()
    original_list = randomizing_capital(list_of_pairs)
    country = original_list[0]
    capital = original_list[1]
    lifes = 5
    dashed_capital = dashing_capital(capital)
    container = []
    game(capital, lifes, dashed_capital, container, start_time, country)


def greeting():
    print("\n", "Welcome to the HangMan game!", "\n", sep='')


def file_load():
    file = open("/home/kodoj/codecool/candc.txt",'r')  
    content = file.read()                                       
    list_of_pairs = content.upper().split("\n")                         
    for i in range (0, len(list_of_pairs)):                    
        list_of_pairs[i] = list_of_pairs[i].split(" | ")
    return list_of_pairs


def randomizing_capital(lista):
    import random
    n=random.randint(0, len(lista))                         
    original_list = lista[n]
    return original_list


def dashing_capital(capital):
    dashed_capital = []
    for item in capital:
        if item == ' ':
            dashed_capital.append("  ")
        else:
            dashed_capital.append(".")    
    return dashed_capital


def game(capital, lifes, dashed_capital, container, start_time, country):
    anything_guessed = False
    if lifes>0:
        print("Time to guess: ")
    print(dashed_capital)
    while True:
        hang_manager(lifes)
        if lifes>0:
            print("You still have ", lifes, "lifes", "\n")
        if lifes == 1:
            print("It is a capital of: ", country, "\n")
        if lifes == 0:
            print("You lose :(", "\n")
            print("The capital of:", country, "is", capital, "\n")
            play_again()
        else:
            input_handle(lifes, capital, dashed_capital, container, start_time, country) 
            

def input_handle(lifes, capital, dashed_capital, container, start_time, country):
    print("Those is your previous input", container, "\n")
    guess = input("Gimme Your best shoot!: ").upper()
    if guess not in container:
        container.append(guess)
    if guess.isdigit():
        print("This is not a letter nor a word!")
        input_handle(lifes)
    else:
        if len(guess) == 1:
            check_letter(guess, capital, lifes, dashed_capital, container, start_time, country)
        else:
            check_word(guess, lifes, capital, dashed_capital, container, start_time, country)
    return lifes
    
        
def check_word(guess, lifes, capital, dashed_capital, container, start_time, country):
    if guess.upper() == capital:
        bonus = 30
        when_win(lifes, start_time, bonus)
        play_again()
    elif lifes>1:
        game(capital, lifes-2, dashed_capital, container, start_time, country)
    else:
        game(capital, lifes-1, dashed_capital, container, start_time, country)
        

def check_letter(guess, capital, lifes, dashed_capital, container, start_time, country):
    if guess in capital:
        for i in range(0, len(capital)):
            if capital[i] == guess:
                dashed_capital[i] = guess.upper()
                if '.' not in dashed_capital:
                    bonus = 0
                    when_win(lifes, start_time, bonus)
                    play_again()
        print(dashed_capital)
        return dashed_capital

    else:
        game(capital, lifes-1, dashed_capital, container, start_time, country)
def play_again():
    sign = input("Do you want to play again y/n?")
    if sign == 'y':
        main()
    elif sign == 'n':
        exit()
    else:
        print("You make it hard :/ ")        

def when_win(lifes, start_time, bonus):
    import time
    end_time = time.time()
    time_of_game = int(end_time - start_time)
    score = 100 + lifes * 10 - time_of_game * 0.6 + bonus
    if score <= 0:
        score = 0
    print("BRAWOOOOOO!! Your score equals: ", score)
    nickname = input("Tell me your name: ")
    highscore_input(score, nickname)
    highscore_output()


def hang_manager(lifes):
    if lifes<=4:
        path=("/home/kodoj/Downloads/"+str(lifes)+".txt")
        with open(path) as f:
            print(f.read())


def highscore_input(score, nickname):
    highscore_file = open("/home/kodoj/codecool/highscore.txt","a")
    score_to_write = nickname + " | " + str(score)
    highscore_file.write(score_to_write)
    highscore_file.write("\n")
    highscore_file.close()
    

def highscore_output():
    from operator import itemgetter
    file = open("/home/kodoj/codecool/highscore.txt","r")
    content = file.read()
    score_board = content.split("\n") 
    score_board = score_board[:-1]
    n = len(score_board)
    for i in range (0,n):
        score_board[i] = score_board[i].split(" | ")
    for j in range(0,n):                                 
        score_board[j][1] = float(score_board[j][1])
    score_board.sort(key = lambda x: x[1], reverse=True)
    if len(score_board) > 10:
        for i in range(0, 10):
            print(score_board[i])
    else:
        for i in range(0, len(score_board)):
            print(i+1, ". ", score_board[i][0], "  ", score_board[i][1])
    file1 = open("/home/kodoj/codecool/highscore.txt", "w")
    for j in range(0, len(score_board)):
        record = (str(score_board[j][0]) + " | " + str(score_board[j][1]) + "\n", sep='')
        file1.write(record)


main()

