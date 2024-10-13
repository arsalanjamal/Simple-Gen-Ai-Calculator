!pip install streamlit
import streamlit as st

# Functions for the calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

# Streamlit app layout
def calculator():
    st.title("Simple Calculator (built by arsalan jamal)")

    # Input: two numbers
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    # Select operation
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform calculation based on operation
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        st.write(f"Result: {result}")

# Call the calculator function to render the app
if __name__ == "__main__":
    calculator()
    
streamlit run app.py
