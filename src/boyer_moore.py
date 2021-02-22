from collections import defaultdict

class BoyerMooreMatcher:

    def __init__(self, case_sensitive: bool = True):
        self.case_sensitive = case_sensitive

    def search(self, pattern: str, text: str):
        if not self.case_sensitive:
            pattern = pattern.lower()
            text = text.lower()
            
        last_occurrence_dict = self._compute_last_occurrence_dict(pattern)

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

    @staticmethod
    def _compute_last_occurrence_dict(pattern: str):
        last_occurrence_dict = defaultdict(0)
        for idx, char in enumerate(pattern):
            last_occurrence_dict[char] = idx
            
        return last_occurrence_dict

    @staticmethod
    def _compute_prefix_dict(pattern: str):
        pattern_len = len(pattern)
        prefix_dict = {}
        prefix_dict[0] = 0
        k = 0

        for q in range(1, pattern_len):
            while k > 0 and pattern[k] != pattern[q]:
                k = prefix_dict[k]

            if pattern[k] == pattern[q]:
                k += 1

            prefix_dict[q] = k

        return prefix_dict

