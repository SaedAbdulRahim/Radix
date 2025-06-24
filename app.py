import streamlit as st
from algorithm import radix_sort_integers, radix_sort_strings
from visualizer import visualize_integer_sort, visualize_string_sort
from utils import validate_integer_list, validate_string_list

st.title("Radix Sort Visualizer")

input_type = st.radio("Select input type:", ("Integers", "Strings"))
user_input = st.text_input("Enter a list (comma-separated):")

if user_input:
    input_list = [x.strip() for x in user_input.split(",")]
    if input_type == "Integers":
        try:
            arr = validate_integer_list(input_list)
            sorted_arr = visualize_integer_sort(arr)
            st.success(f"Sorted: {sorted_arr}")
        except ValueError as e:
            st.error(str(e))
    else:
        try:
            arr = validate_string_list(input_list)
            sorted_arr = visualize_string_sort(arr)
            st.success(f"Sorted: {sorted_arr}")
        except ValueError as e:
            st.error(str(e))
