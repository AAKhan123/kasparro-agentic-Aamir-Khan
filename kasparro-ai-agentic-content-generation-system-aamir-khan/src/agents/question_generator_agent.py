from typing import List, Dict
from src.models.product_model import Product
from src.models.question_model import Question
from src.logic_blocks.question_blocks import generate_all_questions


class QuestionGeneratorAgent:
    """
    Agent responsible for:
    - Taking a Product
    - Generating categorized user questions using reusable logic blocks
    - Returning a structured list of questions
    """

    def run(self, product: Product) -> List[Question]:
        return generate_all_questions(product)

    def run_as_dict(self, product: Product) -> List[Dict[str, str]]:
        """
        Convenience method: returns plain dicts,
        easier to serialize to JSON later.
        """
        questions = self.run(product)
        return [
            {"question": q.text, "category": q.category}
            for q in questions
        ]
