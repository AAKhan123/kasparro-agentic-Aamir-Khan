from dataclasses import dataclass
from typing import List
import json
from pathlib import Path


@dataclass
class Product:
    """
    Internal product representation used by all agents.
    """
    name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str


def load_product_from_json(path: str | Path) -> Product:
    """
    Loads product data from a JSON file and converts it
    into the internal Product model.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    return Product(
        name=raw["product_name"],
        concentration=raw["concentration"],
        skin_type=raw["skin_type"],
        key_ingredients=raw["key_ingredients"],
        benefits=raw["benefits"],
        how_to_use=raw["how_to_use"],
        side_effects=raw["side_effects"],
        price=raw["price"],
    )
