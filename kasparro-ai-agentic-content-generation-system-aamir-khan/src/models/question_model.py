from dataclasses import dataclass


@dataclass
class Question:
    """
    Represents a single user question with a category.
    """
    text: str
    category: str  # e.g. "informational", "usage", "safety", "purchase", "comparison"
