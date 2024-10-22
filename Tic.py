import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.ai_level = 'Simple'
        self.buttons = []
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.master, text=str(row * 3 + col), font='Arial 20', width=5, height=2,
                                command=lambda r=row, c=col: self.player_move(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
        
        self.level_label = tk.Label(self.master, text='AI Level: Simple')
        self.level_label.grid(row=3, columnspan=3)
        self.change_level_button = tk.Button(self.master, text='Change AI Level', command=self.change_ai_level)
        self.change_level_button.grid(row=4, columnspan=3)

    def change_ai_level(self):
        levels = ['Simple', 'Moderate', 'Hard']
        current_index = levels.index(self.ai_level)
        new_index = (current_index + 1) % len(levels)
        self.ai_level = levels[new_index]
        self.level_label.config(text=f'AI Level: {self.ai_level}')

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.update_buttons()

    def update_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.board[row][col] if self.board[row][col] != '' else str(row * 3 + col))

    def player_move(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = 'X'  # Player is always 'X'
            if self.check_winner():
                self.end_game('Player X wins!')
            elif all(cell != '' for row in self.board for cell in row):
                self.end_game("It's a draw!")
            else:
                self.ai_move()

        self.update_buttons()

    def ai_move(self):
        if self.ai_level == 'Simple':
            self.simple_ai()
        elif self.ai_level == 'Moderate':
            self.moderate_ai()
        elif self.ai_level == 'Hard':
            self.hard_ai()

        # Check for a winner after AI's move
        if self.check_winner():
            self.end_game('AI wins!')
        elif all(cell != '' for row in self.board for cell in row):
            self.end_game("It's a draw!")
        self.update_buttons()

    def simple_ai(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 'O'

    def moderate_ai(self):
        best_move = self.find_best_move('O')
        if best_move != (-1, -1):
            self.board[best_move[0]][best_move[1]] = 'O'

    def hard_ai(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '':
                    self.board[r][c] = 'O'
                    if self.check_winner():
                        return
                    self.board[r][c] = ''

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '':
                    self.board[r][c] = 'X'
                    if self.check_winner():
                        self.board[r][c] = 'O'
                        return
                    self.board[r][c] = ''

        if self.board[1][1] == '':
            self.board[1][1] = 'O'
            return

        for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if self.board[r][c] == '':
                self.board[r][c] = 'O'
                return

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '':
                    self.board[r][c] = 'O'
                    return

    def find_best_move(self, player):
        best_value = -float('inf') if player == 'O' else float('inf')
        best_move = (-1, -1)

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '':
                    self.board[r][c] = player
                    move_value = self.minimax(0, player)
                    self.board[r][c] = ''
                    if player == 'O':
                        if move_value > best_value:
                            best_value = move_value
                            best_move = (r, c)
                    else:
                        if move_value < best_value:
                            best_value = move_value
                            best_move = (r, c)

        return best_move

    def minimax(self, depth, player):
        if self.check_winner():
            return 10 if player == 'O' else -10
        if all(cell != '' for row in self.board for cell in row):
            return 0

        if player == 'O':
            best_value = -float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == '':
                        self.board[r][c] = 'O'
                        best_value = max(best_value, self.minimax(depth + 1, 'X'))
                        self.board[r][c] = ''
            return best_value
        else:
            best_value = float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == '':
                        self.board[r][c] = 'X'
                        best_value = min(best_value, self.minimax(depth + 1, 'O'))
                        self.board[r][c] = ''
            return best_value

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def end_game(self, message):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state='disabled')  # Disable buttons
        end_label = tk.Label(self.master, text=message, font='Arial 14')
        end_label.grid(row=5, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
