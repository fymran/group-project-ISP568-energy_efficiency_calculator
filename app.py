import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Energy Efficiency Calculator",
    page_icon="⚡",
    layout="wide"
)

# --- 2. Calculation Logic ---
def calculate_energy(ac_val, fan_val, plug_val, lamp_val):
    """
    Calculates Energy Usage and Efficiency based on weighted formula.
    
    Formula:
    E_usage = w1*AC + w2*Fan + w3*Plug + w4*Lamp
    Efficiency = 100 - E_usage
    
    Weights: AC=0.4, Fan=0.2, Plug=0.2, Lamp=0.2
    """
    # Weights
    w_ac = 0.4
    w_fan = 0.2
    w_plug = 0.2
    w_lamp = 0.2
    
    # Normalize Fan (0-5) to (0-100) for the formula to work with the weight
    # 0->0, 5->100. Factor is 20.
    fan_norm = fan_val * 20
    
    # Weighted Contributions
    c_ac = w_ac * ac_val
    c_fan = w_fan * fan_norm
    c_plug = w_plug * plug_val
    c_lamp = w_lamp * lamp_val
    
    # Total Usage Score
    e_usage = c_ac + c_fan + c_plug + c_lamp
    
    # Energy Efficiency Score (Inversely proportional)
    efficiency = 100 - e_usage
    
    # Clamp results to 0-100 just in case
    e_usage = max(0, min(100, e_usage))
    efficiency = max(0, min(100, efficiency))
    
    return efficiency, e_usage, c_ac, c_fan, c_plug, c_lamp

def get_efficiency_label(efficiency_score):
    """Maps efficiency score to linguistic terms."""
    if efficiency_score >= 80:
        return "Very High", "#38761d", "🌱", "white" # High Efficiency = Good
    elif efficiency_score >= 60:
        return "High", "#93c47d", "✅", "black"
    elif efficiency_score >= 40:
        return "Medium", "#ffd966", "🟡", "black"
    elif efficiency_score >= 20:
        return "Low", "#e69138", "⚠️", "black"
    else:
        return "Very Low", "#cc0000", "🔥", "white" # Low Efficiency = Bad


# --- 3. Sidebar Inputs (Collapsible Drawer for Room) ---
#1.Living Room
with st.sidebar.expander("🛏️ Living Room", expanded=False):

    # 1. Air Conditioner
    # Mapping: off->0, low->30, medium->60, high->90
    ac_map1 = {'Off': 0, 'Low': 30, 'Medium': 60, 'High': 90}
    ac_choice1 = st.selectbox("1. Air Conditioner Usage", options=list(ac_map1.keys()), index=0, key="ac1")
    val_ac1 = ac_map1[ac_choice1]

    # 2. Fan Speed
    # Range 0-5
    val_fan1 = st.slider("2. Fan Speed (0-5)", 0, 5, 0, 1, key="fan1")

    # 3. Plug Load
    # Mapping: off->0, low->25, medium->60, high->90
    plug_map1 = {'Off': 0, 'Low': 25, 'Medium': 60, 'High': 90}
    plug_choice1 = st.selectbox("3. Plug Load", options=list(plug_map1.keys()), index=0, key="plug1")
    val_plug1 = plug_map1[plug_choice1]

    # 4. Lamp Load
    # Mapping: off->0, low->20, medium->50, high->80
    lamp_map1 = {'Off': 0, 'Low': 20, 'Medium': 50, 'High': 80}
    lamp_choice1 = st.selectbox("4. Lamp / Lighting", options=list(lamp_map1.keys()), index=0, key="lamp1")
    val_lamp1 = lamp_map1[lamp_choice1]

    st.markdown("---")
    st.info(f"**Raw Inputs:**\n\nAC: {val_ac1} | Fan: {val_fan1} | Plug: {val_plug1} | Lamp: {val_lamp1}")

