from fuzzy_membership import FuzzyMembership

class FuzzyFan:
    @staticmethod
    def calculate(speed):
        m_off = 1.0 if speed == 0 else 0.0
        m_low = FuzzyMembership.trimf(speed, [0.1, 1.5, 3.0])
        m_med = FuzzyMembership.trimf(speed, [2.0, 3.5, 5.0])
        m_high = 1.0 if speed == 5 else FuzzyMembership.trimf(speed, [4.0, 5.0, 5.1])
        total = m_off + m_low + m_med + m_high
        if total == 0: return 0.0, 0, 0, 0, 0
        score = (m_off * 0 + m_low * 30 + m_med * 65 + m_high * 100) / total
        return score, m_off, m_low, m_med, m_high
