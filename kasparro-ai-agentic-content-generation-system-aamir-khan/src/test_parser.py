from src.agents.data_parser_agent import DataParserAgent
from pathlib import Path


def main():
    agent = DataParserAgent(Path("data/product.json"))
    product = agent.run()
    print(product)


if __name__ == "__main__":
    main()
