class ElegantPrint:
    
    def __init__(self):
        self.last_line_len = 0
        
    def clear_line(self):
        print(' '*self.last_line_len, end='\r')
    
    def print(self, output, same_line=False):
        output = str(output)
        if same_line:
            print(output + ' '*(self.last_line_len - len(output)), end='\r')
            self.last_line_len = len(output)
        else:
            print(output + ' '*(self.last_line_len - len(output)))

ep = ElegantPrint()
eprint = ep.print