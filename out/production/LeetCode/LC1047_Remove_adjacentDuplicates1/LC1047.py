class LC1047(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        stack = []


        for char in S:
            if len(stack) == 0:
                stack.append(char)
            else:
                #If our curr character is equal to the top of the stack, we pop it , don't insert that
                #character in the stack
                if stack[-1] == char:
                    stack.pop()
                else:
                    #Else push that character into the stack
                    stack.append(char)

        #At last , print the stack, (We need to pop all elements from the stack , then reserve it and return it, but in python it is easier to do that)
        return "".join(stack)

