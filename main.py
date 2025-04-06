import streamlit as st

st.set_page_config(page_title="Unit Converter", layout='wide') 

#Styling
st.markdown(
    """
<style>
.stApp{
    background-color: grey;
    color:black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Title and Description 
st.title("Unit Converter App") 
st.write("This app will help you to convert all basic units as per your wish.") 

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }
    value_in_meters = value * conversions[from_unit]
    return value_in_meters / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    value_in_grams = value * conversions[from_unit]
    return value_in_grams / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def convert_area(value, from_unit, to_unit):
    conversions = {
        'square meters': 1,
        'square kilometers': 1e6,
        'square centimeters': 0.0001,
        'square millimeters': 1e-6,
        'acres': 4046.86,
        'hectares': 10000,
        'square feet': 0.092903,
        'square inches': 0.00064516
    }
    value_in_square_meters = value * conversions[from_unit]
    return value_in_square_meters / conversions[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cubic meters': 1000,
        'cubic centimeters': 0.001,
        'cubic inches': 0.0163871,
        'cubic feet': 28.3168
    }
    value_in_liters = value * conversions[from_unit]
    return value_in_liters / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800
    }
    value_in_seconds = value * conversions[from_unit]
    return value_in_seconds / conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {
        'm/s': 1,
        'km/h': 0.277778,
        'mph': 0.44704,
        'ft/s': 0.3048
    }
    value_in_mps = value * conversions[from_unit]
    return value_in_mps / conversions[to_unit]

def convert_pressure(value, from_unit, to_unit):
    conversions = {
        'pascals': 1,
        'kilopascals': 1000,
        'bars': 100000,
        'atmospheres': 101325,
        'psi': 6894.76
    }
    value_in_pascals = value * conversions[from_unit]
    return value_in_pascals / conversions[to_unit]

# Define the main Streamlit app
def main():
    st.title('Unit Converter')

    # Choose category for conversion
    conversion_category = st.selectbox('Select Conversion Category', [
        'Length', 'Weight', 'Temperature', 'Area', 'Volume', 'Time', 'Speed', 'Pressure'
    ])

    # Create input fields based on category selection
    value = st.number_input('Enter value:', min_value=0.0, step=0.1)
    
    if conversion_category == 'Length':
        length_units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'inches', 'feet', 'yards', 'miles']
        from_unit = st.selectbox('From Unit', length_units)
        to_unit = st.selectbox('To Unit', length_units)
        
        if st.button('Convert'):
            result = convert_length(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Weight':
        weight_units = ['grams', 'kilograms', 'milligrams', 'pounds', 'ounces']
        from_unit = st.selectbox('From Unit', weight_units)
        to_unit = st.selectbox('To Unit', weight_units)
        
        if st.button('Convert'):
            result = convert_weight(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Temperature':
        temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
        from_unit = st.selectbox('From Unit', temperature_units)
        to_unit = st.selectbox('To Unit', temperature_units)
        
        if st.button('Convert'):
            result = convert_temperature(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Area':
        area_units = ['square meters', 'square kilometers', 'square centimeters', 'square millimeters', 'acres', 'hectares', 'square feet', 'square inches']
        from_unit = st.selectbox('From Unit', area_units)
        to_unit = st.selectbox('To Unit', area_units)
        
        if st.button('Convert'):
            result = convert_area(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Volume':
        volume_units = ['liters', 'milliliters', 'gallons', 'cubic meters', 'cubic centimeters', 'cubic inches', 'cubic feet']
        from_unit = st.selectbox('From Unit', volume_units)
        to_unit = st.selectbox('To Unit', volume_units)
        
        if st.button('Convert'):
            result = convert_volume(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Time':
        time_units = ['seconds', 'minutes', 'hours', 'days', 'weeks']
        from_unit = st.selectbox('From Unit', time_units)
        to_unit = st.selectbox('To Unit', time_units)
        
        if st.button('Convert'):
            result = convert_time(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Speed':
        speed_units = ['m/s', 'km/h', 'mph', 'ft/s']
        from_unit = st.selectbox('From Unit', speed_units)
        to_unit = st.selectbox('To Unit', speed_units)
        
        if st.button('Convert'):
            result = convert_speed(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    elif conversion_category == 'Pressure':
        pressure_units = ['pascals', 'kilopascals', 'bars', 'atmospheres', 'psi']
        from_unit = st.selectbox('From Unit', pressure_units)
        to_unit = st.selectbox('To Unit', pressure_units)
        
        if st.button('Convert'):
            result = convert_pressure(value, from_unit, to_unit)
            st.write(f'{value} {from_unit} = {result} {to_unit}')
    
    # Add Tailwind CSS for styling
    st.markdown("""
        <style>
            /* Tailwind CSS */
            .stApp {
                font-family: 'Inter', sans-serif;
            }
            .stButton>button {
                background-color: red;
                color: black;
                border-radius: 8px;
                padding: 12px;
                text-align: center;
            }
            .stButton>button:hover {
                background-color: green;
            }
        </style>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
