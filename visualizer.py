import streamlit as st
import time

def draw_buckets(buckets, title=""):
    st.markdown(f"### {title}")
    cols = st.columns(len(buckets))
    for i, col in enumerate(cols):
        with col:
            col.markdown(f"**Bucket {i}**")
            if not buckets[i]:
                col.markdown("*Empty*")
            for val in buckets[i]:
                col.markdown(f"<div style='padding:6px; margin:4px 0; background-color:#f1f3f5; border-radius:6px; text-align:center'>{str(val)}</div>", unsafe_allow_html=True)

def draw_array(arr, title="Array"):
    st.markdown(f"### {title}")
    if not arr:
        st.warning("Array is empty.")
        return
    cols = st.columns(len(arr))
    for i, col in enumerate(cols):
        col.markdown(f"<div style='padding:10px; background-color:#e0f7fa; border-radius:6px; text-align:center; font-weight:bold'>{str(arr[i])}</div>", unsafe_allow_html=True)

def visualize_integer_sort(arr):
    st.subheader("🔢 Integer Radix Sort Visualization")
    draw_array(arr, "Original Array")

    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    step = 1

    while max_num // exp > 0:
        st.markdown(f"## Step {step}: Sorting by digit (exp = {exp})")
        buckets = [[] for _ in range(10)]

        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        draw_buckets(buckets, f"Buckets for exp={exp}")
        time.sleep(1)

        arr = [num for bucket in buckets for num in bucket]
        draw_array(arr, "Array After Re-collection")
        time.sleep(1)

        exp *= 10
        step += 1

    st.success("✅ Sorting complete!")
    return arr
