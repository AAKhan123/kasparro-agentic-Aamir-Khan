from typing import Dict, Any
from src.template_engine.engine import TemplateEngine
from src.models.product_model import Product
from src.logic_blocks.content_blocks import product_to_dict


class ProductPageAgent:
    def __init__(self, template: Dict[str, Any]):
        self.template = template

    def build(self, product: Product) -> Dict[str, Any]:
        engine = TemplateEngine(self.template)
        context = product_to_dict(product)
        return engine.render(context)
