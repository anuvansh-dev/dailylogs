import streamlit as st 
import requests
import time
import pandas as pd
import plotly.express as px
from transformers import pipeline

# Base API URL
BASE_URL = "http://127.0.0.1:8000/api"

# Authentication
def check_login():
    """ Check if the user us logged in by checking session state """
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        
        
def login_user():
    """ Handle user login via Django's login API """
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    

    if st.button("Login"):
        print(f"Username: {username}, Password: {password}")
        response = requests.post(f"{BASE_URL}/login/", json={"username": username, "password": password})
        
        # st.write("DEBUG:", response.status_code, response.text)

        if response.status_code == 200:
            data = response.json()
            st.session_state["token"] = data.get("token") # Store token
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            # time.sleep(1)
            st.rerun()
        else:
            st.error(f"Login Failed: {response.json()}")


def register_user():
    """ Handle user registration via Django's registration API """
    st.title("Register")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Conifrm Password", type="password")
    
    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        else:
            # Making API request to register
            response = requests.post(f"{BASE_URL}/users/", json={
                "username": username,
                "password": password,
            })
            if response.status_code == 201:
                st.success(f"User registered successfully!")
            else:
                st.error(f"Error: {response.json()}")
                

# Function to fetch projects with "Voting Open" status
def get_voting_projects():
    token = st.session_state.get("token")
    if not token:
        st.error("You are not logged in. Please log in first.")
        return []
    
    headers = {
        "Authorization": f"Token {token}" 
    }
    
    response = requests.get(f"{BASE_URL}/projects/", headers=headers)
    
    if response.status_code == 200:
        projects = response.json()
        return {f"{p['name']} - {p['description']}": p['id'] for p in projects if p['status'] == 'Voting Open'}
    else:
        st.error(f"Failed to fetch voting projects. Status: {response.status_code}, Error: {response.text}")
        return []


# Function to check if user has already voted
def user_already_voted():
    token = st.session_state.get("token")
    if not token:
        return False
    
    headers = {"Authorization": f"Token {token}"}
    
    response = requests.get(f"{BASE_URL}/projects/", headers=headers)
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            if project["status"] == "Voting Open":
                vote_check = requests.get(f"{BASE_URL}/projects/{project['id']}/vote/", headers=headers)
                if vote_check.status_code == 200:
                    has_voted = vote_check.json().get("has_voted", False)
                    return has_voted
    return False


# Function to vote for a project
def submit_vote(project_id):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to be logged in to submit vote")
        return 
    
    headers = {"Authorization": f"Token {token}"}
    
    response = requests.post(f"{BASE_URL}/projects/{project_id}/vote/", headers=headers)
    
    if response.status_code == 201:
        st.success("Vote recorded successfully!")
    else:
        st.error(response.json().get("error", "Failed to vote."))
        
        
