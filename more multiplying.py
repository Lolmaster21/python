# Lukas Henriquez
# CSCI128 - Section H
# Python-BasicMultiplicationTable

initial_i = int(input())
final_i = int(input())
initial_j = int(input())
final_j = int(input())

for i in range(initial_i,final_i+1):
    for j in range(initial_j,final_j+1):
        n = i * j
        print(f"{i} x {j} = {n}")
