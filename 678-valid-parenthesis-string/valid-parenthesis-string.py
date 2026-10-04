class Solution:
    def checkValidString(self, s: str) -> bool:
        string_length = len(s)
        counter = 0
        star_counter = 0
        possible_saves = 0
        for i in range(string_length - 1, -1, -1):
            if s[i] == "(":
                counter -= 1
            elif s[i] == ")":
                counter += 1
            else:
                star_counter += 1
                if counter > 0:
                    possible_saves += 1
            
            if possible_saves > counter and counter >= 0:
                possible_saves = counter

            if counter < 0:
                if star_counter == 0:
                    return False
                star_counter -= 1
                counter += 1
                if possible_saves > 0:
                    possible_saves -= 1
        #(((((*)))**
        #((       (((*)))** counter = 0, possible_saves = 0, star_counter = 1   
        #print(counter)
        #print(possible_saves)
        return counter - possible_saves <= 0
            
