class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        answer = ["a"] * (len(str1) + len(str2) - 1)
        answer_fixed = [False] * (len(str1) + len(str2) - 1)
        # Start by filling in the necessary characters according to "T"
        for i, condition in enumerate(str1):
            if condition == "T":
                for j in range(i, i + len(str2)):
                    next_char = str2[j - i]
                    if answer[j] != next_char and answer_fixed[j] == True:
                        return ""
                    answer[j] = next_char
                    answer_fixed[j] = True
        
        for i, condition in enumerate(str1):
            # Have to make a modification
            if condition == "F" and ''.join(answer[i:i + len(str2)]) == str2:
                fixed = False
                #print(i)
                #print(len(str2))
                #print(len(answer))
                #print(''.join(answer[i:i + len(str2)]))
                for j in range(i + len(str2) - 1, i - 1, -1):
                    if answer_fixed[j] == False:
                        # Might have to fix
                        answer[j] = "b"
                        fixed = True
                        break
                
                if not fixed:
                    return ""
        return ''.join(answer)