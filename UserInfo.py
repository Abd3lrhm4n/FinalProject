

def main():
    UserInfoAnalysis('AbdelmoneamMokhtar', "AbdoMokhtar")



def UserInfoAnalysis(info, pw):

    info = info.lower()
    pw = pw.lower()
    
    found = list()

    word = ""

    i = 0
    j = 0

    while i < len(info):
        
        while j < len(pw):

            # p = pw[j]
            # w = info[i]

            if i == len(info):

                i = 0
                j += 1

                if j == len(pw):
                        
                    if len(word) > 0:
                        
                        found.append(word)

                    break

            if pw[j] != info[i]:

                i += 1

                if len(word) > 0:

                    found.append(word)

                    word = ""

                    i = 0

            else:

                word += info[i]

                i += 1
                j += 1

        if j == len(pw):
            
            if len(word) > 0:
                
                found.append(word)

            break

    return max(found, key=len)




if __name__ == "__main__":
    main()