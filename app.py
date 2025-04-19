
import streamlit as st
import pandas as pd

# Initialize or load data
if "df" not in st.session_state:
    columns = ["SR No", "RECVD DT", "INV DATE", "SUPPLIER NAME", "INV NO", "SIZE (INCH)", "GSM", "BF", "SHADE", "REEL NO"]
    st.session_state.df = pd.DataFrame(columns=columns)

columns = st.session_state.df.columns

st.title("Kraft Paper Inward Entry")

with st.form("entry_form"):
    form_data = {}
    for col in columns:
        if col == "SHADE":
            form_data[col] = st.selectbox(col, ["Natural", "Golden", "Duplex"])
        else:
            form_data[col] = st.text_input(col)
    submitted = st.form_submit_button("Add Entry")
    if submitted:
        st.session_state.df.loc[len(st.session_state.df)] = [form_data[col] for col in columns]
        st.success("Entry added successfully!")

st.subheader("Inward Entry Table")
st.dataframe(st.session_state.df)

if st.button("Export to Excel"):
    st.session_state.df.to_excel("Kraft_Paper_Inward_Web.xlsx", index=False)
    st.success("Data exported to Kraft_Paper_Inward_Web.xlsx")
