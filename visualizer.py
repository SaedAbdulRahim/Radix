import streamlit as st
import time

def draw_buckets(buckets, title=""):
    st.markdown(f"### {title}")
    cols = st.columns(len(buckets))
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"**Bucket {i}**")
            for val in buckets[i]:
                st.markdown(f"<div style='padding:4px; border-radius:4px; background-color:#f0f2f6; text-align:center'>{val}</div>", unsafe_allow_html=True)

def draw_array(arr, title="Array"):
    st.markdown(f"### {title}")
    cols = st.columns(len(arr))
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<div style='padding:8px; background-color:#e0f7fa; border-radius:6px; text-align:center'>{arr[i]}</div>", unsafe_allow_html=True)

def visualize_integer_sort(arr):
    st.subheader("🔢 Integer Radix Sort Visualization")
    draw_array(arr, "Original Array")

    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    step = 1

    while max_num // exp > 0:
        st.markdown(f"## Step {step}: Sorting by digit at exp = {exp}")
        buckets = [[] for _ in range(10)]

        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        draw_buckets(buckets, f"Buckets (exp={exp})")
        time.sleep(1)

        arr = [num for bucket in buckets for num in bucket]
        draw_array(arr, "Array After Collection")
        time.sleep(1)

        exp *= 10
        step += 1

    st.success("✅ Sorting complete!")
    return arr
