class Solution(object):
    def sortPeople(self, names, heights):
        people = []
        for i in range(len(names)):
            people.append((heights[i], names[i]))
        people.sort(reverse = True)
        answer = []
        for height, name in people:
            answer.append(name)
        return answer