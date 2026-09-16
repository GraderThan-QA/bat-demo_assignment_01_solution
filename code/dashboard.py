"""
dashboard.py — the Streamlit interface for the Bill Splitter.

TODO: still working on this one. The inputs are there but I haven't wired
in bill.py or the chart yet.
"""

import streamlit as st

st.title("💵 Bill Splitter")

subtotal = st.number_input("Bill subtotal ($)", min_value=0.0, value=50.0, step=1.0, key="subtotal")
pct = st.slider("Tip %", min_value=0, max_value=30, value=18, key="tip")
people = st.number_input("Number of people", min_value=1, value=2, step=1, key="people")

st.write("Results coming soon...")
