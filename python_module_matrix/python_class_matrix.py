'''

TO DO:

[3] Document all steps for this project in a README

[7] Make this project accessible from pip thourhg GitHub and/or PyPi

[8] Add more methods to increase the utility of this class

[9] Create derived classes with __super__ references

[10] Write unit tests

'''

class Matrix():
    def __init__(self, Number_of_Columns_and_Rows = (0,0), value = 5): # This is the initializer (constructor) method, which creates an instance object of the class Matrix().
        if not isinstance(Number_of_Columns_and_Rows, tuple):
            raise TypeError("Number_of_Rows_and_Columns must be set to a tuple of integers. E.g. - (rows, columns)")
        self.rows = Number_of_Columns_and_Rows[0]
        self.columns = Number_of_Columns_and_Rows[1]
        self.matrix = [[value,] * self.columns] * self.rows 
    
    def __iter__(self): # This results in the Matrix class object to be an iterable data type (I think).
        return self
    
    def __next__(self): # This results in the ability to traverse each element of the iterable data type (I think).
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
    def __str__(self): # This customizes the return statement of the instance object of the class when called with the print() function (I think).
        return str(self.matrix)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})" # Note the use of !r to get the repr of the value
    
    def help(self):
        return "Here is your help!"

    def append(self, new_list, mode):
        self.mode = mode.lower()
        
        if mode in ["c", "col", "column", "columns"]:
            self.matrix = self.matrix + [new_list]
        elif mode in ["r", "row", "rows"]:
            self.matrix = [self.matrix[index] + [0] for index in range(len(self.matrix))]
        else:
            raise Exception("Please input 'rows' or 'columns'")
    
    @property
    def size(self):
        size = self.rows * self.columns
        return size
    
    def update(self, Number_of_Columns_and_Rows, value):
        self.matrix = self.matrix[Number_of_Columns_and_Rows]
        self.matrix = value
        
if __name__ == "__main__":
    import sys
    Matrix(int(sys.argv[1]))