package LC309_BuySellStockCooldown;

public class LC309 {
    //This is the dynamic programming approach which we can be used. We are using a memoize the values fro the buyIndex and sellIndex.
    public int maxProfit(int[] prices) {
        int[][] memo = new int[prices.length][prices.length];
        return getMaxProfit(prices, 0, 1, memo);
    }

    int getMaxProfit(int[] prices, int bIdx, int sIdx, int[][] memo){

        //This is the base case for our solution
        if(bIdx >= prices.length || sIdx >= prices.length) return 0;

        //If that value is found in the table, we return it, thus reducing our computational complexity.
        if(memo[bIdx][sIdx] != 0) return memo[bIdx][sIdx];

        //So if the price of sIdx(sellingIndex) is greater than that of bIdex (buyingIndex) , we can make profit.

        if(prices[sIdx] > prices[bIdx]) {
            //This is the profit we get when we sell that item today . prices[sIdx] - prices[bIdx] -> is the profit for selling that item .
            //Now we have to call the getMaxProfit with sIdx+2 as buyIndex bcz buying is possible after 2  days. (we can not buy another item )
            // the day we sold it, one day of cooldown is also required. Therefore buyIndex is sIdx+2 and sellingIndex is sIdx is sIdx+3, selling
            //is possible one day after buying.
            int profit_by_selling_now = (prices[sIdx] - prices[bIdx]) + getMaxProfit(prices, sIdx + 2, sIdx + 3, memo);
            //We compare the value of profit made by selling today and by selling the next days . This gives us optimal value for profit if we buy item at bIdx.
            memo[bIdx][sIdx] = Math.max(profit_by_selling_now, getMaxProfit(prices, bIdx, sIdx + 1, memo));
        }
        else
            //We can't get profit on that day, we increment the buyingIndex by 1 and the sellingIndex by 2. We call the getMaxProfit method with these parameters.
            memo[bIdx][sIdx] = getMaxProfit(prices, bIdx + 1, bIdx + 2, memo);

        //This is our answer
        return memo[bIdx][sIdx];
    }
}


