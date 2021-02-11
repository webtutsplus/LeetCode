class Solution(object):
    def findPairs(self, nums, k):

        dic = {}
        #We create an iterator, i is the index in the array and element is the integer in that array.
        #Here we will create dictionary.
        # [3,1,4,1,5] , k=2
        # So for this input we will create a dictionary
        # 3 ->[0] , 1 -> [1,3] , 4-> [2] , 5-> [4]
        # nums = [1,3,1,5,4], k = 0
        # 1 -> [0,2] , 3 -> [1] , 5 -> [3] , 4-> [4]
        # As k=0; this is a special case, so we will check occurance of a no .
        # As 1 appears twice, our output will be 1.

        for i, element in enumerate(nums):
            if element in dic:
                dic[element].append(i)
            else:
                dic[element] = [i]

        #The answer dictionary contains the possible pairs for this problem.
        ans = {}
        #We run a loop for each element in the dictionary.
        for element in dic:
            #k==0 is a special case. So if we have multiple occurance a no , then we can consider one pair for it.
            if k == 0:
                if len(dic[element]) > 1:
                    ans[(element, element)] = True
            else:
                #As the k-diff is taken as absolute , we have to check for both element+k and element-k in the dictionary.
                #If it is present we will add them into the ans dictionary.
                if element + k in dic:
                    ans[(element, element+k)] = True
                if element -k in dic:
                    ans[(element-k, element)] = True
        #We just have to return the size of the ans dictionary
        return len(ans)