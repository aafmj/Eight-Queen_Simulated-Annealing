import math
import random


class EightQueen:
    def __init__(self):
        self.size = 8
        self.temp = 10
        # Initialize with a random placement of queens.
        self.board = [random.randint(0, self.size - 1) for i in range(0, self.size)]
        print('initial State:')
        self.display(self.board)
        print('---------------------------------\n---------------------------------')

    def display(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[j] != i:
                    print('-', end='  ')
                else:
                    print('Q', end='  ')
            print()


    def random_movement(self):
        board_copy = self.board.copy()
        i = random.randint(0, self.size - 1)
        while True:
            j = random.randint(0, self.size - 1)
            if board_copy[i] != j:
                board_copy[i] = j
                return board_copy


    def get_total_strike(self, board):
        strike = 0
        for queen in range(0, self.size):
            for next_queen in range(queen + 1, self.size):
                if board[queen] == board[next_queen] or abs(queen - next_queen) == abs(
                        board[queen] - board[next_queen]):
                    strike += 1
        return strike


    def simulated_annealing(self):
        while self.get_total_strike(self.board) != 0 and self.temp > 0.2:
            self.temp = self.temp * 0.9
            new_board = self.random_movement()
            dE = self.get_total_strike(new_board) - self.get_total_strike(self.board)
            if dE < 0 or 0 < random.uniform(0, 1) < math.e ** (((-1)* dE) / self.temp):
                self.display(new_board)
                self.board = new_board
                print("dE " , dE)
                print("temp " , self.temp)
                print("probability ", math.e ** ((-1)*dE / self.temp))
                print('total strike:', self.get_total_strike(self.board))
                print('---------------------------------')

        print('#################################\n')
        print('final State:')
        self.display(self.board)
        print('total strike:', self.get_total_strike(self.board))


if __name__ == '__main__':
    eight_queen = EightQueen()
    eight_queen.simulated_annealing()
