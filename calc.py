import streamlit as st
import numpy as np

# Matrix operation functions
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

def main():
    st.title("Matrix Operations Calculator")

    # User selects the operation first
    operation = st.sidebar.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Scalar Multiplication", "Transpose"])

    # Input fields for matrices
    matrix1_input = st.sidebar.text_area("Enter Matrix 1 (comma-separated rows, newline-separated):")
    scalar = None

    if operation != "Scalar Multiplication" and operation != "Transpose":
        matrix2_input = st.sidebar.text_area("Enter Matrix 2 (comma-separated rows, newline-separated):")

    if operation == "Scalar Multiplication":
        scalar = st.sidebar.number_input("Enter Scalar Value:")

    # Convert input text to NumPy arrays
    try:
        matrix1 = np.array([list(map(float, row.split(','))) for row in matrix1_input.split('\n') if row.strip()])
        
        if operation != "Scalar Multiplication" and operation != "Transpose":
            matrix2 = np.array([list(map(float, row.split(','))) for row in matrix2_input.split('\n') if row.strip()])

        if st.sidebar.button("Perform Operation"):
            if operation == "Addition":
                if matrix1.shape != matrix2.shape:
                    st.error("For addition, both matrices must have the same dimensions.")
                else:
                    st.table(add_matrices(matrix1, matrix2))

            elif operation == "Subtraction":
                if matrix1.shape != matrix2.shape:
                    st.error("For subtraction, both matrices must have the same dimensions.")
                else:
                    st.table(subtract_matrices(matrix1, matrix2))

            elif operation == "Multiplication":
                if matrix1.shape[1] != matrix2.shape[0]:
                    st.error("For multiplication, the number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
                else:
                    st.table(multiply_matrices(matrix1, matrix2))

            elif operation == "Scalar Multiplication":
                st.table(scalar_multiply(matrix1, scalar))

            elif operation == "Transpose":
                st.subheader("Transpose of Matrix 1:")
                st.table(transpose_matrix(matrix1))

    except ValueError:
        st.sidebar.error("Please ensure all matrix values are numeric and properly formatted.")

if __name__ == "__main__":
    main()
