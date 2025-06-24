import streamlit as st

def display_buckets(buckets):
    st.write("### Buckets")
    cols = st.columns(len(buckets))
    for i, bucket in enumerate(buckets):
        with cols[i]:
            st.write(f"**{i}**")
            for item in bucket:
                st.write(item)

def get_buckets_integers(arr, digit):
    buckets = [[] for _ in range(10)]
    for num in arr:
        index = (num // 10**digit) % 10
        buckets[index].append(num)
    return buckets

def get_buckets_strings(arr, char_index):
    buckets = [[] for _ in range(27)]
    for word in arr:
        char = word[char_index] if char_index < len(word) else ' '
        index = 0 if char == ' ' else ord(char.lower()) - 96
        buckets[index].append(word)
    return buckets
