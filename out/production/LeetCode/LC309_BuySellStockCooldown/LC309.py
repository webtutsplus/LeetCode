class LC309(object):
    def maxProfit(self, prices):

        #THis is the answer
        self.max_profit = 0
        def backtrack(index, is_buy, buy_price, profit):
            # THis is the base condition. When no more buying or selling is possible.
            # We dont have to check for the is_buy variable , because even if we buy one item ,
            # we cant get a profile without selling it . Therefore that check is not necessary
            if index >= len(prices):
                self.max_profit = max(self.max_profit, profit)
                return

            #If is_buy is true, then we can buy one item .
            if is_buy:
                # It means we buy the index-th item , and we send index+1 and is_buy as false; ie we have
                #to sell the item first before buying another one.
                #price variable is the price at which one item is bought (index-th item is bought)
                price = prices[index]
                #We backtrack for selling that item.
                backtrack(index+1, False, price, profit)

               #We don't buy that item . So we skip this index .
                backtrack(index+1, True, buy_price, profit)

                return

            #If is_buy is false, then we sell that item.
            #When we sell that item , we get our profit as = stock's price today - stock's price the day it was bought
            sell_price = prices[index]
            new_profit = profit + (sell_price-buy_price)

            #So we need to have one day's cooldown , so pass index+2 and is_buy as true . ie. buying is possible only at and after index+2 -th day
            backtrack(index+2, True, 0, new_profit)

            #We don't sell the item this time, we wait for the next day. So index+1 and false is passed as we cant buy item next index+1 th day too.
            backtrack(index+1, False, buy_price, profit)



        #This is our starting case. We say item can be bought on the first day . The backtracking starts from here.
        backtrack(0, True, 0, 0)
        return self.max_profit
