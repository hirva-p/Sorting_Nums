
import streamlit as st
# import matplotlib.pyplot as plt
import pandas as pd

st.title("Sorting Numbers Simulation")
array = []
with st.form("my_form"):
   text = st.text_input("Enter nums(space)",key = "real")
   submitted = st.form_submit_button("Submit")
   
arr = text.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

def func(ar,temp):
    if (temp==0): 
        return
    for i in range(1,temp+1):
        temarr = []
        for k in range(len(ar)):
            temarr.append(ar[k])
        array.append(temarr)
        key = ar[i]
        j = i-1
        while (j>=0) and key<ar[j]:
            ar[j+1] = ar[j]
            j-=1
        ar[j+1] = key
    array.append(ar)

n = len(arr)
arr = func(arr,n-1)
st.subheader("Iteration control")
temp_options = list(range(0,n))
temp = st.select_slider("Choose iteration",options=temp_options)

data = pd.DataFrame(array[temp])
st.markdown("Sorted from index 0 to index "+str(temp))

st.bar_chart(data)
