class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        balance = 100
        n = purchaseAmount % 10
        if n >= 5:
            roundamt = purchaseAmount + (10 - n)
        else:
            roundamt = purchaseAmount - n
        return balance - roundamt