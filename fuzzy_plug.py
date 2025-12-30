from fuzzy_membership import FuzzyMembership

class FuzzyPlug:
    @staticmethod
    def calculate(voltage):
        m_off = 1.0 if voltage == 0 else 0.0
        m_low = FuzzyMembership.trimf(voltage, [0.1, 40, 80])
        m_med = FuzzyMembership.trimf(voltage, [60, 120, 180])
        m_high = FuzzyMembership.trimf(voltage, [160, 240, 240.1])
        total = m_off + m_low + m_med + m_high
        if total == 0: return 0.0, 0, 0, 0, 0
        score = (m_off * 0 + m_low * 25 + m_med * 60 + m_high * 100) / total
        return score, m_off, m_low, m_med, m_high
