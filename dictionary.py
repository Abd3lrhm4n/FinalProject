import io
import os
import glob
import errno
# from sys import argv

# def main():

#     pw = argv[1]

#     DictSearchAlgo(LoadFile(), pw)

result = dict()

def LoadFile():

    source = 'data/dictionary/*.txt'

    # list of data
    dictionary = list()

    files = glob.glob(source)

    # read all txt in directory 
    for name in files:
        try:
            with open(name, "r") as f:
                for line in f:
                    dictionary.append(line.replace("\n", ''))

        # Not sure what error this is
        except IOError as exc:  
            if exc.errno != errno.EISDIR:
                raise

    return dictionary


def DictSearchAlgo(Dict, pw):

    # hold the password value
    password = pw

    # matches words list
    matches = list()

    for w in Dict:
        if password.find(str(w)) != -1:
            
            # remove the matches words from the password
            password = password.replace(str(w), '')

            # add the match word in the list
            matches.append(w)

    # calculate the percentage of the words in the password
    percentage = round(((len(password) / len(pw) * 100) - 100) * -1, 2)

    # store results data
    result = {"matches": matches, "percentage": percentage}

    return result



# if __name__ == "__main__":
#     main()
