class Solution:
    def minInsertions(self, s: str) -> int:
        num_rights_required = num_rights_seen = 0
        answer = 0
        for i, char in enumerate(s):
            if char == ")":
                if num_rights_required > 0:
                    num_rights_required -= 1
                else:
                    num_rights_seen += 1
            else:
                if num_rights_seen > 0:
                    if num_rights_seen % 2 == 0:
                        answer += num_rights_seen // 2
                    else:
                        answer += (num_rights_seen + 1) // 2 + 1
                    num_rights_seen = 0
                    num_rights_required += 2
                else:
                    if num_rights_required % 2 == 1:
                        num_rights_required += 1
                        answer += 1
                    else:
                        num_rights_required += 2
                    
        # "()(()))()())))"
        answer += num_rights_required
        answer += (num_rights_seen + 1) // 2
        if num_rights_seen % 2 == 1:
            answer += 1
        return answer
