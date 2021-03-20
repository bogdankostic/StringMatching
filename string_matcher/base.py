from abc import ABC, abstractmethod


class BaseMatcher(ABC):
    """
    Base class that all matcher classes should inherit from in order
    to ensure uniformity.
    """

    @abstractmethod
    def search(self, pattern: str, text: str):
        """
        Should return a list containing all indices where an instance
        of pattern starts in text.

        :param pattern: The search pattern.
        :type pattern: str
        :param text: The text string to search in.
        :type text: str
        :return: List with indices where occurrences of the search
            pattern start in the text.
        :rtype: List[int]
        """
        pass
