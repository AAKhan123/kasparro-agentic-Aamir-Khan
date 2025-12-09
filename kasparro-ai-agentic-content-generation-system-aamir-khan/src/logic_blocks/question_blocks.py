from typing import List
from src.models.product_model import Product
from src.models.question_model import Question


def generate_informational_questions(product: Product) -> List[Question]:
    return [
        Question(
            text=f"What is {product.name} and what does it do?",
            category="informational",
        ),
        Question(
            text=f"Who is {product.name} suitable for in terms of skin type?",
            category="informational",
        ),
        Question(
            text=f"What is the concentration of Vitamin C in {product.name}?",
            category="informational",
        ),
        Question(
            text=f"What are the key ingredients in {product.name}?",
            category="informational",
        ),
    ]


def generate_usage_questions(product: Product) -> List[Question]:
    return [
        Question(
            text=f"How should I use {product.name} in my daily skincare routine?",
            category="usage",
        ),
        Question(
            text="At what time of day should I apply this serum?",
            category="usage",
        ),
        Question(
            text="Can I use this serum with other active ingredients like retinol or AHA/BHA?",
            category="usage",
        ),
        Question(
            text="How many drops of the serum should I apply each time?",
            category="usage",
        ),
    ]


def generate_safety_questions(product: Product) -> List[Question]:
    return [
        Question(
            text="Is this serum safe for sensitive skin?",
            category="safety",
        ),
        Question(
            text="What kind of side effects or reactions should I watch out for?",
            category="safety",
        ),
        Question(
            text="Should I do a patch test before using this serum on my face?",
            category="safety",
        ),
        Question(
            text="Do I need to apply sunscreen while using this Vitamin C serum?",
            category="safety",
        ),
    ]


def generate_purchase_questions(product: Product) -> List[Question]:
    return [
        Question(
            text=f"What is the price of {product.name}?",
            category="purchase",
        ),
        Question(
            text="Is this serum value for money compared to other Vitamin C serums?",
            category="purchase",
        ),
        Question(
            text="How long will one bottle last with regular daily use?",
            category="purchase",
        ),
    ]


def generate_comparison_questions(product: Product) -> List[Question]:
    return [
        Question(
            text=f"How does {product.name} compare to other Vitamin C serums in terms of effectiveness?",
            category="comparison",
        ),
        Question(
            text="Is this serum better for oily/combination skin than thicker Vitamin C creams?",
            category="comparison",
        ),
    ]


def generate_all_questions(product: Product) -> List[Question]:
    """
    Aggregates questions from all logic blocks.
    Ensures we produce at least 15 questions in total.
    """
    questions: List[Question] = []
    questions.extend(generate_informational_questions(product))
    questions.extend(generate_usage_questions(product))
    questions.extend(generate_safety_questions(product))
    questions.extend(generate_purchase_questions(product))
    questions.extend(generate_comparison_questions(product))

    # Optionally, ensure uniqueness (no exact duplicates)
    unique = []
    seen = set()
    for q in questions:
        if q.text not in seen:
            unique.append(q)
            seen.add(q.text)

    return unique
