from pathlib import Path
from src.agents.data_parser_agent import DataParserAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent


def main():
    # Step 1: parse product
    parser = DataParserAgent(Path("data/product.json"))
    product = parser.run()

    # Step 2: generate questions
    q_agent = QuestionGeneratorAgent()
    questions = q_agent.run_as_dict(product)

    print(f"Total questions generated: {len(questions)}\n")
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. [{q['category']}] {q['question']}")


if __name__ == "__main__":
    main()
