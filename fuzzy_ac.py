from fuzzy_membership import FuzzyMembership

class FuzzyAC:
    @staticmethod
    def calculate(temp):
        if temp == 0: return 0.0, 1.0, 0.0, 0.0, 0.0
        m_low = FuzzyMembership.trimf(temp, [25, 27, 29])
        m_med = FuzzyMembership.trimf(temp, [22, 24, 26])
        m_high = FuzzyMembership.trimf(temp, [15.9, 16, 23])
        m_off = 0.0
        total = m_low + m_med + m_high
        if total == 0: return 0.0, 0, 0, 0, 0
        score = (m_low * 25 + m_med * 60 + m_high * 100) / total
        return score, m_off, m_low, m_med, m_high
