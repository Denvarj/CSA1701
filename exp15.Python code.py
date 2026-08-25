"""Hill Climbing Algorithm"""
import random

def hill_climbing():
    current = random.uniform(-10, 10)
    current_value = -(current ** 2) + 10
    for _ in range(100):
        neighbor = current + random.uniform(-1, 1)
        neighbor_value = -(neighbor ** 2) + 10
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
    return current, current_value

if __name__ == "__main__":
    print("Hill climbing solution:", hill_climbing())
