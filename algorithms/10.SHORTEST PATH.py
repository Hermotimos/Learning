"""
    This file is for learning and exercise purposes.

    Topics:
        - graphs
        - algorithms: shortest path

    Sources:
        Aditya Bhargava - Algorytmy. Ilustrowany przewodnik.
"""
from collections import deque


# undirected graph1 (Sierpinski_Hanoi.jpg)
graph1 = dict()
graph1[1] = [2, 3]
graph1[2] = [1, 3, 4]
graph1[3] = [1, 2, 5]
graph1[4] = [2, 6, 7]
graph1[5] = [3, 8, 9]
graph1[6] = [4, 7, 10]
graph1[7] = [4, 6, 8]
graph1[8] = [5, 7, 9]
graph1[9] = [5, 8, 11]
graph1[10] = [6, 12, 13]
graph1[11] = [9, 14, 15]
graph1[12] = [10, 13, 16]
graph1[13] = [10, 12, 17]
graph1[14] = [11, 15, 18]
graph1[15] = [11, 14, 19]
graph1[16] = [12, 20, 21]
graph1[17] = [13, 22, 23]
graph1[18] = [14, 24, 25]
graph1[19] = [15, 26, 27]
graph1[20] = [16, 21]
graph1[21] = [16, 20, 22]
graph1[22] = [17, 21, 23]
graph1[23] = [17, 22, 24]
graph1[24] = [18, 23, 25]
graph1[25] = [18, 24, 26]
graph1[26] = [19, 25, 27]
graph1[27] = [19, 26]

graph1[28] = [29, 30]
graph1[29] = [28, 30]
graph1[30] = [28, 29]

# ---------------------------------------------------------------------


# BFS (breadth-first search)

def check_if_path_exists(graph, starting_point, target_point):
    search_queue = deque()
    search_queue += graph[starting_point]
    searched = []
    while search_queue:
        checked_now = search_queue.popleft()
        if checked_now not in searched:
            if checked_now == target_point:
                return True
            else:
                search_queue += graph[checked_now]
                searched.append(checked_now)
    return False


print(check_if_path_exists(graph1, 1, 21))
print(check_if_path_exists(graph1, 27, 21))
print(check_if_path_exists(graph1, 1, 30))
