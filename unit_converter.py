import streamlit as st

def convert_unit(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilograms
        "kilogram_gram": 1000, # 1 Kilogram = 1000 grams
         
    }
    key = f"{unit_from}_{unit_to}" # generate a unique key based on input and output units 
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported or available"
    
st.title("Unit Converter ⚖️")
value = st.number_input("Enter the value you want to convert")
unit_from = st.selectbox("Convert From", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert To", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"{value} {unit_from} is equal to {result} {unit_to}")

st.write("____________________________________________________________________")    
st.write("Made by Khadija Faisal ❤️")
       

