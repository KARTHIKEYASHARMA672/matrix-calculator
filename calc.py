import streamlit as st
import numpy as np

# Define matrix operations
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

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse_matrix(matrix):
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "Matrix is singular (non-invertible)."

# Streamlit app
def main():
    st.title("2x2 and 3x3 Matrix Operations Calculator")

    # Sidebar inputs
    st.sidebar.header("Matrix Inputs")
    matrix_size = st.sidebar.radio("Select Matrix Size:", ["2x2", "3x3"])
    
    # Input matrix entries
    matrix1_input = st.sidebar.text_area("Enter Matrix 1 (comma-separated rows):")
    matrix2_input = st.sidebar.text_area("Enter Matrix 2 (comma-separated rows):")
    scalar = st.sidebar.number_input("Enter Scalar Value:", value=1)

    # Convert input strings to NumPy arrays
    def parse_matrix_input(matrix_input):
        return np.array([list(map(float, row.split(','))) for row in matrix_input.split('\n') if row.strip()])

    if st.sidebar.button("Perform Operations"):
        try:
            matrix1 = parse_matrix_input(matrix1_input)
            matrix2 = parse_matrix_input(matrix2_input)

            # Validate matrix size
            if matrix1.shape != matrix2.shape or matrix1.shape[0] != matrix1.shape[1]:
                st.error(f"Both matrices must be square and of size {matrix_size}.")
                return
            
            # Perform operations
            result_addition = add_matrices(matrix1, matrix2)
            result_subtraction = subtract_matrices(matrix1, matrix2)
            result_multiplication = multiply_matrices(matrix1, matrix2)
            result_scalar_multiply1 = scalar_multiply(matrix1, scalar)
            result_scalar_multiply2 = scalar_multiply(matrix2, scalar)
            result_transpose1 = transpose_matrix(matrix1)
            result_transpose2 = transpose_matrix(matrix2)
            det1 = determinant(matrix1)
            det2 = determinant(matrix2)
            inv1 = inverse_matrix(matrix1)
            inv2 = inverse_matrix(matrix2)

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

            st.subheader(f"Scalar Multiplication ({scalar}) for Matrix 1:")
            st.table(result_scalar_multiply1)

            st.subheader(f"Scalar Multiplication ({scalar}) for Matrix 2:")
            st.table(result_scalar_multiply2)

            st.subheader("Transpose of Matrix 1:")
            st.table(result_transpose1)

            st.subheader("Transpose of Matrix 2:")
            st.table(result_transpose2)

            st.subheader("Determinant of Matrix 1:")
            st.write(det1)

            st.subheader("Determinant of Matrix 2:")
            st.write(det2)

            st.subheader("Inverse of Matrix 1:")
            st.table(inv1 if isinstance(inv1, np.ndarray) else inv1)

            st.subheader("Inverse of Matrix 2:")
            st.table(inv2 if isinstance(inv2, np.ndarray) else inv2)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
