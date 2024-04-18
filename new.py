import streamlit as st
 
def calculate_emi(principal, annual_interest_rate, tenure_months):
    r = (annual_interest_rate / 12) / 100
    n = tenure_months
    emi = principal * (r * pow(1 + r, n)) / (pow(1 + r, n) - 1)
    return emi
 
def emi_schedule(principal, annual_interest_rate, tenure_months):
    r = (annual_interest_rate / 12) / 100
    n = tenure_months
    emi = calculate_emi(principal, annual_interest_rate, tenure_months)
    remaining_balance = principal
    schedule = []
 
    for month in range(1, n + 1):
        interest = remaining_balance * r
        principal_paid = emi - interest
        remaining_balance -= principal_paid
        schedule.append((month, emi, interest, principal_paid, remaining_balance))
 
    return schedule
 
# Streamlit app layout
st.title("EMI Calculator Dashboard")
 
# Input fields
principal = st.number_input("Enter principal amount:", min_value=0.0)
annual_interest_rate = st.number_input("Enter annual interest rate (%):", min_value=0.0)
tenure_months = st.number_input("Enter tenure in months:", min_value=0)
 
# Calculate button
calculate_button = st.button("Calculate EMI")
 
# Display results
if calculate_button:
    emi = calculate_emi(principal, annual_interest_rate, tenure_months)
    schedule = emi_schedule(principal, annual_interest_rate, tenure_months)
 
    st.write("EMI per month:", round(emi, 2))
 
    st.subheader("EMI Schedule")
    st.table(schedule, ["Month", "EMI", "Interest", "Principal Paid", "Remaining Balance"])