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

    # check if the password checked
    isChecked = False

    while isChecked == False: 

        i = 0

        # loop in every char in password
        while i < len(password):

            # get the similair from the trie
            r = trie.prefixes(password[i:])

            i += 1

            # if result
            if len(r) > 0:

                # take the longest word
                w = max(r, key=len)

                # add it to matches list
                matches.append(w)

                # remove it from the password
                password = password.replace(w, '', 1)

                # loop over again from the began
                i = 0

        # break while loop
        isChecked = True

    # calculate the percentage of the words in the password
    percentage = round(((len(password) / len(pw) * 100) - 100) * -1, 2)

    # store results data
    result = {"matches": matches, "percentage": percentage}

    return result



# if __name__ == "__main__":
#     main()
