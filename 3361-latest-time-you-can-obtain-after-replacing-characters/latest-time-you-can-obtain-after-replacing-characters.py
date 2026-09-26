class Solution(object):
    def findLatestTime(self, s):
        arr = list(s)
        if arr[0] == "?":
            if arr[1] == "?" or arr[1] <= "1":
                arr[0] = "1"
            else:
                arr[0] = "0"

        if arr[1] == "?":
            if arr[0] == "1":
                arr[1] = "1"
            else:
                arr[1] = "9"

        if arr[3] == "?":
            arr[3] = "5"

        if arr[4] == "?":
            arr[4] = "9"

        return "".join(arr)