
import streamlit as st
import numpy as np
from fuzzy_plug import FuzzyPlug
from fuzzy_lamp import FuzzyLamp
from fuzzy_ac import FuzzyAC
from fuzzy_fan import FuzzyFan
from fuzzy_exhaust_fan import FuzzyExhaustFan
from fuzzy_efficiency import FuzzyEfficiency
from fuzzy_plotter import FuzzyPlotter

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Energy Efficiency Calculator",
    page_icon="⚡",
    layout="wide"
)

# --- 4. Sidebar Inputs ---


def room_ui(room_name, key_suffix, is_kitchen=False):
    with st.sidebar.expander(f"🛏️ {room_name}", expanded=False):
        if not is_kitchen:
            # FUZZY AC
            ac_on = st.toggle(f"Power AC {room_name}", value=False, key=f"acon{key_suffix}")
            if ac_on:
                val_temp = st.select_slider(f"1. AC Temp (°C)", options=list(range(28, 15, -1)), value=24, key=f"temp{key_suffix}")
                ac_s, a_off, a_low, a_med, a_high = FuzzyAC.calculate(val_temp)
                st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_temp, a_off, a_low, a_med, a_high, 28, "AC"))
            else:
                ac_s = 0.0
                st.info("AC is turned off")
            # FUZZY FAN
            val_fan = st.slider(f"2. Fan Speed", 0, 5, 0, 1, key=f"fan{key_suffix}")
            f_s, f_off, f_low, f_med, f_high = FuzzyFan.calculate(val_fan)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_fan, f_off, f_low, f_med, f_high, 5, "Fan"))
            # FUZZY PLUG
            val_v = st.slider(f"3. Plug Voltage (0-240V)", 0, 240, 0, 1, key=f"v{key_suffix}")
            v_s, p_off, p_low, p_med, p_high = FuzzyPlug.calculate(val_v)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_v, p_off, p_low, p_med, p_high, 240, "Plug"))
            # FUZZY LAMP
            val_l = st.slider(f"4. Lamp Intensity (0-100%)", 0, 100, 0, 1, key=f"l{key_suffix}")
            l_s, l_off, l_low, l_med, l_high = FuzzyLamp.calculate(val_l)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_l, l_off, l_low, l_med, l_high, 100, "Lamp"))
            # Always return 5 values for consistency (ac, fan, exhaust, plug, lamp)
            return ac_s, f_s, 0.0, v_s, l_s
        else:
            # Kitchen: Exhaust Fan (3 speed, replaces AC)
            ac_s = 0.0
            val_exhaust = st.slider(f"1. Exhaust Fan Speed", 0, 3, 0, 1, key=f"exfan{key_suffix}")
            exhaust_s, ex_off, ex_low, ex_med, ex_high = FuzzyExhaustFan.calculate(val_exhaust)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_exhaust, ex_off, ex_low, ex_med, ex_high, 3, "Fan"))
            # Kitchen: Regular Fan
            val_fan = st.slider(f"2. Fan Speed", 0, 5, 0, 1, key=f"fan{key_suffix}")
            fan_s, f_off, f_low, f_med, f_high = FuzzyFan.calculate(val_fan)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_fan, f_off, f_low, f_med, f_high, 5, "Fan"))
            # FUZZY PLUG
            val_v = st.slider(f"3. Plug Voltage (0-240V)", 0, 240, 0, 1, key=f"v{key_suffix}")
            v_s, p_off, p_low, p_med, p_high = FuzzyPlug.calculate(val_v)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_v, p_off, p_low, p_med, p_high, 240, "Plug"))
            # FUZZY LAMP
            val_l = st.slider(f"4. Lamp Intensity (0-100%)", 0, 100, 0, 1, key=f"l{key_suffix}")
            l_s, l_off, l_low, l_med, l_high = FuzzyLamp.calculate(val_l)
            st.pyplot(FuzzyPlotter.plot_live_fuzzy(val_l, l_off, l_low, l_med, l_high, 100, "Lamp"))
            return ac_s, fan_s, exhaust_s, v_s, l_s


