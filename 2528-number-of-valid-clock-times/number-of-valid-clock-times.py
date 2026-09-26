class Solution(object):
    def countTime(self, time):
        count = 0
        for hour in range(24):
            for minute in range(60):
                current = "%02d:%02d" % (hour, minute)
                valid = True
                for i in range(5):
                    if time[i] != "?" and time[i] != current[i]:
                        valid = False
                        break
                if valid:
                    count += 1

        return count