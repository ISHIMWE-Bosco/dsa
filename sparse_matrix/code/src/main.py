from sparse_matrix import SparseMatrix

def main():
    # Prompt the user to select matrix operation (addition, subtraction, multiplication)
    operation = input("Enter the matrix operation (addition/subtraction/multiplication): ").strip().lower()

    # Load matrices from input files
    matrix1_file = "dsa/sparse_matrix/sample_inputs/input_matrix1.txt"
    matrix2_file = "dsa/sparse_matrix/sample_inputs/input_matrix2.txt"
    matrix1 = SparseMatrix(matrix_file_path=matrix1_file)
    matrix2 = SparseMatrix(matrix_file_path=matrix2_file)

    result = None

    # Perform the selected operation
    if operation == "addition":
        result = matrix1.add(matrix2)
        result_file = "result_addition.txt"
    elif operation == "subtraction":
        result = matrix1.subtract(matrix2)
        result_file = "result_subtraction.txt"
    elif operation == "multiplication":
        result = matrix1.multiply(matrix2)
        result_file = "result_multiplication.txt"
    else:
        print("Invalid operation. Please choose addition, subtraction, or multiplication.")
        return

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

