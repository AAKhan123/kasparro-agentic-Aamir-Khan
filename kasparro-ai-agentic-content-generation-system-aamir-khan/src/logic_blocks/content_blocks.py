from typing import Dict, Any
from src.models.product_model import Product


def product_to_dict(product: Product) -> Dict[str, Any]:
    """
    Converts a Product object into a plain dict for template filling.
    """
    return {
        "product_name": product.name,
        "concentration": product.concentration,
        "skin_type": ", ".join(product.skin_type),
        "key_ingredients": ", ".join(product.key_ingredients),
        "benefits": ", ".join(product.benefits),
        "how_to_use": product.how_to_use,
        "side_effects": product.side_effects,
        "price": product.price
    }


def generate_comparison_summary(product_a: Product, product_b: Dict[str, Any]) -> str:
    """
    Simple comparison logic:
    - Compares ingredients
    - Compares benefits
    - Compares price
    """
    summary = (
        f"{product_a.name} contains {', '.join(product_a.key_ingredients)} "
        f"while {product_b['name']} contains {', '.join(product_b['key_ingredients'])}. "
        f"{product_a.name} is priced at {product_a.price}, "
        f"while {product_b['name']} costs {product_b['price']}."
    )
    return summary
