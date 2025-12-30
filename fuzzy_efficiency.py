from fuzzy_membership import FuzzyMembership
import numpy as np

class FuzzyEfficiency:
    @staticmethod
    def calculate_energy(ac_score, fan_score, plug_score, lamp_score):
        w_ac, w_fan, w_plug, w_lamp = 0.4, 0.2, 0.2, 0.2
        e_usage = (w_ac * ac_score) + (w_fan * fan_score) + (w_plug * plug_score) + (w_lamp * lamp_score)
        efficiency = 100 - e_usage
        m_vlow = FuzzyMembership.trimf(efficiency, [-0.1, 0, 25])
        m_low = FuzzyMembership.trimf(efficiency, [20, 40, 60])
        m_med = FuzzyMembership.trimf(efficiency, [40, 60, 80])
        m_high = FuzzyMembership.trimf(efficiency, [75, 100, 100.1])
        return efficiency, e_usage, m_vlow, m_low, m_med, m_high

    @staticmethod
    def get_efficiency_label(efficiency_score):
        if efficiency_score >= 80:
            return "Very High", "#38761d", "🌱", "white"
        elif efficiency_score >= 60:
            return "High", "#93c47d", "✅", "black"
        elif efficiency_score >= 40:
            return "Medium", "#ffd966", "🟡", "black"
        elif efficiency_score >= 20:
            return "Low", "#e69138", "⚠️", "black"
        else:
            return "Very Low", "#cc0000", "🔥", "white"
