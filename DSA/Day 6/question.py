def check_Anagram(s1,s2):
    if(len(s1) == len(s2)):
        for i in range(len(s1)):
            if(s1[i] == s2[i]):
                print("Not Anagram")
                exit()
                break

        for i in s1:
            if i in s2:
                s = True
            else:
                s = False
        if s:
            print('Anagram')
        else:
            print("Not Anagram")


s1 = input()
s2 = input()
check_Anagram(s1,s2)