"""Vacuum Cleaner Problem"""

room = {"A": 1, "B": 1}
position = "A"

def vacuum_cleaner(room, position):
    visited = set()
    while True:
        if room[position] == 1:
            print(f"Cleaning room {position}")
            room[position] = 0
        else:
            print(f"Room {position} is already clean")
        if position == "A":
            next_position = "B"
        else:
            next_position = "A"
        if all(v == 0 for v in room.values()) and next_position in visited:
            print("Cleaning completed.")
            return room
        visited.add(position)
        position = next_position

if __name__ == "__main__":
    print("Initial room state:", room)
    vacuum_cleaner(room, position)
    print("Final room state:", room)
