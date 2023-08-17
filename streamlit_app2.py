import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import time
from streamlit_autorefresh import st_autorefresh


st.title("Sorting Numbers Simulation")
selectlist = ["Insertion Sort", "Bubble Sort", "Selection Sort"]
result = st.selectbox("Select type of sort:", selectlist)

st.subheader(result)
array = []

with st.form("my_form"):
    text = st.text_input("Enter nums (space separated)", key="real")
    submitted = st.form_submit_button("Submit")


arr = text.split()
maxi = 0
size = 0
staten = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
    maxi = max(maxi, arr[i])
    size += 1


def insert(ar, temp):
    if temp == 0:
        return
    temarr = ar.copy()

    for i in range(1, temp + 1):
        key = ar[i]
        j = i - 1
        while (j >= 0) and key < ar[j]:
            ar[j + 1] = ar[j]
            ar[j] = key
            array.append([temarr, [j, j + 1]])
            temarr = ar.copy()
            j -= 1
        array.append([temarr, [j + 1, j + 1]])
        temarr = ar.copy()
    array.append([temarr, [-1, -1]])


def bubble(ar):
    p = len(ar)
    swapped = False
    for i in range(p):
        temarr = []
        for k in range(len(ar)):
            temarr.append(ar[k])
        array.append(temarr)
        for j in range(0, p - i - 1):
            if ar[j] > ar[j + 1]:
                swapped = True
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
        if not swapped:
            array.append(ar)
            return


def select(ar, temp):
    for i in range(temp):
        min = i
        temarr = []
        for k in range(len(ar)):
            temarr.append(ar[k])
        array.append(temarr)
        for j in range(i + 1, temp):
            if ar[j] < ar[min]:
                min = j
        ar[i], ar[min] = ar[min], ar[i]
    temarr = []


n = len(arr)

st.session_state
if "cnt" not in st.session_state:
    st.session_state["cnt"] = 0


def show_graph():
    if st.session_state["cnt"] >= 0 and st.session_state["cnt"] < staten:
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        index = []
        for i in range(size):
            index.append(i)
        ax.bar(index, array[st.session_state["cnt"]][0])
        for j, val in enumerate(array[st.session_state["cnt"]][0]):
            ax.text(j, val + 0.2, str(val), ha="center", va="bottom", color="black")
        ax.set_xlabel("Index")
        plt.ylim([0, maxi + 1])
        left = array[st.session_state["cnt"]][1][0]
        right = array[st.session_state["cnt"]][1][1]
        st.markdown("Swapping green values")
        if right != -1:
            ax.bar(right, array[st.session_state["cnt"]][0][right], color="green")
        if left != -1:
            ax.bar(left, array[st.session_state["cnt"]][0][left], color="green")
        plt.xticks(index)
        plt.yticks([])
        st.pyplot(fig)
    elif st.session_state["cnt"] < 0:
        st.session_state["cnt"] = 0
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        index =  []
        for i in range(size):
            index.append(i)
        ax.bar(index, array[st.session_state["cnt"]][0])
        for j, val in enumerate(array[st.session_state["cnt"]][0]):
            ax.text(j, val + 0.2, str(val), ha="center", va="bottom", color="black")
        ax.set_xlabel("Index")
        plt.ylim([0, maxi + 1])
        left = array[st.session_state["cnt"]][1][0]
        right = array[st.session_state["cnt"]][1][1]

        st.markdown("Swapping green values")
        if right != -1:
            ax.bar(right, array[st.session_state["cnt"]][0][right], color="green")
        if left != -1:
            ax.bar(left, array[st.session_state["cnt"]][0][left], color="green")
        plt.xticks(index)
        plt.yticks([])
        st.pyplot(fig)
    else:
        st.session_state["cnt"] = staten - 1
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        index = []
        for i in range(size):
            index.append(i)
        ax.bar(index, array[st.session_state["cnt"]][0])
        for j, val in enumerate(array[st.session_state["cnt"]][0]):
            ax.text(j, val + 0.2, str(val), ha="center", va="bottom", color="black")

        ax.set_xlabel("Index")
        plt.ylim([0, maxi + 1])
        left = array[st.session_state["cnt"]][1][0]
        right = array[st.session_state["cnt"]][1][1]

        st.markdown("Swapping green values")
        if right != -1:
            ax.bar(right, array[st.session_state["cnt"]][0][right], color="green")
        if left != -1:
            ax.bar(left, array[st.session_state["cnt"]][0][left], color="green")
        plt.xticks(index)
        plt.yticks([])
        st.pyplot(fig)


placeholder = st.empty()


def call_func():
    st.session_state["cnt"] = 0
    st.session_state["cnt"] = st_autorefresh(interval=1500, limit=staten)
    show_graph()


if result == "Insertion Sort":
    arr = insert(arr, n - 1)
    staten = len(array)
    if staten > 0:
        if st.button("auto"):
            st.session_state["cnt"] = 0
        if st.button("Next"):
            st.session_state["cnt"] += 1
        if st.button("Prev"):
            st.session_state["cnt"] -= 1
        call_func()


if result == "Bubble Sort":
    arr = bubble(arr)
    st.subheader("Iteration control")
    if n > 0:
        if st.button("Next"):
            st.session_state["cnt"] += 1
        if st.button("Prev"):
            st.session_state["cnt"] -= 1
        if st.session_state["cnt"] >= 0 and st.session_state["cnt"] < n - 1:
            data = pd.DataFrame(array[st.session_state["cnt"]])
            st.markdown("Iteration " + str(st.session_state["cnt"]))
            st.bar_chart(data)
        elif st.session_state["cnt"] < 0:
            data = pd.DataFrame(array[0])
            st.markdown("Iteration " + str(0))
            st.bar_chart(data)
            st.session_state["cnt"] = 0
        else:
            data = pd.DataFrame(array[n - 1])
            st.markdown("Iteration " + str(n - 1))
            st.bar_chart(data)
            st.session_state["cnt"] = n - 1

if result == "Selection Sort":
    arr = select(arr, n)
    if n > 0:
        if st.button("Next"):
            st.session_state["cnt"] += 1
        if st.button("Prev"):
            st.session_state["cnt"] -= 1
        if st.session_state["cnt"] >= 0 and st.session_state["cnt"] < n:
            data = pd.DataFrame(array[st.session_state["cnt"]])
            st.markdown("Iteration " + str(st.session_state["cnt"]))
            st.bar_chart(data)
        elif st.session_state["cnt"] < 0:
            data = pd.DataFrame(array[0])
            st.markdown("Iteration " + str(0))
            st.bar_chart(data)
            st.session_state["cnt"] = 0
        else:
            data = pd.DataFrame(array[n - 1])
            st.markdown("Iteration " + str(n - 1))
            st.bar_chart(data)
            st.session_state["cnt"] = n - 1
