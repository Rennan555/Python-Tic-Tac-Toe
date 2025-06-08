class Table:
    def __init__(self):
        self.X_ICON = 'X'
        self.O_ICON = 'O'
        self.spaces = [[None for _ in range(3)] for _ in range(3)]
        
    def __str__(self) -> str:
        return str(self.spaces)
    
    def check_playable_condition(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.spaces[i][j] == None: return True
        return False
    
    def check_rows(self) -> bool:        
        for i in range(3):
            if self.spaces[i][0] == None: pass
            elif self.spaces[i][0] == self.spaces[i][1] and self.spaces[i][1] == self.spaces[i][2]: return True
        return False
    
    def check_columns(self) -> bool:
        for i in range(3):
            if self.spaces[0][i] == None: pass
            elif self.spaces[0][i] == self.spaces[1][i] and self.spaces[1][i] == self.spaces[2][i]: return True
        return False
    
    def check_diagonal_down(self) -> bool:
        if self.spaces[0][0] == None: pass
        elif self.spaces[0][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][2]: return True
        return False
    
    def check_diagonal_up(self) -> bool:
        if self.spaces[0][2] == None: pass
        elif self.spaces[0][2] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][0]: return True
        return False
    
    def check_victory_condition(self) -> str:
        for i in range(3):
            if self.check_rows(): return self.spaces[i][0] # Horizontal check
            if self.check_columns(): return self.spaces[0][i] # Vertical check
        if self.check_diagonal_down(): return self.spaces[0][0] # Diagonal down check
        elif self.check_diagonal_up(): return self.spaces[0][2] # Diagonal up check
        else: return None # Game continues / Draw

# Test cases
if __name__ == '__main__':
    t = Table()
    op = 2
    match op:
        case 0:
            t.spaces[0][0] = t.O_ICON
            t.spaces[0][1] = t.O_ICON
            t.spaces[0][2] = t.O_ICON
        case 1:
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][0] = t.O_ICON
            t.spaces[2][0] = t.O_ICON
        case 2:
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[2][2] = t.O_ICON
        case 3:
            t.spaces[0][2] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[2][0] = t.O_ICON
        case 4:
            for i in range(3):
                for j in range(3):
                    t.spaces[i][j] = t.O_ICON
        case _:
            t.spaces[0][0] = t.O_ICON
            t.spaces[1][1] = t.O_ICON
            t.spaces[0][2] = t.O_ICON
    print(f'Table: {t}')
    print(f'Victory: {t.check_victory_condition()}')
    print(f'Playable: {t.check_playable_condition()}')
