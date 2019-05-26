import io
import os
import glob
import errno

def main():

    # read dictionary file
    # with open("large.txt", "r") as file:
    #     data = file.read()
    
    # # load file data in list
    # dictionary = data.split("\n")

    # for x in range(10):
    #     print(dictionary[x])

    LoadFile()


def LoadFile():

    source = 'data/dictionary/*.txt'

    # list of data
    dictionary = list()

    files = glob.glob(source)

    # read all txt in directory 
    for name in files:
        try:
            with open(name) as f:
                for line in f:
                    dictionary.append((line.split()))

        except IOError as exc:  # Not sure what error this is
            if exc.errno != errno.EISDIR:
                raise

    return dictionary












if __name__ == "__main__":
    main()
