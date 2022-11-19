import krakenex
from pykrakenapi import KrakenAPI
import streamlit as st

api = krakenex.API()
k = KrakenAPI(api)
pairs = k.get_tradable_asset_pairs()


st.title("Kraken API")
st.header("get_tradable_asset_pairs()")
st.markdown("This endpoint returns a list of tradable asset pairs from Kraken")

st.dataframe(pairs)