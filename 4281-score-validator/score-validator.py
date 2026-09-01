class Solution(object):
    def scoreValidator(self, events):
        score = 0
        counter = 0
        for i in events:
            if i in "012346":
                score = score + int(i)
            elif i == "WD" or i == "NB":
                score += 1
            elif i == "W":
                counter += 1
            if counter == 10:
                break
        a = []
        a.append(score)
        a.append(counter)
        return a