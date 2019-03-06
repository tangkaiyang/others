# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         # 取出所有无重复元素的子串:从第一个元素依次取最长子串,子串取出规则:取到的元素不在之前的子串中
#         s_len = len(s)
#         if s_len <= 1:
#             return s_len
#         else:
#             i = 0
#             m = 1
#             substring_len = []
#             while i < s_len:
#                 substring = [s[i]]
#                 while m < s_len:
#                     if s[m] not in substring:
#                         substring.append(s[m])
#                         print(substring)
#                     else:
#                         substring_len.append(len(substring))
#                         break
#                     substring_len.append(len(substring))
#                     m += 1
#                 i += 1
#                 m = i + 1
#             return max(substring_len)
#             # return substring_len
#
#
# sol = Solution()
# print(sol.lengthOfLongestSubstring(''))

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s:str
        :rtype: int
        :param s:
        :return:
        """
        result = 0
        temp = []
        for item in s:
            if item in temp:
                if len(temp) > result:
                    result = len(temp)
                temp = temp[temp.index(item)+1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(len(temp), result)
sol = Solution()
print(sol.lengthOfLongestSubstring(''))