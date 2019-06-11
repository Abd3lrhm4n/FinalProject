

# def main():
#     UserInfoAnalysis('AbdelmoneamMokhtar', "AbdoMokhtar")



def UserInfoAnalysis(info, pw):

    info = info.lower()
    pw = pw.lower()
    
    # found words list
    found = list()

    # word which found
    word = ""

    i = 0
    j = 0

    while i < len(info):
        
        while j < len(pw):

            # p = pw[j]
            # w = info[i]

            # if the end of word start from began again
            if i == len(info):

                i = 0
                j += 1

                # if the end of word
                if j == len(pw):
                        
                    # and word found
                    if len(word) > 0:
                        
                        # append found word in list
                        found.append(word)

                    break

            # if the word not equal move to next
            if pw[j] != info[i]:

                i += 1

                # and if there's a word found
                if len(word) > 0:

                    # append it
                    found.append(word)

                    # then clear
                    word = ""

                    # start over again
                    i = 0

            else:

                # append this char to word
                word += info[i]

                # then move next
                i += 1
                j += 1

        # the end of word
        if j == len(pw):
            
            # and there's a word
            if len(word) > 0:
                
                # append it
                found.append(word)

            break
        
    # if found list not empty
    if len(found):  

        # get the longest word and return it
        return max(found, key=len)

    # if nothing return null
    else:
        return ''



# if __name__ == "__main__":
#     main()