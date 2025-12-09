from pathlib import Path
from src.models.product_model import Product, load_product_from_json



class DataParserAgent:
    """
    Agent responsible for:
    - Reading raw product JSON
    - Validating basic fields (optionally)
    - Returning a clean Product model instance
    """

    def __init__(self, data_path: str | Path):
        self.data_path = Path(data_path)

    def run(self) -> Product:
        if not self.data_path.exists():
            raise FileNotFoundError(f"Product data file not found: {self.data_path}")

        product = load_product_from_json(self.data_path)
        return product
