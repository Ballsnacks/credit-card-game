#!/usr/bin/env python3

import sys
import random
import time
import os
os.system('color') # apparently this makes colors work for windows users

main = ""
cvc = ""
date = ""
margin = " "*8
seconds = ""
failure_words = ["Bollocks", "Bugger", "ffs", "Shite", "Damn", "Goddammit", "Gah", "Nope", "Boo", "Dagnabbit", "For goodness' sake", "Nuh-uh", "Nah", "Negative", "You almost did it", "Yea...but no", "Do you need a break?", "WOW... Thats embarassing", "No... Just no", "YOU ALMOST DID IT", "try removing distractions", "GOOD JOB you failed", "That's okay, I remembered for you", "BEEP BOOP, wrong answer", "You cant just mash the keys and hope its right!!", "lolwut", "Losing feels bad, doesn't it", "You need a clear mind to do this", "Ok...THAT was pretty bad", "You did it! if failure was your goal", "Your better than this", "Not today criminal scum", "Sorry sport, try again", "Not very epic of you", "Not even close","$*#@!!",]#you want failure_words? we got em!
success_words = ["Woohooo!", "No way", "PARTY!", "Hell yeah", "Well done", "Good job", "Awww yeah", "Indeed", "Hurrah", "Whoopee", "Hooray", "You're a master", "Nice", "Awesome", "Amazing", "Keep up the good work", "Keep it up", "You did it!", "WOW", "Your training is nearing its completion", "Your getting better at this!", "YASS", "YOU DID IT OMG", "NICE BRAIN", "WOOHOO!! Drinks are on me", "Easy Peasy", "PIECE OF CAKE", "You got lucky that time", ":D", "AND THE CROWD GOES WILD",]#Oh, your in to success_words? we got you covered baby!
names = ["John Smith", "Gamithra M.", "Donald Trump", "Foo Bar", "Jane Doe", "David", "Karl Marx", "Abe Lincoln", "Elon Musk", "Steve Jobs", "S. Wozniak", "Willy Wonka", "Bill Gates", "Henry Ford", "Ada Lovelace", "Master Yoda", "Tommy Wiseau", "Capt. Picard", "K. Janeway", "Henry Rollins", "Kōbō Abe", "Monty Python", "Tasha Yar", "Amuro Ray", "Annie Easley", "Jean Bartik", "Ben Swolo", "Wanda Austin", "B. Coleman", "Malcolm Owen", "Zach Hill", "Al Cisneros", "D. Jenifer", "Cal Chuchesta", "G. Galilei", "Anaximander", "Nancy Wake", "Louis Braille", "Bruce Wayne", "Anne Sullivan", "GabeN", "Albert Camus", "Herodotus", "Lenie Clarke", "Hari Seldon", "Will Smith", "Gaal Dornick", "Bel Riose", "Nikki Jumpei",  "Leeloo", "Korben Dallas", "Haru Nemuri", "Dizzy Flores", "Sugar Watkins", "Sadi Carnot", "James Charles", "Alfred Nobel", "VISA PREPAID", "B.B. King", "Paul Simon", "A. Garfunkel", "Tom Scott", "Giichi Nomura", "Zoz Brooks", "Marty Robbins", "GIFTCARD","Mace Windu", "Mari Natsuki", "D. Rothschild", "Carlton Banks",]#you want some names? Easy! WE GOT IT ALL!!
banks = ['\u263B', '\u262F', '\u2605', '\u2622', '\u2665', '\u266B', '\u2691', '\u2654']

# failure and success colors
fc = "\x1B[38;5;124m"
sc = "\x1B[38;5;76m"
cd = "\x1B[0m" # default color
cbg = ""


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdout.write('\x1Bc')
        sys.stdout.flush()


def print_card():
    global main, date, cvc, cbg, cd, banks

    cl = str(16 + random.randint(0,5) * 36 + random.randint(0, 20)) # magic values to make sure the colours are on the darker side
    cbg = "\x1B[48;5;" + cl + "m" # colored background
    ctx = "\x1B[38;5;" + cl + "m" # colored text (for the corners)
    cch = "\x1B[48;5;136m"

    name, bank = random.choice(names), random.choice(banks)

    card_front = [ctx + '\u259F' + cd + cbg +" "*26 + cd + ctx + '\u2599' + cd, \
                  cbg + " "*24 + bank + " "*3 + cd, \
                  cbg + " "*28 + cd, \
                  cbg + " "*3 + cch + " "*4 + cbg + " "*21 + cd, \
                  cbg + " "*28 + cd, \
                  cbg + "   "+ main + " "*(25-len(main)) + cd, \
                  cbg + "   "+ name + (14-len(name))*" " + date + "      " + cd, \
                  ctx + '\u259C' + cd + cbg +" "*26 + cd + ctx + '\u259B' + cd, \
                  ]

    card_back = [ctx + '\u259F' + cd + cbg +" "*26 + cd + ctx + '\u2599' + cd, \
                  cd + " "*28 + cd, \
                  cd + " "*28 + cd, \
                  cbg + " "*28 + cd, \
                  cbg + " "*3 + "\x1B[48;5;231m" + "\x1B[38;5;16m" + " "*8 + cvc + cbg + " "*14 + cd, \
                  cbg + " "*28 + cd, \
                  cbg + " "*28 + cd, \
                  ctx + '\u259C' + cd + cbg +" "*26 + cd + ctx + '\u259B' + cd, \
                  ]


    for i in range(len(card_front)):
        print(margin + card_front[i] + "   " + card_back[i])

    print("")

