import enum


class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2


class Player:
    def __init__(self, name: str, piece_colour) -> None:
        self._name = name
        self._piece_colour = piece_colour

    def get_name(self) -> str:
        return self._name

    def get_piece_colour(self) -> GridPosition:
        return self._piece_colour


class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows = rows
        self._columns = columns
        self._grid: list[list[GridPosition]] = []
        self.init_grid()

    def init_grid(self) -> None:
        self._grid = [
            [GridPosition.EMPTY for _ in range(self._columns)]
            for _
            in range(self._rows)
        ]

    def get_grid(self) -> list[list[GridPosition]]:
        return self._grid

    def get_column_count(self) -> int:
        """Used to tell the user how where they can place their piece"""
        return self._columns

    def place_piece(self, column: int, piece: GridPosition) -> int:
        if column < 0 or column >= self._columns:
            raise ValueError(f"Column {column} is out of bounds")
        if piece == GridPosition.EMPTY:
            raise ValueError("Cannot place an empty piece")

        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row

        return -1

    def check_win(self, connect_n: int, row: int, column: int, piece: GridPosition) -> bool:
        # Check horizontal
        count = 0
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connect_n:
                return True

        # Check vertical
        count = 0
        for r in range(self._rows):
            if self._grid[r][column] == piece:
                count += 1
            else:
                count = 0
            if count == connect_n:
                return True

        # Check diagonal
        count = 0
        for r in range(self._rows):
            c = row + column - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connect_n:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = column - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connect_n:
                return True

        return False


class Game:
    def __init__(self, grid: Grid, connect_n: int, target_score: int) -> None:
        self._grid = grid
        self._connect_n = connect_n
        self._target_score = target_score

        self._players = [
            Player("Player 1", GridPosition.YELLOW),
            Player("Player 2", GridPosition.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player] = 0

    def print_board(self) -> None:
        print("Board:\n")
        grid = self._grid.get_grid()
        for row in grid:
            row_rep = ""
            for piece in row:
                if piece == GridPosition.EMPTY:
                    row_rep += "0 "
                elif piece == GridPosition.YELLOW:
                    row_rep += "Y "
                elif piece == GridPosition.RED:
                    row_rep += "R "
            print(row_rep)
        print("")

    def play_move(self, player: Player) -> tuple[int, int]:
        self.print_board()
        print(f"{player.get_name()}'s turn")

        col_count = self._grid.get_column_count()
        move_column = int(input(f"Enter a column (0-{col_count - 1}): "))
        move_row = self._grid.place_piece(
            move_column, player.get_piece_colour())
        return (move_row, move_column)

    def play_round(self) -> Player:
        while True:
            for player in self._players:
                move_row, move_column = self.play_move(player)
                piece_colour = player.get_piece_colour()
                if self._grid.check_win(self._connect_n, move_row, move_column, piece_colour):
                    self._score[player] += 1
                    return player

        # might result in a draw

    def play(self) -> None:
        max_score = 0
        winner = self._players[0]  # default, has no impact
        while max_score < self._target_score:
            winner = self.play_round()
            print(f"{winner.get_name()} won the round!")
            max_score = max(max_score, self._score[winner])

            self._grid.init_grid()
        print(f"{winner.get_name()} won the game!")


if __name__ == "__main__":
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()
