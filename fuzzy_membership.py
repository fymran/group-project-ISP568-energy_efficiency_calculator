class FuzzyMembership:
    """Helper class for fuzzy membership functions."""
    @staticmethod
    def trimf(x, abc):
        assert len(abc) == 3, 'abc must be a list of 3 floats'
        a, b, c = abc
        if x <= a or x >= c:
            return 0.0
        if a < x <= b:
            return (x - a) / (b - a)
        if b < x < c:
            return (c - x) / (c - b)
        return 0.0
