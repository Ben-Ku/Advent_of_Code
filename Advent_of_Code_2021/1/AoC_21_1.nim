import strutils
import sequtils


var
    s = readFile("input1.1.txt")
    s_list = s.split("\n")
    s_list_int = s_list.mapIt(parseInt(it))

echo s_list_int


var count = 0
for i in 1 .. high(s_list_int):
    if s_list_int[i-1] < s_list_int[i]:
        inc count

echo count

# part 2

var count_2 = 2
for i in 2 .. high(s_list_int)-3:
    if s_list_int[i] < s_list_int[i+3]:
        inc count_2

echo count_2
