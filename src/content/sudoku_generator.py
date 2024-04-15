"""A simple sudoku engine."""

import random

import matplotlib.pyplot as plt
import numpy as np

from config.paths import OUTPUT_PATH


class Sudoku:
    def __init__(self, size: int, percent_to_remove: float) -> None:
        """
        Initializes the Sudoku class.
        :param size: The size of the Sudoku grid.
        :param percent_to_remove: The percentage of numbers to remove from the grid.
        """
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.percent_to_remove = percent_to_remove

    def _valid_numbers(self, i: int, j: int) -> list[int]:
        """
        Returns a list of valid numbers for the given cell.
        :param i: The row index of the cell.
        :param j: The column index of the cell.
        :return: A list of valid numbers for the given cell.
        """
        valid_numbers = set(range(1, self.size + 1))

        for k in range(self.size):
            valid_numbers.discard(self.grid[i][k])
            valid_numbers.discard(self.grid[k][j])

        i_start, j_start = 3 * (i // 3), 3 * (j // 3)
        for i in range(i_start, i_start + 3):
            for j in range(j_start, j_start + 3):
                valid_numbers.discard(self.grid[i][j])

        return list(valid_numbers)

    def _fill_grid(self) -> None:
        """Fills the Sudoku grid with random numbers."""
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = random.sample(self._valid_numbers(i, j), 1)[0]

    def _remove_numbers(self) -> None:
        """Removes numbers from the Sudoku grid."""
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.percent_to_remove:
                    self.grid[i][j] = 0

    def solve(self, grid: np.ndarray) -> list[np.ndarray]:
        """
        Finds all solutions to the given Sudoku grid, using backtracking.
        :param grid: The Sudoku grid to solve.
        :return: A list of solutions to the Sudoku grid.
        """

        def find_empty() -> tuple | None:
            """Finds the next empty cell in the grid."""
            for i in range(self.size):
                for j in range(self.size):
                    if grid[i][j] == 0:
                        return i, j
            return None

        def solve_sudoku(solutions: list[np.ndarray]) -> None:
            """Solves the Sudoku grid using backtracking."""
            if len(solutions) > 1:
                return  # Stop when multiple solutions are found

            empty = find_empty()
            if not empty:
                solutions.append(grid.copy())
                return

            i, j = empty
            for n in self._valid_numbers(i, j):
                grid[i][j] = n
                solve_sudoku(solutions)
                grid[i][j] = 0  # Backtrack

        solutions = []
        solve_sudoku(solutions)
        return solutions

    def _is_unique(self) -> bool:
        """
        Checks if the Sudoku grid has a unique solution.
        :return: True if the Sudoku grid has a unique solution, False otherwise.
        """
        solutions: list = self.solve(self.grid)

        if len(solutions) == 1:
            return True
        else:
            return False

    def generate(self) -> None:
        """Generates a random Sudoku puzzle."""
        unique = False
        while unique is False:
            self._fill_grid()
            self._remove_numbers()
            unique = self._is_unique()


def plot_sudoku(grid: np.ndarray, name: str) -> None:
    """
    Plots the given Sudoku grid.
    :param grid: The Sudoku grid to plot.
    :param name: The name of the file to save the plot as.
    :return: None
    """

    fig, ax = plt.subplots(figsize=(6, 6))  # Set figure size
    ax.set_aspect("equal")  # Make squares actually square
    plt.xlim(0, 9)
    plt.ylim(0, 9)

    # Draw grid lines
    for i in range(10):
        lw = 2 if i % 3 == 0 else 0.5  # Make lines thicker for 3x3 blocks
        plt.axvline(i, color="black", linewidth=lw)
        plt.axhline(i, color="black", linewidth=lw)

    # Place numbers in cells
    for i in range(9):
        for j in range(9):
            num = grid[j, i]
            if num != 0:  # Only add non-zero numbers
                plt.text(
                    i + 0.5,
                    9 - j - 0.5,
                    str(num),
                    fontsize=15,
                    ha="center",
                    va="center",
                )

    plt.axis("off")  # Hide axes
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_PATH}{name}.png", dpi=300)  # Save as PNG file

    return name


def sudoku_gen() -> tuple[np.ndarray, np.ndarray]:
    """
    Generates a Sudoku puzzle and its solution.
    :return: None
    """

    while True:
        try:
            sudoku = Sudoku(9, 0.6)
            sudoku.generate()
            break
        except ValueError:
            continue

    sudoku = (
        plot_sudoku(sudoku.grid, "Sudoku"),
        plot_sudoku(np.array(sudoku.solve(sudoku.grid)[0]), "Sudoku Solution"),
    )

    return sudoku
