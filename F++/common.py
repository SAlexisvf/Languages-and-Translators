class symbols_table_structure:
    def __init__(self, variable_id, variable_type, variable_address, function_index):
        self.id = variable_id
        self.type = variable_type
        self.address = variable_address
        self.index = function_index
        self.value = 0 if variable_type == 'int' or 'int_array' else 0.0

