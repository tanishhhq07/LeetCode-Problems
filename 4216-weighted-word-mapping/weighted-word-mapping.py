class Solution(object):
    def mapWordWeights(self, words, weights):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = []
        for word in words:
            total = 0
            for ch in word:
                index = alphabet.index(ch)
                total += weights[index]

            remainder = total % 26
            result.append(alphabet[25 - remainder])

        return "".join(result)