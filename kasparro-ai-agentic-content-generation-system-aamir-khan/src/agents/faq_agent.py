import json
from typing import Dict, Any, List
from src.template_engine.engine import TemplateEngine
from src.models.product_model import Product
from src.models.question_model import Question


class FAQAgent:
    def __init__(self, template: Dict[str, Any]):
        self.template = template

    def build(self, product: Product, questions: List[Question]) -> Dict[str, Any]:
        engine = TemplateEngine(self.template)

        # Prepare context
        context = {
            "product_name": product.name,
            "questions_list": [
                {"question": q.text, "category": q.category} for q in questions
            ]
        }

        return engine.render(context)
