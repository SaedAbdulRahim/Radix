import streamlit as st
from algorithm import radix_sort_integers, radix_sort_strings
from utils import display_buckets, get_buckets_integers, get_buckets_strings

st.title("🔢 Radix Sort Visualization")
mode = st.radio("Select mode", ["Integer", "String"])

if mode == "Integer":
    raw = st.text_input("Enter integers (comma-separated)", "170, 45, 75, 90, 802, 24, 2, 66")
    arr = [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]
    
    if st.button("Visualize Sort"):
        max_length = len(str(max(arr)))
        for digit in range(max_length):
            st.write(f"### Pass {digit + 1} (Digit: {10**digit})")
            buckets = get_buckets_integers(arr, digit)
            display_buckets(buckets)
            arr = [num for bucket in buckets for num in bucket]
        st.success(f"Sorted: {arr}")

else:
    raw = st.text_input("Enter strings (comma-separated)", "apple, dog, banana, cat, ball")
    arr = [x.strip() for x in raw.split(",") if x.strip()]
    
    if st.button("Visualize Sort"):
        max_length = max(len(word) for word in arr)
        for char_index in reversed(range(max_length)):
            st.write(f"### Pass {max_length - char_index} (Char index: {char_index})")
            buckets = get_buckets_strings(arr, char_index)
            display_buckets(buckets)
            arr = [word for bucket in buckets for word in bucket]
        st.success(f"Sorted: {arr}")
