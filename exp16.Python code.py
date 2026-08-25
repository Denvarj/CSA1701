"""Simulated Annealing Algorithm"""
import math
import random

def objective(x):
    return -(x - 5) ** 2

def simulated_annealing():
    current = random.uniform(-10, 10)
    temp = 100.0
    best = current
    best_score = objective(current)
    while temp > 0.01:
        new = current + random.uniform(-1, 1)
        new_score = objective(new)
        delta = new_score - objective(current)
        if delta > 0 or random.random() < math.exp(delta / temp):
            current = new
        if objective(current) > best_score:
            best = current
            best_score = objective(current)
        temp *= 0.95
    return best, best_score

if __name__ == "__main__":
    print("Simulated annealing best:", simulated_annealing())
