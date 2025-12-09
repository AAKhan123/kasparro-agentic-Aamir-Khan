from typing import Dict, Any
from src.template_engine.engine import TemplateEngine
from src.models.product_model import Product
from src.logic_blocks.content_blocks import (
    product_to_dict,
    generate_comparison_summary
)


class ComparisonAgent:
    def __init__(self, template: Dict[str, Any]):
        self.template = template

    def build(self, product_a: Product) -> Dict[str, Any]:
        # Create fictional Product B
        product_b = {
            "name": "RadiantPlus Vitamin C Serum",
            "key_ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Evens Skin Tone"],
            "price": "₹799"
        }

        engine = TemplateEngine(self.template)

        context = {
            "product_a": product_to_dict(product_a),
            "product_b": product_b,
            "comparison_summary": generate_comparison_summary(product_a, product_b)
        }

        return engine.render(context)
