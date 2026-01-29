class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Want to use Djikstra's to determine min cost
        edges_dict = {}
        all_letters_set = set()
        for i in range(len(original)):
            if original[i] not in edges_dict:
                edges_dict[original[i]] = {}
            
            if changed[i] in edges_dict[original[i]]:
                edges_dict[original[i]][changed[i]] = min(cost[i], edges_dict[original[i]][changed[i]])
            else:
                edges_dict[original[i]][changed[i]] = cost[i]
            all_letters_set.add(original[i])
            all_letters_set.add(changed[i])

        min_cost_dict = {}
        for char in edges_dict:
            local_min_cost_dict = {}
            local_min_cost_dict[char] = 0
            queue = [(0, char)]
            letters_seen = set()
            while queue and len(letters_seen) < len(all_letters_set):
                curr_cost, curr_letter = heapq.heappop(queue)
                if curr_letter not in letters_seen and curr_letter in edges_dict:
                    for next_letter in edges_dict[curr_letter]:
                        if next_letter in local_min_cost_dict:
                            local_min_cost_dict[next_letter] = min(local_min_cost_dict[next_letter], edges_dict[curr_letter][next_letter] + curr_cost)
                        else:
                            local_min_cost_dict[next_letter] = edges_dict[curr_letter][next_letter] + curr_cost

                        if next_letter not in letters_seen:
                            heapq.heappush(queue, (edges_dict[curr_letter][next_letter] + curr_cost, next_letter))
    
                letters_seen.add(curr_letter)
            min_cost_dict[char] = local_min_cost_dict
        
        answer = 0
        for i in range(len(target)):
            if source[i] != target[i]:
                if source[i] not in min_cost_dict:
                    return -1
                
                if target[i] not in min_cost_dict[source[i]]:
                    return -1
                
                answer += min_cost_dict[source[i]][target[i]]
        return answer