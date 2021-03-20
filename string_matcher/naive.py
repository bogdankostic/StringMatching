
class NaiveMatcher:
    """
    Implements the naive string matching algorithm as it was outlined
    in Cormen et al.'s (1990) 'Introduction to Algorithms'.
    """

    def __init__(self, case_sensitive: bool = True):
        """
        Instantiates a NaiveMatcher instance.

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

        correct_shifts = []
        text_len = len(text)
        pattern_len = len(pattern)

        # Iterate over each position in the text and check if an instance of the
        # search pattern starts at the current index
        for shift in range(text_len - pattern_len + 1):
            candidate_match = text[shift:shift+pattern_len]
            if pattern == candidate_match:
                # Correct match, i.e. an instance of search pattern starts at
                # current index
                correct_shifts.append(shift)

        return correct_shifts
