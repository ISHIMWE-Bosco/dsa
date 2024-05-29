from sparse_matrix import SparseMatrix
import os

def main():
    # Prompt the user to select matrix operation (addition, subtraction, multiplication)
    operation = input("Enter the matrix operation (addition/subtraction/multiplication): ").strip().lower()

    if operation not in {"addition", "subtraction", "multiplication"}:
        print("Invalid operation. Please choose addition, subtraction, or multiplication.")
        return

    # Define the correct paths for the input files
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../sample_inputs/'))
    matrix1_file = os.path.join(base_path, "input_matrix1.txt")
    matrix2_file = os.path.join(base_path, "input_matrix2.txt")

    # Load matrices from input files
    try:
        matrix1 = SparseMatrix(matrix_file_path=matrix1_file)
        matrix2 = SparseMatrix(matrix_file_path=matrix2_file)
    except FileNotFoundError as e:
        print("Error: {}".format(e))
        return

    result = None
    result_file = ""

    # Perform the selected operation
    if operation == "addition":
        result = matrix1.add(matrix2)
        result_file = os.path.join(base_path, "result_addition.txt")
    elif operation == "subtraction":
        result = matrix1.subtract(matrix2)
        result_file = os.path.join(base_path, "result_subtraction.txt")
    elif operation == "multiplication":
        result = matrix1.multiply(matrix2)
        result_file = os.path.join(base_path, "result_multiplication.txt")

    # Output the result to a file
    if result:
        with open(result_file, "w") as f:
            f.write("rows={}\n".format(result.rows))
            f.write("cols={}\n".format(result.cols))
            for (row, col), value in result.matrix.items():
                f.write("({}, {}, {})\n".format(row, col, value))

        print("Result has been saved in '{}'.".format(result_file))

if __name__ == "__main__":
    main()

