# https://leetcode.com/problems/find-in-mountain-array/description/

import sys,math
class Solution:
    def findInMountainArray(self, target, mountain_arr) -> int:
        l = 0
        h = mountain_arr.length()-1
        t = -1
        top = -1
        while l<=h:
            m = math.ceil((h+l)/2)
            prev = sys.maxsize
            nex = sys.maxsize
            mid = mountain_arr.get(m)
            if m>0:
                prev = mountain_arr.get(m-1)
            if m<mountain_arr.length()-1:
                nex = mountain_arr.get(m+1)
            if mid>prev and mid>nex:
                t = m
                top = mountain_arr.get(t)
                break
            elif mid>prev and mid<nex:
                l = m+1
            else:
                h = m-1
        if target > top:
            return -1
        if target == top:
            return t
        l = 0
        h = t - 1
        while l<=h:
            m = math.ceil((h+l)/2)
            mid = mountain_arr.get(m)
            if mid == target:
                return m
            elif mid < target:
                l = m+1
            else:
                h = m-1
        l = t + 1
        h = mountain_arr.length()-1
        while l<=h:
            m = math.ceil((h+l)/2)
            mid = mountain_arr.get(m)
            if mid == target:
                return m
            elif mid > target:
                l = m+1
            else:
                h = m-1
        return -1