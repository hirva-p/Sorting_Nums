
import streamlit as st
import pandas as pd

st.title("Sorting Numbers Simulation")
selectlist = ['Insertion Sort','Bubble Sort','Selection Sort']
result = st.selectbox('Select type of sort:',selectlist)

st.subheader(result)
array = []

with st.form("my_form"):
   text = st.text_input("Enter nums (space separated)",key = "real")
   submitted = st.form_submit_button("Submit")


arr = text.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

def insert(ar,temp):
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

def bubble(ar):
    p = len(ar)
    swapped  = False
    for i in range(p):
        temarr = []
        for k in range(len(ar)):
            temarr.append(ar[k])
        array.append(temarr)
        for j in range(0,p-i-1):
            if (ar[j]>ar[j+1]):
                swapped = True
                ar[j],ar[j+1] = ar[j+1],ar[j]
        if not swapped:
            array.append(ar)
            return

def select(ar,temp):
    for i in range(temp):
        min = i
        temarr = []
        for k in range(len(ar)):
            temarr.append(ar[k])
        array.append(temarr)
        for j in range(i+1,temp):
            if (ar[j]<ar[min]):
                min = j
        ar[i],ar[min] = ar[min],ar[i]
    temarr = []
    

n = len(arr)
st.session_state
if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0

if (result=='Insertion Sort'):
    arr = insert(arr,n-1)
    if (n>0):
        if st.button('Next'):
            st.session_state['cnt'] +=1
        if st.button('Prev'):
            st.session_state['cnt'] -= 1
        if (st.session_state['cnt']>=0 and st.session_state['cnt']<n):
            data = pd.DataFrame(array[st.session_state['cnt']])
            st.markdown("Sorted from index 0 to index "+str(st.session_state['cnt']))
            st.bar_chart(data)
        elif (st.session_state['cnt']<0):
            data = pd.DataFrame(array[0])
            st.markdown("Sorted from index 0 to index "+str(0))
            st.bar_chart(data)
            st.session_state['cnt'] = 0
        else:
            data = pd.DataFrame(array[n-1])
            st.markdown("Sorted from index 0 to index "+str(n-1))
            st.bar_chart(data)
            st.session_state['cnt'] = n-1

if (result=='Bubble Sort'):
    arr = bubble(arr)
    st.subheader("Iteration control")
    if (n>0):
        if st.button('Next'):
            st.session_state['cnt'] +=1
        if st.button('Prev'):
            st.session_state['cnt'] -= 1
        if (st.session_state['cnt']>=0 and st.session_state['cnt']<n-1):
            data = pd.DataFrame(array[st.session_state['cnt']])
            st.markdown("Iteration "+str(st.session_state['cnt']))
            st.bar_chart(data)
        elif (st.session_state['cnt']<0):
            data = pd.DataFrame(array[0])
            st.markdown("Iteration "+str(0))
            st.bar_chart(data)
            st.session_state['cnt'] = 0
        else:
            data = pd.DataFrame(array[n-1])
            st.markdown("Iteration "+str(n-1))
            st.bar_chart(data)
            st.session_state['cnt'] = n-1

if (result=='Selection Sort'):
    arr = select(arr,n)
    if (n>0):
        if st.button('Next'):
            st.session_state['cnt'] +=1
        if st.button('Prev'):
            st.session_state['cnt'] -= 1
        if (st.session_state['cnt']>=0 and st.session_state['cnt']<n):
            data = pd.DataFrame(array[st.session_state['cnt']])
            st.markdown("Iteration "+str(st.session_state['cnt']))
            st.bar_chart(data)
        elif (st.session_state['cnt']<0):
            data = pd.DataFrame(array[0])
            st.markdown("Iteration "+str(0))
            st.bar_chart(data)
            st.session_state['cnt'] = 0
        else:
            data = pd.DataFrame(array[n-1])
            st.markdown("Iteration "+str(n-1))
            st.bar_chart(data)
            st.session_state['cnt'] = n-1
