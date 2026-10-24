class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Want to convert the month numbers into days
        month_to_days = {"01" : 0, "02" : 31, "03" : 59, "04" : 90, "05": 120, "06" : 151, "07" : 181, "08" : 212, "09" : 243, "10" : 273, "11" : 304, "12" : 334}
        alice_arrive = month_to_days[arriveAlice[0:2]] + int(arriveAlice[3:])
        alice_leave = month_to_days[leaveAlice[0:2]] + int(leaveAlice[3:])
        bob_arrive = month_to_days[arriveBob[0:2]] + int(arriveBob[3:])
        bob_leave = month_to_days[leaveBob[0:2]] + int(leaveBob[3:])
        return max(0, min(alice_leave, bob_leave) - max(alice_arrive, bob_arrive) + 1)