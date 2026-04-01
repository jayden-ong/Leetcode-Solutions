class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Want to put all positions, health, direction, robot_num in a heap
        # Want to start with earliest position first
        robots_heap = []
        for i in range(len(positions)):
            heapq.heappush(robots_heap, (positions[i], healths[i], directions[i], i))
        
        robots_stack = []
        while robots_heap:
            curr_pos, curr_health, curr_dir, curr_index = heapq.heappop(robots_heap)
            # If the robot is moving right, add to robots_stack(cannot run into anything yet)
            if curr_dir == "R":
                robots_stack.append([curr_pos, curr_health, curr_dir, curr_index])
            else:
                # If there are no robots on the stack, nothing to hit
                # If the robot on top is moving left, nothing to hit
                while robots_stack and robots_stack[-1][2] == "R" and curr_health > 0:
                    # If curr robot has more health, kick off robot from stack
                    if curr_health > robots_stack[-1][1]:
                        robots_stack.pop()
                        curr_health -= 1
                    elif curr_health == robots_stack[-1][1]:
                        robots_stack.pop()
                        curr_health = 0
                    else:
                        if robots_stack[-1][1] <= 1:
                            robots_stack.pop()
                        else:
                            robots_stack[-1][1] -= 1
                        curr_health = 0
                
                # Went through all viable robots and won
                if curr_health > 0:
                    robots_stack.append([curr_pos, curr_health, curr_dir, curr_index])
        
        # Now want to sort by index
        index_heap = []
        while robots_stack:
            curr_pos, curr_health, curr_dir, curr_index = robots_stack.pop()
            heapq.heappush(index_heap, (curr_index, curr_health))
        
        answer = []
        while index_heap:
            _, curr_health = heapq.heappop(index_heap)
            answer.append(curr_health)
        return answer