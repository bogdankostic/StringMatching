from collections import defaultdict

class BoyerMooreMatcher:

    def __init__(self, case_sensitive: bool = True):
        self.case_sensitive = case_sensitive

    def search(self, pattern: str, text: str):
        if not self.case_sensitive:
            pattern = pattern.lower()
            text = text.lower()

        pattern_len = len(pattern)
        text_len = len(text)

        last_occurence_dict = self._compute_last_occurrence_dict(pattern)
        good_suffix_dict = self._compute_good_suffix_dict(pattern)
        current_shift = 0
        good_shifts = []

        while current_shift < text_len - pattern_len:
            current_char_idx = pattern_len - 1
            while current_char_idx >= 0 \
                  and pattern[current_char_idx] == text[current_shift + current_char_idx]:
                current_char_idx -= 1

            if current_char_idx < 0:
                good_shifts.append(current_shift)
                current_shift += good_suffix_dict[-1]
            else:
                bad_char = text[current_shift + current_char_idx]
                current_shift += max(
                    good_suffix_dict[current_char_idx],
                    current_char_idx - last_occurence_dict[bad_char]
                )

        return good_shifts


    @staticmethod
    def _compute_last_occurrence_dict(pattern: str):
        last_occurrence_dict = defaultdict(lambda: -1)
        for idx, char in enumerate(pattern):
            last_occurrence_dict[char] = idx
            
        return last_occurrence_dict

    @staticmethod
    def _compute_prefix_dict(pattern: str):
        pattern_len = len(pattern)
        prefix_dict = {0: 0}
        good_prefix_len = 0

        for current_idx in range(1, pattern_len):
            while good_prefix_len > 0 \
                  and pattern[good_prefix_len] != pattern[current_idx]:
                good_prefix_len = prefix_dict[good_prefix_len]

            if pattern[good_prefix_len] == pattern[current_idx]:
                good_prefix_len += 1

            prefix_dict[current_idx] = good_prefix_len

        return prefix_dict

    def _compute_good_suffix_dict(self, pattern: str):
        pattern_len = len(pattern)
        pattern_prefix_dict = self._compute_prefix_dict(pattern)

        reversed_pattern = pattern[::-1]
        reversed_pattern_prefix_dict = self._compute_prefix_dict(reversed_pattern)

        good_suffix_dict = {}
        for idx in range(-1, pattern_len):
            good_suffix_dict[idx] = pattern_len - pattern_prefix_dict[pattern_len - 1]

        for idx in range(pattern_len):
            j = pattern_len - 1 - reversed_pattern_prefix_dict[idx]
            new_value = idx - reversed_pattern_prefix_dict[idx]
            if good_suffix_dict[j] > new_value:
                good_suffix_dict[j] = new_value

        return good_suffix_dict
            
        
        
        


