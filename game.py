import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = 4
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.finished_at = None

    def elapsed(self):
        end = self.finished_at if self.finished_at is not None else time.monotonic()
        return int(end - self.started)

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print("Moves:", self.moves, " Time:", self.elapsed(), "s")

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")
        while True:
            self.display()
            if self.puzzle.solved():
                print(f"Solved in {self.moves} moves and {self.elapsed()}s!")
                return
            key = input("> ").strip().lower()
            if key == "q":
                return
            if key not in "wasd":
                print("Use W/A/S/D.")
                continue
            if self.puzzle.move(key):
                self.moves += 1
                if self.puzzle.solved():
                    self.finished_at = time.monotonic()   # freeze the timer
            else:
                print("That move is not possible.")