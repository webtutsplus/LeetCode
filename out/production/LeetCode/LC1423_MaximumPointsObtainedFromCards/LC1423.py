class LC1423(object):
    def maxScore(self, cardPoints, K):
        ar = cardPoints

        #O(n*n*k)
        # O(n*k)

        dic = {}

        def cal(i, j, k): # ar[i:j] for k cards, what is the answer
            # save it the dic
            if  k < 1:
                return 0

            if (i, j, k) in dic:
                return dic[(i, j, k)]

            if i > j:
                return 0

            if i == j:
                if k == 1:
                    dic[(i, j, k)] = ar[i]
                    return ar[i]
                else:
                    return 0
            dic[(i, j, k)] = max(cal(i+1, j, k-1) + ar[i], cal(i, j-1, k-1)+ar[j])
            return dic[(i, j, k)]

        ans = cal(0, len(ar)-1, K)
        #print dic
        return ans





