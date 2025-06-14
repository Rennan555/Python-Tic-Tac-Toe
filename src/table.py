class Table:
    def __init__(self):
        self.X_ICON = 'X'
        self.O_ICON = 'O'
        self.CURRENT_PLAYER = self.X_ICON
        self.OPOSITE_PLAYER = self.O_ICON
        self.spaces = [[None for _ in range(3)] for _ in range(3)]
        
    def __str__(self) -> str:
        return str(self.spaces)
    
    def change_player(self) -> None:
        if self.CURRENT_PLAYER == self.X_ICON:
            self.CURRENT_PLAYER = self.O_ICON
            self.OPOSITE_PLAYER = self.X_ICON
        else:
            self.CURRENT_PLAYER = self.X_ICON
            self.OPOSITE_PLAYER = self.O_ICON
    
    def play(self, x, y) -> None:
        '''
        Play a move
        
        args:
            x (int): Row
            y (int): Column
        '''
        if self.spaces[x][y] != None: return
        else:
            self.spaces[x][y] = self.CURRENT_PLAYER
            self.change_player()
    
    def check_playable_condition(self) -> bool:
        '''
        Check if the table is still playable
        '''
        for i in range(3):
            for j in range(3):
                if self.spaces[i][j] == None: return True
        return False
    
    def check_rows(self) -> bool:
        '''
        Check if there is a horizontal win
        '''
        for i in range(3):
            if self.spaces[i][0] == None: pass
            elif self.spaces[i][0] == self.spaces[i][1] and self.spaces[i][1] == self.spaces[i][2]: return True
        return False
    
    def check_columns(self) -> bool:
        '''
        Check if there is a vertical win
        '''
        for i in range(3):
            if self.spaces[0][i] == None: pass
            elif self.spaces[0][i] == self.spaces[1][i] and self.spaces[1][i] == self.spaces[2][i]: return True
        return False
    
    def check_diagonal_down(self) -> bool:
        '''
        Check if there is a diagonal win (upper left to lower right)
        '''
        if self.spaces[0][0] == None: pass
        elif self.spaces[0][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][2]: return True
        return False
    
    def check_diagonal_up(self) -> bool:
        '''
        Check if there is a diagonal win (lower left to upper right)
        '''
        if self.spaces[0][2] == None: pass
        elif self.spaces[0][2] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][0]: return True
        return False
    
    def check_victory_condition(self) -> str:
        '''
        Check if there is a win (all conditions)
        '''
        winner = 'Winner player: '
        if self.check_rows(): return winner + self.OPOSITE_PLAYER # Horizontal check
        elif self.check_columns(): return winner + self.OPOSITE_PLAYER # Vertical check
        elif self.check_diagonal_down(): return winner + self.OPOSITE_PLAYER # Diagonal down check
        elif self.check_diagonal_up(): return winner + self.OPOSITE_PLAYER # Diagonal up check
        elif self.check_playable_condition(): return None # Game continues
        else: return 'Draw'

# Test cases
if __name__ == '__main__':
    t = Table()
    op = 0
    match op:
        case 0: # Horizontal win
            t.spaces[1][0] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[1][2] = t.O_ICON
        case 1: # Vertical win
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][0] = t.O_ICON
            t.spaces[2][0] = t.O_ICON
        case 2: # Diagonal win (upper left to lower right)
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[2][2] = t.O_ICON
        case 3: # Diagonal win (lower left to upper right)
            t.spaces[0][2] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[2][0] = t.O_ICON
        case 4: # Unplayable case
            for i in range(3):
                for j in range(3):
                    t.spaces[i][j] = t.O_ICON
        case _: # Unfinished unconcluded game
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[0][2] = t.O_ICON
    t.play(1, 0)
    print(f'Table: {t}')
    print(f'Player: {t.CURRENT_PLAYER}')
    print(f'{t.check_victory_condition()}')
