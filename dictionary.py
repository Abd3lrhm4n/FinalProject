import io
import os
import glob
import errno
from sys import argv
import marisa_trie

# def main():

#     pw = argv[1]

#     DictSearchAlgo(LoadFile('data/dictionary/*.marisa'), pw)

result = dict()

trie = marisa_trie.Trie()


def LoadFile(dirPath):

    source = dirPath

    files = glob.glob(source)

    # read all txt in directory 
    for name in files:
        try:
            with open(name, "r") as f:
                trie.read(f)

        # Not sure what error this is
        except IOError as exc:  
            if exc.errno != errno.EISDIR:
                raise

    return trie


def DictSearchAlgo(Dict, pw):

    # hold the password value
    password = pw

    # matches words list
    matches = list()

    isChecked = False

    while isChecked == False: 

        r = trie.prefixes(password)

        if len(r) > 0:

            w = max(r, key=len)
            matches.append(w)
            password = password.replace(w, '', 1)

        else:
            isChecked = True

    # calculate the percentage of the words in the password
    percentage = round(((len(password) / len(pw) * 100) - 100) * -1, 2)

    # store results data
    result = {"matches": matches, "percentage": percentage}

    return result



# if __name__ == "__main__":
#     main()
