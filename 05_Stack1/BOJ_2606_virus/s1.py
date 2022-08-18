import sys

sys.stdin = open('input.txt')

computers = int(input())
adjacent_com = int(input())
graph = [[] for _ in range(computers+1)]

for i in range(adjacent_com):
