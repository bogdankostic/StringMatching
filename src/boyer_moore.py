
class BoyerMooreMatcher:

    def __init__(self, case_sensitive: bool = True):
        self.case_sensitive = case_sensitive

    def search(self, pattern: str, text: str):
        if not self.case_sensitive:
            pattern = pattern.lower()
            text = text.lower()

        correct_shifts = []
        text_len = len(text)
        pattern_len = len(pattern)

        current_shift = 0
        while current_shift < text_len - pattern_len + 1:
            current_pattern_idx = pattern_len - 1
            while current_pattern_idx and \
                  pattern[current_pattern_idx] == text[current_shift + current_pattern_idx]:
                current_pattern_idx -= 1

            if current_pattern_idx == 0:
                correct_shifts.append(current_shift)
                s += ...
            else:
                s += ...

