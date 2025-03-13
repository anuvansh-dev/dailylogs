import streamlit as st 
import requests
import time

BASE_URL  = "http://127.0.0.1:8000/api/auth/"

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        response = requests.post(f"{BASE_URL}login/", json={"username": username, "password": password})
        if response.status_code == 200:
            data = response.json()
            st.session_state["token"] = data["tokens"]["access"]
            st.session_state["refresh"] = data["tokens"]["refresh"]
            st.session_state["user"] = data["user"]
            st.success(f"Welcome, {data['user']['username']}!")
            time.sleep(1)
            st.rerun()
        else:
            st.error(f'Login Failed {response.text}')
            
    
def register():
    st.title('Register')
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        response = requests.post(f"{BASE_URL}register/", json={"username": username, "email": email, "password": password})
        if response.status_code == 201:
            st.success("User registered successfully!")
        else:
            st.error(f"Registration failed: {response.text}")
            

def main():
    if "token" not in st.session_state:
        page = st.sidebar.radio("Choose", ["Login", "Register"])
        if page == "Login":
            login()
        else:
            register()
    
    else:
        st.write(f"Hello, {st.session_state['user']['username']}!")
        if st.button("Logout"):
            st.session_state.clear()
            st.success("Logged out!")
            time.sleep(1)
            st.rerun()
            
if __name__ == "__main__":
    main()
            
    