#2.Sons' Room
with st.sidebar.expander("🛏️ Son's Room", expanded=False):

    # 1. Air Conditioner
    # Mapping: off->0, low->30, medium->60, high->90
    ac_map2 = {'Off': 0, 'Low': 30, 'Medium': 60, 'High': 90}
    ac_choice2 = st.selectbox("1. Air Conditioner Usage", options=list(ac_map2.keys()), index=0, key="ac2")
    val_ac2 = ac_map2[ac_choice2]

    # 2. Fan Speed
    # Range 0-5
    val_fan2 = st.slider("2. Fan Speed (0-5)", 0, 5, 0, 1, key="fan2")

    # 3. Plug Load
    # Mapping: off->0, low->25, medium->60, high->90
    plug_map2 = {'Off': 0, 'Low': 25, 'Medium': 60, 'High': 90}
    plug_choice2 = st.selectbox("3. Plug Load", options=list(plug_map2.keys()), index=0, key="plug2")
    val_plug2 = plug_map2[plug_choice2]

    # 4. Lamp Load
    # Mapping: off->0, low->20, medium->50, high->80
    lamp_map2 = {'Off': 0, 'Low': 20, 'Medium': 50, 'High': 80}
    lamp_choice2 = st.selectbox("4. Lamp / Lighting", options=list(lamp_map2.keys()), index=0, key="lamp2")
    val_lamp2 = lamp_map2[lamp_choice2]

    st.markdown("---")
    st.info(f"**Raw Inputs:**\n\nAC: {val_ac2} | Fan: {val_fan2} | Plug: {val_plug2} | Lamp: {val_lamp2}")

#3.Parent's Room
with st.sidebar.expander("🛏️ Parent's Room", expanded=False):

    # 1. Air Conditioner
    # Mapping: off->0, low->30, medium->60, high->90
    ac_map3 = {'Off': 0, 'Low': 30, 'Medium': 60, 'High': 90}
    ac_choice3 = st.selectbox("1. Air Conditioner Usage", options=list(ac_map3.keys()), index=0, key="ac3")
    val_ac3 = ac_map3[ac_choice3]

    # 2. Fan Speed
    # Range 0-5
    val_fan3 = st.slider("2. Fan Speed (0-5)", 0, 5, 0, 1, key="fan3")

    # 3. Plug Load
    # Mapping: off->0, low->25, medium->60, high->90
    plug_map3 = {'Off': 0, 'Low': 25, 'Medium': 60, 'High': 90}
    plug_choice3 = st.selectbox("3. Plug Load", options=list(plug_map3.keys()), index=0, key="plug3")
    val_plug3 = plug_map3[plug_choice3]

    # 4. Lamp Load
    # Mapping: off->0, low->20, medium->50, high->80
    lamp_map3 = {'Off': 0, 'Low': 20, 'Medium': 50, 'High': 80}
    lamp_choice3 = st.selectbox("4. Lamp / Lighting", options=list(lamp_map3.keys()), index=0, key="lamp3")
    val_lamp3 = lamp_map3[lamp_choice3]

    st.markdown("---")
    st.info(f"**Raw Inputs:**\n\nAC: {val_ac3} | Fan: {val_fan3} | Plug: {val_plug3} | Lamp: {val_lamp3}")

#4.Kitchen
with st.sidebar.expander("🛏️ Kitchen", expanded=False):

    # 1. exhaust Fan
    #Range 0-5
    val_exhaust_fan = st.slider("2. Exhaust Fan Speed (0-3)", 0, 3, 0, 1, key="exfan")

    # 2. Fan Speed
    # Range 0-5
    val_fan4 = st.slider("2. Fan Speed (0-5)", 0, 5, 0, 1, key="fan4")

    # 3. Plug Load
    # Mapping: off->0, low->25, medium->60, high->90
    plug_map4 = {'Off': 0, 'Low': 25, 'Medium': 60, 'High': 90}
    plug_choice4 = st.selectbox("3. Plug Load", options=list(plug_map4.keys()), index=0, key="plug4")
    val_plug4 = plug_map4[plug_choice4]

    # 4. Lamp Load
    # Mapping: off->0, low->20, medium->50, high->80
    lamp_map4 = {'Off': 0, 'Low': 20, 'Medium': 50, 'High': 80}
    lamp_choice4 = st.selectbox("4. Lamp / Lighting", options=list(lamp_map4.keys()), index=0, key="lamp4")
    val_lamp4 = lamp_map4[lamp_choice4]

    st.markdown("---")
    st.info(f"**Raw Inputs:**\n\Exhaust Fan: {val_exhaust_fan} | Fan: {val_fan4} | Plug: {val_plug4} | Lamp: {val_lamp4}")

