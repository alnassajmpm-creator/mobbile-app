import streamlit as st
import psycopg2

# --- DATABASE CONFIG ---
# ലിങ്ക് കൃത്യമായി ഈ രീതിയിൽ തന്നെ നൽകുക
DB_URI = "postgresql://postgres.vneiheoyglbwxlzdstrp:basheer123@aws-1-ap-south-1.pooler.supabase.com:6543/postgres"

# നിങ്ങളുടെ ലിസ്റ്റ്
PARTICULARS_LIST = [
    "SALARY FROM SCHOOL", "SALARY FROM TUTION", "SALARY FROM ALMAHS", 
    "CHITTY RICEVED", "DONATION RICIEVED", "TRAINING AND COUNSELLING INCOME",
    "CASH BORROWING", "OTHER INCOME", "SAVINGS WITHDRAW", "LENDING CASH RITERN",
    "WITH DRAW FROM SAVINGS", "OPENING BALANCE", "ALMAHS FEE RICEVED",
    "TRAVEL AND PETROL", "PAID TO CHITTY", "HOME PURCHASE", "FOOD PURCHASE",
    "SHOPING AND PURCHASE", "NAHAL EXPENCES", "PERSONAL PURCHASE",
    "HEALTH AND MEDICAL EXP.", "TRAINING AND STUDYING EXPENCES", "PAID DONATION",
    "CASH LENNDING", "BORROW RETERN", "NIDHA AND RIHAM EXPENCES",
    "ALMAHS INVESTMENT EXP.", "ALMAHS 30% TO SAVINGS", "MY SALARY 20% TO SAVINGS",
    "ALMAHS 20% TO SAVINGS", "MY SALARY 30% TO SAVINGS", "PERSONAL DEPOSIT TO SAVINGS",
    "PERSONAL 10% SAVINGS", "DEPOSITED TO ACCAUNT FOR SAVINGS", "ALMAHS EXPENCES",
    "ALMAHS TEA AND SNACKS EXP.", "PREVIOUS YEAR EXPENCES CREDIT"
]

st.title("📱 India Mobile Entry")

with st.form("entry_form", clear_on_submit=True):
    particulars = st.selectbox("Particulars", PARTICULARS_LIST)
    category = st.selectbox("Category", ["INCOME", "EXPENCE"])
    description = st.text_input("Description")
    debit = st.number_input("Debit (In ₹)", min_value=0.0)
    credit = st.number_input("Credit (Out ₹)", min_value=0.0)
    
    if st.form_submit_button("SAVE TO CLOUD"):
        try:
            # ഡാറ്റാബേസിലേക്ക് കണക്ട് ചെയ്യുന്നു
            conn = psycopg2.connect(DB_URI, sslmode='require')
            cur = conn.cursor()
            cur.execute("INSERT INTO transactions (particulars, category, description, debit, credit, user_name) VALUES (%s, %s, %s, %s, %s, %s)",
                        (particulars, category, description, debit, credit, "India_Mobile"))
            conn.commit()
            st.success("Saved Successfully! ✅")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")
