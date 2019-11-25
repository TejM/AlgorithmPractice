""" https://www.hackerrank.com/challenges/the-minion-game/problem """

def minion_game(string):
    vowels ="AEIOU"

    num_kevin = 0
    num_stuart = 0

    for x in range(len(string)):
        if string[x] in vowels:
            num_kevin += len(string) - x
        else:
            num_stuart += len(string) - x
    
    if num_kevin>num_stuart:
        print("Kevin", num_kevin)
    elif num_stuart>num_kevin:
        print("Stuart", num_stuart)
    else:
        print("Draw")