v1 = room_ui("Living Room", "1")
v2 = room_ui("Son's Room", "2")
v3 = room_ui("Parent's Room", "3")
v4 = room_ui("Kitchen", "4", is_kitchen=True)

# --- 5. Main Content ---
st.title("🏠 Smart Home Energy Efficiency Tracker (Fuzzy Logic)")
st.markdown("All inputs and the final output now utilize **Fuzzy Inference Systems** for precise environmental modeling.")




# Aggregate Inputs
# For kitchen: v4 = (ac_s, fan_s, exhaust_s, v_s, l_s)

ac_scores = [v1[0], v2[0], v3[0], v4[0]]
fan_scores = [v1[1], v2[1], v3[1], v4[1]]
plug_scores = [v1[3], v2[3], v3[3], v4[3]]
lamp_scores = [v1[4], v2[4], v3[4], v4[4]]

avg_ac = np.mean(ac_scores)
avg_fan = np.mean(fan_scores)
avg_plug = np.mean(plug_scores)
avg_lamp = np.mean(lamp_scores)

eff, usage, m_vl, m_l, m_m, m_h = FuzzyEfficiency.calculate_energy(avg_ac, avg_fan, avg_plug, avg_lamp)
label, color, icon, text_color = FuzzyEfficiency.get_efficiency_label(eff)

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Efficiency Status")
    st.markdown(f"""
    <div style="padding: 20px; border-radius: 10px; text-align: center; 
                background-color: {color}; color: {text_color}; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h3 style="margin:0; color: {text_color};">EFFICIENCY LEVEL</h3>
        <div style="font-size: 3.5em; margin: 15px 0;">{icon} {label.upper()}</div>
        <p style="font-size: 1.4em; font-weight: bold;">{eff:.1f} / 100</p>
        <hr style="border-color: {text_color}; opacity: 0.3;">
        <p style="font-size: 0.9em;">Aggregate Usage Score: {usage:.1f}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Global Efficiency Fuzzy Membership")
    st.pyplot(FuzzyPlotter.plot_live_fuzzy(eff, m_vl, m_l, m_m, m_h, 100, "Efficiency"))
    st.info(f"The blue marker indicates the system's defuzzified efficiency value: **{eff:.1f}%**.")

# --- 6. Educational & Methodology Section ---
st.divider()

with st.expander("🧮 View Calculation Methodology"):
    st.markdown("### Energy Usage Formula")
    st.latex(r"Usage_{total} = \sum (Weight_i \times Score_i)")
    st.markdown("Where $Score_i$ is the defuzzified score for each appliance type across all rooms.")
    
    st.markdown("### Weights ($W_i$):")
    cols = st.columns(4)
    cols[0].metric("AC Weight", "0.4")
    cols[1].metric("Fan Weight", "0.2")
    cols[2].metric("Plug Weight", "0.2")
    cols[3].metric("Lamp Weight", "0.2")
    
    st.markdown("### Defuzzification (Centroid Method):")
    st.latex(r"Score = \frac{\sum (\mu(x) \times Center_x)}{\sum \mu(x)}")
    st.write("For each input, the system calculates the degree of membership $\mu(x)$ for Low, Medium, and High sets, then calculates a weighted average score based on set centers (e.g., Low=25, High=100).")

with st.expander("📚 View Fuzzy Sets Definition"):
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Fan Speed (0-5):**")
        st.markdown("- **Low**: 0.1 → 3.0 (Center: 1.5)")
        st.markdown("- **Med**: 2.0 → 5.0 (Center: 3.5)")
        st.markdown("- **High**: 4.0 → 5.1 (Center: 5.0)")
        st.markdown("**AC (16-28°C):**")
        st.markdown("- **Low Energy**: 25°C → 29°C")
        st.markdown("- **Med Energy**: 22°C → 26°C")
        st.markdown("- **High Energy**: 15.9°C → 23°C")
    with col_b:
        st.markdown("**Efficiency Output (0-100%):**")
        st.markdown("- **Very Low**: 0-25%")
        st.markdown("- **Low**: 20-60%")
        st.markdown("- **Medium**: 40-80%")
        st.markdown("- **High**: 75-100%")