# --- 4. Main Content ---
st.title("🏠 Smart Home Energy Efficiency Tracker")
st.markdown("Calculates **Energy Efficiency** based on appliance usage. Lower usage results in higher efficiency.")
# Aggregate Inputs from all rooms
val_ac = (val_ac1 + val_ac2 + val_ac3)/3
val_fan = (val_fan1 + val_fan2 + val_fan3 + val_fan4 + val_exhaust_fan)/4
val_plug = (val_plug1 + val_plug2 + val_plug3 + val_plug4)/4
val_lamp = (val_lamp1 + val_lamp2 + val_lamp3 + val_lamp4)/4
# --- Calculation ---
efficiency, usage_score, c_ac, c_fan, c_plug, c_lamp = calculate_energy(val_ac, val_fan, val_plug, val_lamp)
label, color, icon, text_color = get_efficiency_label(efficiency)

# --- Display Results ---
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("Efficiency Score")
    st.markdown(f"""
    <div style="padding: 20px; border-radius: 10px; text-align: center; 
                background-color: {color}; color: {text_color}; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h3 style="margin:0; color: {text_color};">EFFICIENCY LEVEL</h3>
        <div style="font-size: 3em; margin: 15px 0;">{icon} {label.upper()}</div>
        <p style="font-size: 1.2em; font-weight: bold;">{efficiency:.1f} / 100</p>
        <hr style="border-color: {text_color}; opacity: 0.3;">
        <p style="font-size: 0.9em;">Energy Usage Score: {usage_score:.1f}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Tip:** Higher Efficiency means you are saving more energy!")

with col2:
    st.subheader("Usage Breakdown")
    # Bar chart showing contribution of each device to the Usage Score
    
    categories = ['Air Cond', 'Fan', 'Plug', 'Lamp']
    values = [c_ac, c_fan, c_plug, c_lamp]
    colors = ['#3498db', '#2ecc71', '#e74c3c', '#f1c40f']
    
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(categories, values, color=colors)
    
    # Add values to end of bars
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width + 1 if width < 90 else width - 5
        ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}', va='center')

    ax.set_xlabel('Weighted Contribution to Usage Score')
    ax.set_xlim(0, 50) # Fixed limit helps visualization stability
    ax.set_title(f'Total Usage Score: {usage_score:.1f}')
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    st.pyplot(fig)

# --- 5. Educational Section ---
with st.expander("📚 View Formula & Logic Details"):
    st.markdown("### 1. Calculation Formula")
    st.latex(r"""
    E_{usage} = 0.4(AC) + 0.2(Fan_{norm}) + 0.2(Plug) + 0.2(Lamp)
    """)
    st.latex(r"""
    Efficiency = 100 - E_{usage}
    """)
    
    st.markdown("### 2. Input Mappings")
    st.markdown("""
    - **Air Conditioner:** Off(0), Low(30), Medium(60), High(90)
    - **Fan:** 0 to 5 (Normalized to 0-100 scale)
    - **Plug:** Off(0), Low(25), Medium(60), High(90)
    - **Lamp:** Off(0), Low(20), Medium(50), High(80)
    """)
    
    st.markdown("### 3. Output Categories")
    st.markdown("""
    | Efficiency Score | Level |
    | :--- | :--- |
    | 80 - 100 | **Very High** (Excellent) |
    | 60 - 79 | **High** |
    | 40 - 59 | **Medium** |
    | 20 - 39 | **Low** |
    | 0 - 19 | **Very Low** (High Consumption) |
    """)