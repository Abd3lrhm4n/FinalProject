from sys import argv
import re
from humanize import intword

# pw = argv[1]

# def __main__():
#     Bruteforce(pw)
#     TimeEstimateSec(pw)
#     SecondsToYears(sec)

def Bruteforce(pw):

    upper = False
    lower = False
    num = False
    symbol = False


    # collect the total score of the password
    score = 0
    
    for i in range(len(pw)):
        
        # check upper characters
        if pw[i].isupper() and not upper:
            score += 26
            upper = True

        # check lower characters
        elif pw[i].islower() and not lower:
            score += 26
            lower = True

        # check num characters
        elif pw[i].isnumeric() and not num:
            score += 10
            num = True

        # check speical characters
        elif re.match(r"[^\w]", pw[i]):
            score += 10
            symbol = True

        else:
            score += 0

    return score**len(pw)
     


def TimeEstimateSec(pw):

    # proccess frequence 3Ghz
    proccessFreq = 3000000000

    seconds = 0

    seconds = (Bruteforce(pw) / proccessFreq) * (10**3)

    return round(seconds)

def SecondsToYears(sec):
    
    time = dict()
    years = 0
    months = 0
    weeks = 0
    days = 0
    hours = 0
    minutes = 0
    seconds = sec

    # calculate years 
    years = round(seconds / 60 / 60 / 24 / 7 / 30 /12)
    seconds %= (60 * 60 * 24 * 7 * 30 * 12)

    # calculate month
    months = round(seconds / 60 / 60 / 24 / 7 / 30)
    seconds %= (60 * 60 * 24 * 7 * 30)

    # calculate weeks 
    weeks = round(seconds / 60 / 60 / 24 / 7)
    seconds %= (60 * 60 * 24)

    # calcuate days
    days = round(seconds / 60 / 60 /24)
    seconds %= (60 * 60 * 24)

    # calculate hours 
    hours = round(seconds / 60 / 60)
    seconds %= (60 * 60)

    # calculate mintues 
    minutes = round(seconds / 60)
    seconds %= (60)

    # hold the time in dict
    time = {"years": f"{intword(years)}", "months": f"{months}", "weeks": f"{weeks}",
            "days": f"{days}", "hours": f"{hours}", "mintues": f"{minutes}", "seconds": f"{seconds}"}

    return time
    
# if __name__ == "__main__":
#     SecondsToYears(TimeEstimateSec(pw))
