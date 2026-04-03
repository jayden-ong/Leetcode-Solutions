class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robots_to_range = {}
        for i in range(len(robots)):
            robots_to_range[robots[i]] = distance[i]
        robots.sort()
        walls.sort()

        left_walls, right_walls, walls_between = [0] * len(robots), [0] * len(robots), [0] * len(robots)

        for i in range(len(robots)):
            # Places the robot where it would be between the walls
            insert_point = bisect.bisect_right(walls, robots[i])
            # If the robot is the first, no need to worry about other robots to the left
            # We are inserting the bullet right after the wall it hits to determine the number of walls it can destroy
            if i == 0:
                last_wall = bisect.bisect_left(walls, robots[i] - robots_to_range[robots[i]])
            else:
                # Could hit a robot
                # Either the robot before is too far away or it hits the robot
                # It cannot hit the wall the prev robot is on -- if there is one
                max_range = max(robots[i] - robots_to_range[robots[i]], robots[i - 1] + 1)
                last_wall = bisect.bisect_left(walls, max_range)
            left_walls[i] = insert_point - last_wall

            insert_point2 = bisect.bisect_left(walls, robots[i])
            if i == len(robots) - 1:
                last_wall2 = bisect.bisect_right(walls, robots[i] + robots_to_range[robots[i]])
            else:
                max_range = min(robots[i] + robots_to_range[robots[i]], robots[i + 1] - 1)
                last_wall2 = bisect.bisect_right(walls, max_range)
            right_walls[i] = last_wall2 - insert_point2

            if i != 0:
                walls_between[i] = insert_point - bisect.bisect_left(walls, robots[i - 1])
        
        prev_left, prev_right = left_walls[0], right_walls[0]
        for i in range(1, len(robots)):
            # If you shoot left and the other robot shot left, no conflict
            # If the prev robot shot right, subtract the walls the prev robot hit
            # The maximum amount of walls you can hit is the number of walls between the robots
            # It is also possible the two robots don't have the range to hit all the walls between them
            current_left = max(prev_left + left_walls[i], prev_right - right_walls[i - 1] + min(left_walls[i] + right_walls[i - 1], walls_between[i]))
            # There is no way for past robots to interfere if this robot shoots right
            current_right = max(prev_left + right_walls[i], prev_right + right_walls[i])
            prev_left, prev_right = current_left, current_right
        return max(prev_left, prev_right)