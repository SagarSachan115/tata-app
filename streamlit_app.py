import streamlit as st

# Set page title
st.set_page_config(page_title="Kamgar Samiti App", layout="centered")

# Dummy user data
users = {
    "1001": {"name": "Rajesh Kumar", "loan": 50000, "emi": 2500, "balance": 25000},
    "1002": {"name": "Sita Devi", "loan": 30000, "emi": 1500, "balance": 15000},
    "1003": {"name": "Anil Sharma", "loan": 70000, "emi": 3500, "balance": 42000},
}

# Login form
st.title("Kamgar Vetan Bhogi Sahkari Rin Samiti - Member Portal")

st.sidebar.header("Login")
user_id = st.sidebar.text_input("Enter Member ID")
if st.sidebar.button("Login"):
    if user_id in users:
        user = users[user_id]
        st.success(f"Welcome, {user['name']}!")

        st.subheader("📊 Loan Details")
        st.write(f"**Loan Amount:** ₹{user['loan']:,}")
        st.write(f"**Monthly EMI:** ₹{user['emi']:,}")
        st.write(f"**Remaining Balance:** ₹{user['balance']:,}")

        st.subheader("📁 Upload Documents")
        uploaded_file = st.file_uploader("Upload ID or Loan Document", type=["pdf", "jpg", "png"])
        if uploaded_file:
            st.success("Document uploaded successfully!")

        st.subheader("📨 Raise a Request")
        query = st.text_area("Enter your request or issue")
        if st.button("Submit Request"):
            st.success("Request submitted. We will contact you soon.")
    else:
        st.error("Invalid Member ID. Please try again.")

st.sidebar.markdown("---")
st.sidebar.info("© 2025 Kamgar Vetan Bhogi Sahkari Rin Samiti Ltd.")

