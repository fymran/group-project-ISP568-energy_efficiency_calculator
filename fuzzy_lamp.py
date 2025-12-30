from fuzzy_membership import FuzzyMembership

class FuzzyLamp:
    @staticmethod
    def calculate(intensity):
        m_off = 1.0 if intensity == 0 else 0.0
        m_low = FuzzyMembership.trimf(intensity, [0.1, 16.5, 33])
        m_med = FuzzyMembership.trimf(intensity, [25, 50, 75])
        m_high = FuzzyMembership.trimf(intensity, [66, 100, 100.1])
        total = m_off + m_low + m_med + m_high
        if total == 0: return 0.0, 0, 0, 0, 0
        score = (m_off * 0 + m_low * 25 + m_med * 60 + m_high * 100) / total
        return score, m_off, m_low, m_med, m_high