# Function to fetch active project
def get_active_project():
    token = st.session_state.get("token")
    if not token:
        st.error("You are not logged in. Please log in first.")
        return None
    
    headers = {"Authorization": f"Token {token}"}
    
    response = requests.get(f"{BASE_URL}/projects/active_project/", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return None


# Function to submit feedback for a project
def submit_feedback(project_id, rating, comments):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to be logged in to submit feedback.")
        return 
    
    headers = {"Authorization": f"Token {token}"}
    
    feedback_data = {"project": project_id, "rating": rating, "comments": comments}
    response = requests.post(f"{BASE_URL}/feedback/", json=feedback_data, headers=headers)
    if response.status_code == 201:
        st.success("Feedback submitted successfully!")
    else:
        st.error(response.json().get("error", "Failed to submit feedback."))
        

def submit_request_feedback(facility_req_id, rating, comments):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to be logged in to submit feedback.")
        return 
    
    headers = {"Authorization": f"Token {token}"}
    
    feedback_data = {"facility_request": facility_req_id, "rating": rating, "comments": comments}
    response = requests.post(f"{BASE_URL}/feedback/", json=feedback_data, headers=headers)
    if response.status_code == 201:
        st.success("Feedback submitted successfully!")
    else:
        st.error(response.json().get("error", "Failed to submit feedback."))    

        
# Function to submit a facility request (user)
def raise_request(category, description):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to be logged in to raise facility requests.")
    
    headers = {"Authorization": f"Token {token}"}
    
    request_data = {"category": category, "description": description}
    response = requests.post(f"{BASE_URL}/facility-requests/", json=request_data, headers=headers)
    if response.status_code == 201:
        st.success("Request submitted successfully!")
    else:
        st.error(f"The request cannot be submitted!, {response.status_code}: {response.text}")
        
        
# Function to fetch facility requests
def get_facility_requests():
    token = st.session_state.get("token")
    
    if not token:
        st.error("You are not logged in, you need to login first.")
        return []
    
    headers = {"Authorization": f"Token {token}"} 
    
    response = requests.get(f"{BASE_URL}/facility-requests/", headers=headers)
    facility_requests = response.json()
    
    return facility_requests
    
    
# Function to show facility requests filtered by the user
def show_user_facility_requests():
    st.title("My Facility Requests")
    
    facility_requests = get_facility_requests()
    
    if facility_requests:
        for req in facility_requests: 
            with st.expander(f"Request ID: {req['id']} - {req['category']}"):
                st.write(f"**Description:** {req['description']}")
                st.write(f"**Status:** {req['status']}")
                st.write(f"**Created At:** {req['created_at']}")
                # Feedback functionality for completed requests
                if req['status'] == 'Completed': 
                    # Checking if the feedback already exists for the request
                    if req.get('feedback'):
                        st.success("Feedback Submitted!")
                        st.write(f"**Rating:** {req['feedback']['rating']}/5")
                        st.write(f"**Comments:** {req['feedback']['comments']}")
                    else:    
                        st.markdown("### Give Feedback")
                        rating = st.slider("rating (1-5)", 1, 5, 3, key=f"rating_{req['id']}")
                        comments = st.text_area("Comments", key=f"comments_{req['id']}")
                        if st.button("Submit Feedback", key=f"submit_feedback_{req['id']}"):
                            if comments.strip():
                                submit_request_feedback(req["id"], rating, comments)
                                st.rerun()
                            else:
                                st.warning("Comments cannot be empty!")                            
    else:
        st.info("You have not submitted any facility requests yet.")
        
    st.subheader("Raise a New Facility Request")
    category = st.selectbox("Select Category", ['Roads', 'Water Supply', 'Electricity', 'Parks', 'Cleaning', 'Other'])
    description = st.text_area("Describe the issue")
    if st.button("Submit Request"):
        raise_request(category, description)
     
        
# **Admin functionalities**
        
# Function to update status of requests for admins
def update_facility_status(request_id, new_status):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
        return 
    
    headers = {"Authorization": f"Token {token}"}
    data = {"status": new_status}
    
    response = requests.patch(f"{BASE_URL}/facility-requests/{request_id}/", json=data, headers=headers)
    
    if response.status_code == 200:
        st.success("Status updated successfully!")
        time.sleep(1)
        st.rerun()
    else:
        st.error(f"Failed to update status:{response.status_code} - {response.text}")

      
# Project management for admins
# Function to fetch all the projects
def get_projects():
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
        
    headers = {'Authorization': f"Token {token}"}
    
    response = requests.get(f"{BASE_URL}/projects/", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch projects!, {response.status_code} - {response.text}")
        return []
    
    
# Function to update the status of an existing project   
def update_project_status(id, new_status):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
        return
    
    headers = {"Authorization": f"Token {token}"}
    
        # If marking a project as Active, discard all other "Voting Open" projects
    if new_status == "Active":
        response = requests.get(f"{BASE_URL}/projects/", headers=headers)
        if response.status_code == 200:
            all_projects = response.json()
            for project in all_projects:
                if project["status"] == "Voting Open" and project["id"] != id:
                    requests.patch(f"{BASE_URL}/projects/{project['id']}/", json={"status": "Discarded"}, headers=headers)
    
    response = requests.patch(f"{BASE_URL}/projects/{id}/",json={"status": new_status}, headers=headers)
    if response.status_code == 200:
        st.success("Status updated sucecssfully!")
        time.sleep(1)
        st.rerun()
    else:
        st.error(f"Failed to update status!, {response.status_code} - {response.text}")
        

# Function to add a new project
def add_project(name, description):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
    
    headers = {"Authorization": f"Token {token}"}
    data = {"name": name, "description": description}
    
    response = requests.post(f"{BASE_URL}/projects/",json=data, headers=headers)
    if response.status_code == 201:
        st.success("Project added successfully!")
    else:
        st.error(f"Failed to add project, {response.status_code} - {response.text}")


# Function to delete an exisitng project
def delete_project(id):
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
        return
    
    headers = {"Authorization": f"Token {token}"}
    
    response = requests.delete(f"{BASE_URL}/projects/{id}/", headers=headers)
    if response.status_code == 204:
        st.success("Project deleted successfully!")
        st.rerun()
    else:
        st.error(f"Failed to delete the project, {response.status_code} - {response.text}")


# Function to show the list of projects and add project functionality
def show_projects():
    st.title("Project Management")

    col1, col2 = st.columns([4, 1])  

    # with col1:
    #     st.subheader("")

    with col2:
        if st.button("➕ Add Project", use_container_width=True):
            st.session_state["show_add_form"] = not st.session_state.get("show_add_form", False)

    # Show Add Project Form 
    if st.session_state.get("show_add_form", False):
        st.markdown("---")
        st.subheader("Add New Project")
        name = st.text_input("Project Name", key="new_project_name")
        description = st.text_area("Project Description", key="new_project_desc")

        if st.button("Submit Project", key="submit_project_btn"):
            if name and description:
                add_project(name, description)
            else:
                st.warning("Please provide both name and description.")

    projects = get_projects()

    if not projects:
        st.warning("No projects available.")
        return

    # Categorized projects into sections
    active_projects = []
    voting_open_projects = []
    discarded_projects = []
    completed_projects = []

    for project in projects:
        if project["status"] == "Active":
            active_projects.append(project)
        elif project["status"] == "Voting Open":
            voting_open_projects.append(project)
        elif project["status"] == "Discarded":
            discarded_projects.append(project)
        elif project["status"] == "Completed":
            completed_projects.append(project)

    # Display Active Projects Section
    if active_projects:
        st.markdown("## Active Projects")
        for project in active_projects:
            with st.expander(f"{project['name']} - {project['status']}"):
                st.write(f"**Description:** {project['description']}")
                st.write(f"**Created At:** {project['created_at']}")
                st.write(f"🗳️ **{project['vote_count']} Votes**")

                # Mark as Completed Button
                if st.button("Mark as Completed", key=f"complete_{project['id']}"):
                    update_project_status(project["id"], "Completed")
                    st.success(f"Project '{project['name']}' marked as Completed!")
                    st.rerun()

    # Display Voting Open Projects Section
    if voting_open_projects:
        st.markdown("## Voting Open Projects")
        for project in sorted(voting_open_projects, key=lambda p: p["vote_count"], reverse=True):
            with st.expander(f"{project['name']} - {project['status']} `{project['vote_count']} votes`"):
                st.write(f"**Description:** {project['description']}")
                st.write(f"**Created At:** {project['created_at']}")

                col1, col2 = st.columns(2)

                # Set as Active (Only for Voting Open projects)
                with col1:
                    if st.button("Set as Active", key=f"set_active_{project['id']}"):
                        update_project_status(project["id"], "Active")
                        st.success(f"Project '{project['name']}' is now Active.")
                        st.rerun()

                # Delete Project
                with col2:
                    if st.button("Delete Project", key=f"delete_{project['id']}"):
                        delete_project(project["id"])
                        st.warning(f"Project '{project['name']}' has been deleted.")
                        st.rerun()

    # Display Discarded Projects Section
    if discarded_projects:
        st.markdown("## Discarded Projects")
        for project in discarded_projects:
            with st.expander(f"{project['name']} - {project['status']}"):
                st.write(f"**Description:** {project['description']}")
                st.write(f"**Created At:** {project['created_at']}")

                # Delete Project Button
                if st.button("Delete Project", key=f"delete_discarded_{project['id']}"):
                    delete_project(project["id"])
                    st.warning(f"Project '{project['name']}' has been deleted.")
                    st.rerun()

    # Display Completed Projects Section
    if completed_projects:
        st.markdown("## Completed Projects")
        for project in completed_projects:
            with st.expander(f"{project['name']} - {project['status']}"):
                st.write(f"**Description:** {project['description']}")
                st.write(f"**Created At:** {project['created_at']}")


# Facility requests management
def facility_requests_mang():
    st.title("Manage Facility Requests")
    
    st.subheader("Requests")
    
    facility_requests = get_facility_requests()
    if not facility_requests:
        st.warning("No request available.")
        return
    
    pending_requests = []
    approved_requests = []
    rejected_requests = []
    completed_requests = []
    
    for req in facility_requests:
        if req['status'] == 'Pending':
            pending_requests.append(req)
        elif req['status'] == 'Approved':
            approved_requests.append(req)
        elif req['status'] == 'Rejected':
            rejected_requests.append(req)
        else:
            completed_requests.append(req)
    
    if pending_requests:
        st.markdown("## Pending Requests")
        for req in pending_requests:
            with st.expander(f"Request ID: {req['id']} - {req['category']} (Submitted by {req['username']})"):
                st.write(f"**Description:** {req['description']}")
                st.write(f"**Status:** {req['status']}")
                st.write(f"**Created At:** {req['created_at']}")

                new_status = st.selectbox(f"Update Status for Request {req['id']}", ['Pending', 'Approved', 'Rejected', 'Completed'], index=['Pending', 'Approved', 'Rejected', 'Completed'].index(req['status']))
                if st.button(f"Update Request {req['id']}"):
                    update_facility_status(req['id'], new_status)
    else:
        st.info("No pending requests found.")
        
    if approved_requests:  
        st.markdown("## Active/Approved Requests")
        for req in approved_requests:
            with st.expander(f"Request ID: {req['id']} - {req['category']} (Submitted by {req['username']})"):
                st.write(f"**Description:** {req['description']}")
                st.write(f"**Status:** {req['status']}")
                st.write(f"**Created At:** {req['created_at']}")

                new_status = st.selectbox(f"Update Status for Request {req['id']}", ['Pending', 'Approved', 'Rejected', 'Completed'], index=['Pending', 'Approved', 'Rejected', 'Completed'].index(req['status']))
                if st.button(f"Update Request {req['id']}"):
                    update_facility_status(req['id'], new_status)
    else:
        st.info("No approved/active requests found.")
        
    if rejected_requests:   
        st.markdown("## Rejected Requests")
        for req in rejected_requests:
            with st.expander(f"Request ID: {req['id']} - {req['category']} (Submitted by {req['username']})"):
                st.write(f"**Description:** {req['description']}")
                st.write(f"**Status:** {req['status']}")
                st.write(f"**Created At:** {req['created_at']}")

                new_status = st.selectbox(f"Update Status for Request {req['id']}", ['Pending', 'Approved', 'Rejected', 'Completed'], index=['Pending', 'Approved', 'Rejected', 'Completed'].index(req['status']))
                if st.button(f"Update Request {req['id']}"):
                    update_facility_status(req['id'], new_status)
    # else:
    #     st.info("No rejected requests found.")
        
    if completed_requests:   
        st.markdown("## Completed Requests")
        for req in completed_requests:
            with st.expander(f"Request ID: {req['id']} - {req['category']} (Submitted by {req['username']})"):
                st.write(f"**Description:** {req['description']}")
                st.write(f"**Status:** {req['status']}")
                st.write(f"**Created At:** {req['created_at']}")
    else:
        st.info("No Completed requests found.")


# Function to fetch feedbacks
def get_feedbacks():
    token = st.session_state.get("token")
    if not token:
        st.error("You need to login first.")
        return []
        
    headers = {'Authorization': f"Token {token}"}
    
    response = requests.get(f"{BASE_URL}/feedback/", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch feedbacks!, {response.status_code} - {response.text}")
        return []    


# Function to show feedback list
def show_feedbacks():
    st.title("User Feedbacks")
    
    feedbacks = get_feedbacks()
    
    if feedbacks:
        df = pd.DataFrame(feedbacks)    # Converting feedbacks list into a pandas dataframe
        st.dataframe(df, use_container_width=True)  # Displaying an interactive table
    else:
        st.info("No Feedback Available!")


# **Visualizations**

def show_request_analytics(data):
    with st.expander("Request Status Overview"):
        fig = px.bar(data, 
                     x='count', 
                     y='status', 
                     color='status', 
                     text_auto=True,  # Show exact count on bars
                     labels={"status": "Request Status", "count": "Number of Requests"},
                     title="Requests Count by Status",
                     orientation="h")
        fig.update_layout(bargap=0.6, height=300, 
                              xaxis=dict(showline=True, linecolor="black", linewidth=2), 
                              yaxis=dict(showline=True, linecolor="black", linewidth=2)
                              )
        st.plotly_chart(fig)
    

def show_voting_analytics(voting_projects):
    with st.expander("Voting Analytics"):
        st.write("Insights into the ongoing voting session.")
        
        fig = px.bar(voting_projects, 
                x="name", 
                y="vote_count", 
                text="vote_count", 
                title="Votes per Project", 
                labels={"name": "Project", "vote_count": "Total Voted"},
                color="name"
                )
        st.plotly_chart(fig, use_container_width=True)
        
        fig_pie = px.pie(voting_projects, values="vote_count", names="name", color="name", title="Vote Share per Project", hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)    
            
# Sentiment analysis            
@st.cache_resource
def load_sentiment_model():
    return pipeline(task="sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")


# Mapping labels to proper sentiment names as the used model doesnt returns sentiment names explicitly
LABEL_MAPPING = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}


def user_feedback_analytics(feedback_df):   
    sentiment_analyzer = load_sentiment_model()
    with st.expander("User Feedback Analytics"):    
        # Creating sentiment field
        feedback_df['sentiment'] = feedback_df['comments'].apply(lambda x: LABEL_MAPPING[sentiment_analyzer(x)[0]['label']])
        # Counting sentiments
        sentiment_counts = feedback_df['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['sentiment', 'count']
        
        # Bar chart for sentiment distribution
        st.subheader("User Sentiment Analysis (Count)")
        fig_bar = px.bar(sentiment_counts, 
            x='count', 
            y='sentiment', 
            color='sentiment',
            text_auto=True,
            labels={"sentiment": "Sentiment", "count": "Number of Feedbacks"},
            title="User Sentiment Distribution",
            orientation="h"
        )
        
        fig_bar.update_layout(bargap=0.5, height=400, 
                              xaxis=dict(showline=True, linecolor="black", linewidth=2), 
                              yaxis=dict(showline=True, linecolor="black", linewidth=2)
                              )
        
        st.plotly_chart(fig_bar)
        
        # Pie chart for sentiment porportion
        st.subheader("Sentiment Breakdown (%)")
        fig_pie = px.pie(sentiment_counts, names='sentiment', values='count', color='sentiment', title='User Sentiment Proportion', hole=0.4)
        st.plotly_chart(fig_pie)
        
        # feedbacks with sentiments in an interactive table
        st.markdown("## Feedbacks")
        st.dataframe(feedback_df[['rating', 'comments', 'sentiment', 'created_at']])
    

# Admin dashboard
def show_admin_dashboard():
    st.title("Admin Dashboard")
    
    # Voting analytics
    projects = get_projects()
    df = pd.DataFrame(projects)
    voting_projects_df = df[df["status"]=="Voting Open"]
    
    if not voting_projects_df.empty:
        show_voting_analytics(voting_projects_df)
    else:
        st.warning("No active voting session found.")
    
    # Request analytics
    
    # request status distribution
    requests_data = get_facility_requests()
    df = pd.DataFrame(requests_data)
    # counting requests by status
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    
    if not status_counts.empty:
        show_request_analytics(status_counts)
    else:
        st.warning("No request available.")
        
    # User feedback analytics
    
    feedbacks = get_feedbacks()
    feedback_df = pd.DataFrame(feedbacks)
    
    if not feedback_df.empty:
        user_feedback_analytics(feedback_df)
    else:
        st.warning("No user feedback available.")
    
    # st.info('This section is under development and will be available soon! Stay tuned for updates, and thank you for your patience.')

    
# User Functionalities
def show_user_dashboard():
    st.title("Digital Infrastructure Gap Portal")
    
    # Voting Section(only if voting is open and user has'nt voted)
    voting_projects = get_voting_projects()
    if voting_projects:
        if not user_already_voted():
            st.subheader("Vote for a Project")
            # Select project name (key), but store project ID (value)
            selected_project = st.selectbox("Choose a project to vote for:", list(voting_projects.keys()))
 
            if st.button("Submit Vote"):
                project_id = voting_projects[selected_project]  # Retrieve the project ID
                submit_vote(project_id)
        else:
            st.info("You have already voted in this session.")
    else:
        st.info("No projects to vote")

    # Active project selection
    active_project = get_active_project()
    if active_project:
        st.subheader("Active Project")
        st.write(f"**{active_project['name']}**")
        st.write(active_project['description'])

        st.subheader("Submit Feedback on Active Project")
        rating = st.slider("rating (1-5)", 1, 5, 3)
        comments = st.text_area("Comments")
        if st.button("Submit Feedback"):
            submit_feedback(active_project["id"], rating, comments)
    else:
        st.info("No active projects.")

# Main
def main():
    
    check_login()
    
    st.sidebar.image("/home/anuvansh/Pictures/digital_gap_portal_logo.jpg", width=310)  # Add your logo
    st.sidebar.markdown("### Digital Infrastructure Gap Portal")
    st.sidebar.markdown("---")
    
    if not st.session_state.logged_in:
        st.sidebar.markdown("## 🔐 Welcome!")
        
        choice = st.sidebar.selectbox("Choose", ("Login", "Register"))
        if choice == "Login":
            login_user()
        elif choice == "Register":
            register_user()
        return
    else:
        st.sidebar.markdown(f"👤 **Logged in as:** `{st.session_state.username}`")
        if st.sidebar.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.token = None
            st.success("You have logged out successfully!")
            # time.sleep(1)
            st.rerun()
        
        st.sidebar.subheader("Navigation")
        
        # Role based navigation
        if st.session_state.username == "admin":
            page = st.sidebar.radio("Go to", ('Admin Dashboard', 'Manage Projects', 'Manage Facility Requests', 'Feedbacks'))
        else: 
            page = st.sidebar.radio("Go to", ('Home', 'My Facility Requests'))
            
        if page == "Home":
            show_user_dashboard()
        elif page == "My Facility Requests":
            show_user_facility_requests()
        elif page == "Admin Dashboard":
            show_admin_dashboard()
        elif page == "Manage Projects":
            show_projects()
        elif page == "Manage Facility Requests":
            facility_requests_mang()
        elif page == "Feedbacks":
            show_feedbacks()
            
                
if __name__ == "__main__":
    main()