import streamlit as st
import numpy as np

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
    
def elementwise_multiply(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def main():
    st.title("Matrix Operations Calculator")

    st.sidebar.header("Matrix Inputs")

    matrix1_input = st.sidebar.text_area("Enter Matrix 1 (comma-separated rows):")
    matrix2_input = st.sidebar.text_area("Enter Matrix 2 (comma-separated rows):")
    scalar = st.sidebar.number_input("Enter Scalar Value:", value=1)

    def parse_matrix_input(matrix_input):
        try:
            return np.array([list(map(float, row.split(','))) for row in matrix_input.strip().split('\n') if row.strip()])
        except ValueError:
            st.error("Invalid matrix format. Ensure all values are numbers and rows are comma-separated.")
            return None

    matrix1 = parse_matrix_input(matrix1_input)
    matrix2 = parse_matrix_input(matrix2_input)

    if st.sidebar.button("Perform Operations"):
        if matrix1 is not None and matrix2 is not None:
            st.subheader("Results:")
            st.write("Matrix 1:")
            st.table(matrix1)

            st.write("Matrix 2:")
            st.table(matrix2)

 
            if matrix1.shape == matrix2.shape:
                st.subheader("Matrix Addition:")
                st.table(add_matrices(matrix1, matrix2))

                st.subheader("Matrix Subtraction:")
                st.table(subtract_matrices(matrix1, matrix2))
            else:
                st.error("Addition and subtraction skipped: Matrices must have the same dimensions.")

        
            if matrix1.shape[1] == matrix2.shape[0]:
                st.subheader("Matrix Multiplication:")
                st.table(multiply_matrices(matrix1, matrix2))
            else:
                st.error("Matrix multiplication skipped: The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")

           
            st.subheader(f"Scalar Multiplication (Matrix 1 × {scalar}):")
            st.table(scalar_multiply(matrix1, scalar))

            st.subheader(f"Scalar Multiplication (Matrix 2 × {scalar}):")
            st.table(scalar_multiply(matrix2, scalar))

            
            st.subheader("Transpose of Matrix 1:")
            st.table(transpose_matrix(matrix1))

            st.subheader("Transpose of Matrix 2:")
            st.table(transpose_matrix(matrix2))
        else:
            st.error("Please enter valid matrices.")

if __name__ == "__main__":
    main()
