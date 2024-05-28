import os

class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = {}
        
        if matrix_file_path:
            self.read_from_file(matrix_file_path)

    def read_from_file(self, matrix_file_path):
        try:
            with open(matrix_file_path, 'r') as file:
                lines = file.readlines()
        except IOError:
            raise IOError("File not found: {}".format(matrix_file_path))
        
        try:
            self.num_rows = int(lines[0].strip().split('=')[1])
            self.num_cols = int(lines[1].strip().split('=')[1])
        except (IndexError, ValueError):
            raise ValueError("Input file has wrong format")
        
        for line in lines[2:]:
            line = line.strip()
            if not line:
                continue

            if not self.validate_line(line):
                raise ValueError("Input file has wrong format")
            
            row, col, value = self.parse_line(line)
            self.set_element(row, col, value)

    def validate_line(self, line):
        if not (line.startswith('(') and line.endswith(')')):
            return False
        parts = line[1:-1].split(',')
        if len(parts) != 3:
            return False
        try:
            int(parts[0].strip())
            int(parts[1].strip())
            int(parts[2].strip())
        except ValueError:
            return False
        return True

    def parse_line(self, line):
        parts = line[1:-1].split(',')
        row = int(parts[0].strip())
        col = int(parts[1].strip())
        value = int(parts[2].strip())
        return row, col, value

    def get_element(self, row, col):
        return self.matrix.get(row, {}).get(col, 0)

    def set_element(self, row, col, value):
        if value != 0:
            if row not in self.matrix:
                self.matrix[row] = {}
            self.matrix[row][col] = value
        else:
            if row in self.matrix and col in self.matrix[row]:
                del self.matrix[row][col]
                if not self.matrix[row]:
                    del self.matrix[row]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for row in self.matrix:
            for col in self.matrix[row]:
                result.set_element(row, col, self.get_element(row, col))
        
        for row in other.matrix:
            for col in other.matrix[row]:
                result.set_element(row, col, result.get_element(row, col) + other.get_element(row, col))
        
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for row in self.matrix:
            for col in self.matrix[row]:
                result.set_element(row, col, self.get_element(row, col))
        
        for row in other.matrix:
            for col in other.matrix[row]:
                result.set_element(row, col, result.get_element(row, col) - other.get_element(row, col))
        
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for row in self.matrix:
            for col in self.matrix[row]:
                if col in other.matrix:
                    for k in other.matrix[col]:
                        result.set_element(row, k, result.get_element(row, k) + self.get_element(row, col) * other.get_element(col, k))
        
        return result

def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        raise IOError("File not found: {}".format(file_path))

# Example usage
if __name__ == "__main__":
    try:
        # Provide the correct path to the matrix files
        matrix1_path = "/dsa/sparse_matrix/sample_inputs/input1.txt"
        matrix2_path = "/dsa/sparse_matrix/sample_inputs/input2.txt"
        matrix3_path = "/dsa/sparse_matrix/sample_inputs/input3.txt"

        # Check if files exist
        check_file_exists(matrix1_path)
        check_file_exists(matrix2_path)
        check_file_exists(matrix3_path)

        matrix1 = SparseMatrix(matrix1_path)
        matrix2 = SparseMatrix(matrix2_path)
        matrix3 = SparseMatrix(matrix3_path)

        print("Matrix 1: {} x {}".format(matrix1.num_rows, matrix1.num_cols))
        print("Matrix 2: {} x {}".format(matrix2.num_rows, matrix2.num_cols))
        print("Matrix 3: {} x {}".format(matrix3.num_rows, matrix3.num_cols))

        # Perform addition, subtraction, and multiplication if dimensions are correct
        try:
            result_add = matrix1.add(matrix2)
            print("Addition result:")
            print(result_add.matrix)  # Example of printing the internal representation
        except ValueError as e:
            print(e)

        try:
            result_subtract = matrix1.subtract(matrix2)
            print("Subtraction result:")
            print(result_subtract.matrix)  # Example of printing the internal representation
        except ValueError as e:
            print(e)

        try:
            result_multiply = matrix1.multiply(matrix3)
            print("Multiplication result:")
            print(result_multiply.matrix)  # Example of printing the internal representation
        except ValueError as e:
            print(e)

    except IOError as e:
        print(e)
    except ValueError as e:
        print(e)

