
class NaiveMatcher:

    def __init__(self, case_sensitive: bool = True):
        self.case_sensitive = case_sensitive

    def search(self, pattern: str, text: str):
        if not self.case_sensitive:
            pattern = pattern.lower()
            text = text.lower()

        correct_shifts = []
        text_len = len(text)
        pattern_len = len(pattern)

        for shift in range(text_len - pattern_len + 1):
            candidate_match = text[shift:shift+pattern_len]
            if pattern == candidate_match:
                correct_shifts.append(shift)

        return correct_shifts
