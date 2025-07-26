import streamlit as st

from garden_planner import load_plants, recommend_plants, watering_string

st.set_page_config(page_title="Smart Garden Planner")
st.title("Smart Garden Planner")

plants = load_plants()

# Gather options
climate_options = sorted({c for p in plants for c in p["climate"]})
soil_options = sorted({p["soil"] for p in plants})
sun_options = sorted({p["sunlight"] for p in plants})

with st.sidebar:
    st.header("Garden Conditions")
    climate = st.selectbox("Climate", climate_options)
    sunlight = st.selectbox("Sunlight", sun_options)
    soil = st.selectbox("Soil", soil_options)
    rainfall = st.slider("Rainfall this week (mm)", 0, 40, 0)

matches = recommend_plants(plants, climate, sunlight, soil)

if not matches:
    st.warning("No matching plants found.")
else:
    st.subheader("Recommended Plants")
    for plant in matches:
        st.markdown(f"### {plant['name']}")
        st.write(f"Sunlight: {plant['sunlight']}  ")
        st.write(f"Soil: {plant['soil']}  ")
        st.write(watering_string(plant, rainfall))
        st.markdown("---")
