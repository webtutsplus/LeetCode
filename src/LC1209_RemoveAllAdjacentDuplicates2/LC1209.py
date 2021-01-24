class LC1209(object):
    def removeDuplicates(self, s, k):
        stack = []
        count = 0

        for c in s:

            if stack and c == stack[-1][0]:
                prev = stack.pop()[1]
                stack.append((c, prev + 1))

                if prev + 1 == k:
                    stack.pop()
            else:
                count = 1
                stack.append((c, count))

        result = ''
        for char, count in stack:
            result += char * count

        return result
