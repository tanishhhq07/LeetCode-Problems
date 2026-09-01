class Solution(object):
    def scoreValidator(self, events):
        total = 0
        counter = 0
        digits = "012346"
        for i in events:
            if i in digits:
                total = total + int(i)
            elif i == "WD" or i == "NB":
                total += 1
            elif i == "W":
                counter += 1
            if counter == 10:
                break
        arr = []
        arr.append(total)
        arr.append(counter)
        return arr