#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 15:25
# @File     : 20-单词拆分.py
# @Project  : AGTD


class Solution(object):

    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for j in range(1, len(s) + 1):
            for word in wordDict:
                if j >= len(word):
                    # dp[i]: 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])

        return dp[-1]


if __name__ == '__main__':
    s1 = "catsandog"
    wordDict1 = ["cats", "dog", "sand", "and", "cat"]
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    solution = Solution()
    res1 = solution.wordBreak(s1, wordDict1)
    res2 = solution.wordBreak(s2, wordDict2)
    print(res1, res2)
