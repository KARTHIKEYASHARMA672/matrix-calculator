import streamlit as st
import numpy as np

# Function definitions
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def scalar_multiply(matrix, scalar):
    return np.multiply(matrix, scalar)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

# Function to process user input safely
def parse_matrix(matrix_str):
    try:
        matrix = np.array([list(map(int, row.split(','))) for row in matrix_str.split('\n') if row.strip()])
        return matrix
    except ValueError:
        return None

def main():
    st.title("Square Matrix Operations Calculator")
    
    st.sidebar.header("Matrix Input")
    matrix1_str = st.sidebar.text_area("Enter Matrix 1 (comma-separated values, each row on a new line):")
    matrix2_str = st.sidebar.text_area("Enter Matrix 2 (comma-separated values, each row on a new line):")
    scalar = st.sidebar.number_input("Enter Scalar Value:", value=1)

    if st.sidebar.button("Perform Operations"):
        matrix1 = parse_matrix(matrix1_str)
        matrix2 = parse_matrix(matrix2_str)

        # Input validation
        if matrix1 is None or matrix2 is None:
            st.error("Invalid input! Ensure all matrix entries are integers and formatted correctly.")
            return
        
        if not (is_square(matrix1) and is_square(matrix2)):
            st.error("Both matrices must be square for this calculator.")
            return

        if matrix1.shape != matrix2.shape:
            st.error("Matrices must be of the same dimensions for addition and subtraction.")
            return

        try:
            # Perform operations
            result_addition = add_matrices(matrix1, matrix2)
            result_subtraction = subtract_matrices(matrix1, matrix2)
            result_multiplication = multiply_matrices(matrix1, matrix2)
            result_scalar_multiply_for_1 = scalar_multiply(matrix1, scalar)
            result_scalar_multiply_for_2 = scalar_multiply(matrix2, scalar)
            result_transpose_for_1 = transpose_matrix(matrix1)
            result_transpose_for_2 = transpose_matrix(matrix2)

            # Display results
            st.subheader("Results:")

            st.write("Matrix 1:")
            st.table(matrix1)

            st.write("Matrix 2:")
            st.table(matrix2)

            st.subheader("Matrix Addition:")
            st.table(result_addition)

            st.subheader("Matrix Subtraction:")
            st.table(result_subtraction)

            st.subheader("Matrix Multiplication:")
            st.table(result_multiplication)

            st.subheader(f"Scalar Multiplication with {scalar} (Matrix 1):")
            st.table(result_scalar_multiply_for_1)

            st.subheader(f"Scalar Multiplication with {scalar} (Matrix 2):")
            st.table(result_scalar_multiply_for_2)

            st.subheader("Transpose of Matrix 1:")
            st.table(result_transpose_for_1)

            st.subheader("Transpose of Matrix 2:")
            st.table(result_transpose_for_2)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
