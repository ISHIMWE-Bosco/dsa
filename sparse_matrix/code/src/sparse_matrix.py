class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        self.rows = num_rows
        self.cols = num_cols
        self.matrix = {}

        if matrix_file_path:
            self.load_from_file(matrix_file_path)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith('rows='):
                    self.rows = int(line.strip().split('=')[1])
                elif line.startswith('cols='):
                    self.cols = int(line.strip().split('=')[1])
                else:
                    parts = line.strip().replace('(', '').replace(')', '').split(',')
                    row = int(parts[0])
                    col = int(parts[1])
                    value = int(parts[2])
                    self.set_element(row, col, value)

    def get_element(self, curr_row, curr_col):
        return self.matrix.get((curr_row, curr_col), 0)

    def set_element(self, curr_row, curr_col, value):
        if value != 0:
            self.matrix[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.matrix:
            del self.matrix[(curr_row, curr_col)]

    def add(self, other_matrix):
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)

        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value + other_matrix.get_element(row, col))

        for (row, col), value in other_matrix.matrix.items():
            result.set_element(row, col, value + self.get_element(row, col))

        return result

    def subtract(self, other_matrix):
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)

        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value - other_matrix.get_element(row, col))

        for (row, col), value in other_matrix.matrix.items():
            result.set_element(row, col, self.get_element(row, col) - value)

        return result

    def multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result = SparseMatrix(num_rows=self.rows, num_cols=other_matrix.cols)

        for i in range(self.rows):
            for j in range(other_matrix.cols):
                value = 0
                for k in range(self.cols):
                    value += self.get_element(i, k) * other_matrix.get_element(k, j)
                result.set_element(i, j, value)

        return result

