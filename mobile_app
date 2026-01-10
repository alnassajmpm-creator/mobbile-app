import streamlit as st
import psycopg2

DB_URI = "YOUR_SUPABASE_CONNECTION_URI_HERE"

st.title("📱 India Mobile Entry")

with st.form("entry_form", clear_on_submit=True):
    particulars = st.selectbox("Particulars", PARTICULARS_LIST) # Use same list as above
    category = st.selectbox("Category", ["INCOME", "EXPENCE"])
    description = st.text_input("Description")
    debit = st.number_input("Debit (In ₹)", min_value=0.0)
    credit = st.number_input("Credit (Out ₹)", min_value=0.0)
    
    if st.form_submit_button("SAVE TO CLOUD"):
        conn = psycopg2.connect(DB_URI)
        cur = conn.cursor()
        cur.execute("INSERT INTO transactions (particulars, category, description, debit, credit, user_name) VALUES (%s, %s, %s, %s, %s, %s)",
                    (particulars, category, description, debit, credit, "India_Mobile"))
        conn.commit()
        st.success("Saved!")
        conn.close()
