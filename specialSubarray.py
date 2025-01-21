from os import *
from sys import *
from collections import *
from math import *

from typing import List


def specialSubarray(n: int, arr: List[int]) -> List[int]:
    # write your code here
    freqs = {0:set({})}
    itemfqs = dict()
    for i in range(n):
        freqs.get(itemfqs.get(arr[i],0),set({})).discard(arr[i])
        itemfqs[arr[i]] = itemfqs.get(arr[i],0) + 1
        freqs[itemfqs.get(arr[i],1)]=freqs.get(itemfqs.get(arr[i],1),set({}))
        freqs[itemfqs.get(arr[i],1)].add(arr[i])
    modefq = max(freqs)
    if modefq==1:
        return arr[:1]
    else:
        modes = freqs[modefq]
        smallestcont = arr
        for m in modes:
            start = -1
            end = -1
            tempmodefq = modefq
            for i in range(n):
                if start == -1:
                    if arr[i] == m:
                        start = i
                        end = i
                        tempmodefq-=1
                elif not tempmodefq==0 and start>=0:
                    end+=1
                    if arr[i]==m:
                        tempmodefq-=1
            if end-start+1<len(smallestcont):
                smallestcont = arr[start:end+1]
    return smallestcont
            
specialSubarray(21,[21,23,5,13,9,10,17,2,21,22,9,15,20,5,3,10,24,22,10,24,22])