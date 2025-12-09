import json
from pathlib import Path
from typing import Dict, Any

from src.agents.data_parser_agent import DataParserAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent
from src.agents.faq_agent import FAQAgent
from src.agents.product_page_agent import ProductPageAgent
from src.agents.comparison_agent import ComparisonAgent


# ---------- Helper functions ----------

def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------- Orchestrator ----------

class Orchestrator:
    """
    Coordinates the entire pipeline:
    1. Parse product data
    2. Generate questions
    3. Build FAQ page
    4. Build Product page
    5. Build Comparison page
    6. Save all as JSON
    """

    def __init__(self):
        self.project_root = Path(".")  # assuming we run from project root

        # Paths
        self.data_path = self.project_root / "data" / "product.json"
        self.templates_path = self.project_root / "src" / "templates"
        self.output_path = self.project_root / "output"

    def run(self):
        print("🚀 Starting orchestration pipeline...")

        # 1. Parse product
        print("📥 Parsing product data...")
        parser = DataParserAgent(self.data_path)
        product = parser.run()

        # 2. Generate questions
        print("❓ Generating categorized questions...")
        q_agent = QuestionGeneratorAgent()
        questions = q_agent.run(product)

        # 3. Load templates
        print("📄 Loading templates...")
        faq_template = load_json(self.templates_path / "faq_template.json")
        product_template = load_json(self.templates_path / "product_template.json")
        comparison_template = load_json(self.templates_path / "comparison_template.json")

        # 4. Build FAQ page
        print("🧩 Building FAQ page...")
        faq_agent = FAQAgent(faq_template)
        faq_page = faq_agent.build(product, questions)
        save_json(self.output_path / "faq.json", faq_page)

        # 5. Build Product page
        print("🧴 Building Product page...")
        product_page_agent = ProductPageAgent(product_template)
        product_page = product_page_agent.build(product)
        save_json(self.output_path / "product_page.json", product_page)

        # 6. Build Comparison page
        print("⚖️ Building Comparison page...")
        comparison_agent = ComparisonAgent(comparison_template)
        comparison_page = comparison_agent.build(product)
        save_json(self.output_path / "comparison_page.json", comparison_page)

        print("✅ Pipeline complete.")
        print(f"   - FAQ: {self.output_path / 'faq.json'}")
        print(f"   - Product Page: {self.output_path / 'product_page.json'}")
        print(f"   - Comparison Page: {self.output_path / 'comparison_page.json'}")


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run()
