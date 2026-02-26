'''Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = list()
        store = n
        while (store>0):
            rem = int(store%2)
            store = int(store/2)
            binary.append(rem)
        temp = binary[0]
        alternating = True
        for i in range(1,len(binary)):
            if temp == binary[i]:
                alternating = False
                return False
                break
            temp = binary[i]
        if alternating:
            return True
