from fuzzy_membership import FuzzyMembership

class FuzzyExhaustFan:
    @staticmethod
    def calculate(speed):
        # speed: 0 (off), 1 (low), 2 (med), 3 (high)
        m_off = 1.0 if speed == 0 else 0.0
        m_low = FuzzyMembership.trimf(speed, [0.1, 1, 2])
        m_med = FuzzyMembership.trimf(speed, [1, 2, 3])
        m_high = 1.0 if speed == 3 else FuzzyMembership.trimf(speed, [2, 3, 3.1])
        total = m_off + m_low + m_med + m_high
        if total == 0: return 0.0, 0, 0, 0, 0
        score = (m_off * 0 + m_low * 30 + m_med * 65 + m_high * 100) / total
        return score, m_off, m_low, m_med, m_high
