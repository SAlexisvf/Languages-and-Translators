import numpy as np

class symbols_table_structure:
    def __init__(self, variable_id, variable_type, variable_address, function_index, dimention_1):
        self.id = variable_id
        self.type = variable_type
        self.address = variable_address
        self.index = function_index
        if variable_type == 'int':
            self.value = 0
        elif variable_type == 'double':
            self.value = 0.0
        elif variable_type == 'int_array':
            self.value = np.zeros(dimention_1, dtype=int)
        elif variable_type == 'double_array':
            self.value = np.zeros(dimention_1)
