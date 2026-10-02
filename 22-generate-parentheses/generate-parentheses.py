class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        # n = 1 - ["()"]
        if n == 1:
            return ["()"]
        else:
            # n = 2 - ["(())", "()()"] - put parentheses around first and left of first?
            # n = 3 - ["((()))","(()())","(())()","()(())","()()()"]
            # n = 3 - figure out third and fourth one
            # output - n = 4 - ["()(())()"]
            # expected - n = 4 - ["(())(())"]
            curr_answer = []
            prev_case = self.generateParenthesis(n - 1)
            for case in prev_case:
                curr_answer.append("(" + case + ")")
                curr_answer.append(case + "()")
                if curr_answer[-1] != "()" + case:
                    curr_answer.append("()" + case)
        return curr_answer
        '''

        def choice(num_left, num_right, curr_paren):
            if len(curr_paren) == n * 2:
                return [curr_paren]
            
            answer = []
            # It means that the last 
            if num_left < n:
                answer += choice(num_left + 1, num_right, curr_paren + "(")
            
            if num_right < n and num_right < num_left:
                answer += choice(num_left, num_right + 1, curr_paren + ")")
            return answer
        
        return choice(0, 0, "")