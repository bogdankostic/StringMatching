from collections import defaultdict

class BoyerMooreMatcher:
    """
    Implements the Boyer-Moore string matching algorithm as it was
    outlined in Cormen et al.'s (1990) 'Introduction to Algorithms'.
    """

    def __init__(self, case_sensitive: bool = True):
        """
        Instantiates a BoyerMooreMatcher instance.

        :param case_sensitive: Whether the string matching is
            case-sensitive. (default = True)
        :type case_sensitive: bool
        """
        self.case_sensitive = case_sensitive

    def search(self, pattern: str, text: str):
        """
        Searches for pattern in text and returns a list containing
        all indices where an instance of pattern starts in the text.

        :param pattern: The search pattern.
        :type pattern: str
        :param text: The text string to search in.
        :type text: str
        :return: List with indices, where occurrences of the search
            start in the text.
        :rtype: List[int]
        """
        if not self.case_sensitive:
            # Lowercase search pattern and text for case-insensitive search
            pattern = pattern.lower()
            text = text.lower()

        pattern_len = len(pattern)
        text_len = len(text)

        # Preprocessing of the pattern to be able to make use of the
        # bad-character heuristic and good-suffix heuristic
        last_occurence_dict = self._compute_last_occurrence_dict(pattern)
        good_suffix_dict = self._compute_good_suffix_dict(pattern)
        current_shift = 0
        good_shifts = []

        # Iterate over text
        while current_shift <= text_len - pattern_len:
            # Compare pattern and current text slice from right to left
            current_char_idx = pattern_len - 1
            while current_char_idx >= 0 and \
                pattern[current_char_idx] == \
                text[current_shift + current_char_idx]:
                # Current pattern char and current text char match
                current_char_idx -= 1

            # Pattern matches current text slice
            if current_char_idx < 0:
                good_shifts.append(current_shift)
                # Use good-suffix heuristic to get start of new text slice
                current_shift += good_suffix_dict[-1]

            # Pattern doesn't match current text slice
            else:
                bad_char = text[current_shift + current_char_idx]
                # Use maximum of good-suffix heuristic and bad-character
                # heuristic to get start of new text slice
                current_shift += max(
                    good_suffix_dict[current_char_idx],
                    current_char_idx - last_occurence_dict[bad_char]
                )

        return good_shifts


    @staticmethod
    def _compute_last_occurrence_dict(pattern: str):
        """
        Creates a dictionary with each char of pattern as key and the
        highest index the char can be found as value. For chars
        not contained in the pattern, the dict returns a default value
        of -1.

        :param pattern: The search pattern.
        :type pattern: str
        :return: Dictionary with each char of the pattern as key and the
            highest index the char can be found at as value.
        :rtype: Dict[str, int]
        """
        last_occurrence_dict = defaultdict(lambda: -1)
        for idx, char in enumerate(pattern):
            last_occurrence_dict[char] = idx
            
        return last_occurrence_dict

    @staticmethod
    def _compute_prefix_dict(pattern: str):
        """
        For each position in the pattern, computes the length of the
        longest prefix of the pattern that is also a suffix of the
        pattern sliced at the current position.

        :param pattern: The search pattern.
        :type pattern: str
        :return: Dictionary with each pattern index as key and length
            of the longest prefix of the pattern that is also a suffix
            of the pattern sliced at the current index as value.
        :rtype: Dict[int, int]
        """
        pattern_len = len(pattern)
        prefix_dict = {0: 0}
        good_prefix_len = 0

        for current_idx in range(1, pattern_len):
            while good_prefix_len > 0 and \
                  pattern[good_prefix_len] != pattern[current_idx]:
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
            
        
        
        


