
class TestExample:
    def test_phrase(self):
        expexted_len = 15
        phrase = input(f"Set phrase short as {expexted_len} symbols : ")
        assert len(phrase) <= expexted_len, f"expected len of phrase bigger as {expexted_len} symbols"


