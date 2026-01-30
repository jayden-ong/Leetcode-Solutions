class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Once you change a substring once, you can't alter any of its chars again
        #   -- Unless it is exactly the same substring
        # Map strings to other strings
        lengths = set()
        min_cost_dict = defaultdict(dict)
        for i in range(len(original)):
            if changed[i] not in min_cost_dict[original[i]]:
                min_cost_dict[original[i]][changed[i]] = cost[i]
            else:
                min_cost_dict[original[i]][changed[i]] = min(min_cost_dict[original[i]][changed[i]], cost[i])
            lengths.add(len(original[i]))
        
        # Need to find out the min cost to convert a substring to any other substring it can convert to
        original_to_changed = defaultdict(dict)
        for substring in min_cost_dict:
            queue = [(0, substring)]
            visited = set()
            while queue:
                curr_cost, curr_string = heapq.heappop(queue)
                if curr_string in visited:
                    continue
                visited.add(curr_string)
                original_to_changed[substring][curr_string] = curr_cost
                # Cannot convert string to anything
                if curr_string not in min_cost_dict:
                    continue
                
                for next_string in min_cost_dict[curr_string]:
                    if next_string not in visited:
                        heapq.heappush(queue, (curr_cost + min_cost_dict[curr_string][next_string], next_string))
                
        curr_index = 0
        dp = [float('inf')] * (len(source) + 1)
        dp[0] = 0
        for i in range(len(source)):
            if dp[i] == float('inf'):
                continue
            
            # No need to do any ops
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            for length in lengths:
                # No conversion to be done
                if i + length > len(source):
                    continue
                
                sub_source = source[i:i + length]
                sub_target = target[i:i + length]
                if sub_source in original_to_changed and sub_target in original_to_changed[sub_source]:
                    dp[i + length] = min(dp[i + length], dp[i] + original_to_changed[sub_source][sub_target])
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        