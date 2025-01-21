import streamlit as st
import functions as funcs


todos = funcs.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    funcs.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app")

st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        funcs.write_todos(todos)
        del st.session_state[todo]
        st.rerun(scope="app")
        #print("reurn")


st.text_input(label="temp", label_visibility="hidden", placeholder="Add new todo...", on_change=add_todo,
              key='new_todo')

#st.session_state