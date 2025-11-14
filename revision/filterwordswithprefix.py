# all_words = ["cat", "car", "milk", "man"]
# partial_word = "c"

# res = []
# n = len(all_words)
# for i in range(n):
#     if all_words[i].startswith(partial_word):
#         res.append(all_words[i])

# print(res)

class Autocomplete:
    """A simple autocomplete tool."""

    def __init__(self, all_words: list[str]):
        """Constructor.
        Args:
            all_words: A list of all valid words. Words only include chars [a-z].
        """
        self.all_words = all_words  # Store the word list

    def get_predictions(self, partial_word: str) -> list[str]:
        """Returns a list of possible words that the user may be typing.

        Args:
            partial_word: the letters the user has typed so far for a given word.

        Returns:
            A list of words (from `all_words`) that the user could be typing. 
            All returned words have `partial_word` as a prefix.
        """
        # Filter words that start with the given prefix
        return [word for word in self.all_words if word.startswith(partial_word)]


# Example usage:
all_words = ["cat", "car", "milk", "man"]
autocomplete_tool = Autocomplete(all_words)

predictions = autocomplete_tool.get_predictions("c")
print(predictions)
