class TestMath:
    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y

    def test_add(self):
        return self.x + self.y

    def test_subtract(self):
        return self.x - self.y

    def test_multiply(self):
        return self.x * self.y