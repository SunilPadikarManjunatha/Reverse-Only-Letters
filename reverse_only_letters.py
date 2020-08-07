class Solution:
    
    # if string if empty
    # if at-least one character "A"
    #two characters a- or -a
    #three characters a- or b-a, d-e
    #Four chars ab-cd, a-bcd
    
    def reverseOnlyLetters(self, S: str) -> str:
        
        length = len(S)
        f, l = 0, length-1
        s_list = list(S)

        while(f != l and f<l):
            print(s_list[f], s_list[l])
            if s_list[f].isalpha() and s_list[l].isalpha():
                s_list[f], s_list[l]= s_list[l], s_list[f]
                l-=1
                f+=1
            else:
                if not s_list[f].isalpha(): f+=1
                if not s_list[l].isalpha(): l-=1

        return ''.join(s_list)