def luhn(digits):
    """
    Calc the correct CC checksum for our random CC number.
    input - digits - is a list of integers.
    """
    odds_sum = sum(digits[-2::-2])
    evens_sum = sum([sum(divmod(2*i, 10)) for i in digits[-1::-2]])
    sum_digits = odds_sum+evens_sum
    # because we have an odd num of digits, we just take the mod 10
    return (10-(sum_digits % 10)) % 10

def do_checksum(pan):
    pan_digits = list(map(int,pan.replace("-","")))
    return pan[:-1]+str(luhn(pan_digits[:-1]))


def ask():
    global main, date, cvc, seconds
    print(margin + "Memorize as many digits as you can!")
    print("")

    main = ""

    # add numbers that start with zero
    for i in range(4):
        main += str(random.randint(1,9999)).zfill(4)
        if i < 3: main += "-"
    # added checksum - luhn
    main = do_checksum(main)

    cvc = str(random.randint(100, 999))

    expires_day = random.randint(1, 12)
    if expires_day < 10:
        expires_day = "0" + str(expires_day)
    date  = str(expires_day) + "/" + str(random.randint(20, 28))


    sys.stdout.write("\r")
    print_card()
    if seconds != "":
        for remaining in range(seconds, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(margin + "    {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
    else:
        input(margin + "Press Enter when you're done!")
    clear_screen()


def calc_score(a, b, date=False):
    score = 0
    if date:
        if a[0:2] == b[0:2]:
            score += 1
        if a[3:5] == b[3:5]:
            score += 1
    else:
        for i in range(min(len(a), len(b))):
            if a[i] != "-" or a[i] == "/":
                if a[i] == b[i]:
                    score += 1

    return score



def success():
    global sc, cd
    return sc + success_words[random.randint(0, len(success_words)-1)] + "!" + cd

def failure():
    global fc, cd
    return fc + failure_words[random.randint(0, len(failure_words)-1)] + "!" + cd

def guess():
    global main, date, cvc, cbg, cd


    for i in range(4):
        print("")

    guess_main = input(margin + cbg + "What was the credit card number? \n" + cd + margin + "Format: xxxx-xxxx-xxxx-xxxx\n"+ margin)
    score_main = calc_score(guess_main, main)
    if guess_main == main:
        print(margin + success() + " You got it right!")
    elif score_main > 0:
        print(margin + failure() + " It was " + main + ", but you got " + str(score_main) + " digits right!")
    else:
        print(margin + failure() + " It was " + main + ".")
    print("")

    guess_cvc = input(margin + cbg + "What was the CVC?\n" + cd + margin + "Format: xxx\n"+margin)
    score_cvc = calc_score(guess_cvc, cvc)
    if guess_cvc == cvc:
        print(margin + success() + " That's correct.")
    elif score_cvc > 0:
        print(margin + failure() + " It was " + cvc + ", but you got " + str(score_cvc) + " digits right!")
    else:
        print(margin + failure() + " It was " + cvc + ".")
    print("")

    guess_date = input(margin + cbg + "What was the expiry date?\n" + cd + margin + "Format: xx/xx\n"+margin)
    score_date = calc_score(guess_date, date, date=True)
    if guess_date == date:
        print(margin + success() + " That's it.")
    elif score_date > 0:
        print(margin + failure() + " It was " + date + ", but you got " + str(score_date) + " digits right!")
    else:
        print(margin + failure() + " It was " + date + ".")

    print("")
    print(margin + "\x1B[48;5;231m" + "\x1B[38;5;16m" + " Score for this round: " + str(int((score_main + score_cvc + score_date)/21*100)) + "% " + cd)

    print("")
    print("")

    print(margin + "Too easy? To set a time limit, just run:\n"+margin+"'python3 credit_card.py [seconds]'!")
    print("")

    print(margin + "\x1B[38;5;22m" + "made by @gamithra" + cd)
    play_again = input(margin + "Press Enter to play again - or 'q' to quit!")
    if play_again == "q":
        print(margin + "See you again soon :-)")
    else:
        play()


def play():
    global seconds
    clear_screen()
    if len(sys.argv) > 1:
        seconds = int(sys.argv[1])
    for i in range(4):
        print("")

    ask()
    guess()

if __name__ ==  "__main__":
    play()


