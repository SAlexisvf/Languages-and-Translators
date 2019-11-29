import numpy as np

class symbols_table_structure:
    '''
    Symbols table structure for the program variables
    '''
    def __init__(self, variable_id, variable_type, variable_address, function_index, dimention_1, dimention_2):
        self.id = variable_id
        self.type = variable_type
        self.address = variable_address
        self.index = function_index
        if variable_type == 'int':
            self.value = 0
        elif variable_type == 'double':
            self.value = 0.0
        elif variable_type == 'int_array':
            if dimention_2 != 0:
                self.value = np.zeros((dimention_1, dimention_2), dtype=int)
            else:
                self.value = np.zeros(dimention_1, dtype=int)
        elif variable_type == 'double_array':
            if dimention_2 != 0:
                self.value = np.zeros((dimention_1, dimention_2))
            else:
                self.value = np.zeros(dimention_1)
