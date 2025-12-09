## Multi-Agent Content Generation System – Project Documentation

This project implements a modular, multi-agent automation system designed to turn a small, structured product dataset into multiple machine-readable JSON content pages. The system emphasizes engineering design, clear agent responsibilities, and automated orchestration. It does not focus on UI or manual content writing, but rather on building a scalable backend-style content generation workflow.

The process starts with a simple product.json file containing information about a skincare product. Instead of handling everything in one script, the system splits the work into several independent agents, each responsible for a single, well-defined task. This mirrors real production environments, where clarity, modularity, and maintainability are more important than writing long monolithic code.

The first component is the DataParserAgent. Its only responsibility is to read the raw product JSON and convert it into a clean internal Product model. This model standardizes the structure of the data so that all downstream agents can rely on consistent types and fields.

Next, the QuestionGeneratorAgent analyzes the product model and automatically generates a set of more than fifteen user-oriented questions. These questions span different categories such as informational, usage, safety, purchase, and comparison. The question generation process is entirely deterministic and uses small reusable logic blocks, making it easy to extend or modify without touching the rest of the system.

A simple custom TemplateEngine is used to assemble final pages. It works using placeholder values like {{product_name}} and supports nested lists and objects. Despite being lightweight, the engine is flexible enough to plug in any template structure and produce clean JSON output. This approach ensures repeatability and separates content structure from content logic.

Three agents are responsible for building the final pages. The FAQAgent takes the product name and the generated questions and produces a structured FAQ page. The ProductPageAgent uses all fields of the product model—such as concentration, key ingredients, benefits, and usage instructions—to build a descriptive product page. The ComparisonAgent introduces a fictional Product B with its own structured fields and compares it to the main product, generating a comparison page that includes both product objects and a short comparison summary.

The entire workflow is controlled by an Orchestrator. It runs the pipeline step by step: parsing the input, generating questions, loading templates, building all three pages, and finally writing the output files to the output directory. This orchestrated flow demonstrates the use of agent-based automation, similar to real AI-powered content systems used in production environments.

A few assumptions guide the system design. It works with one product at a time, but its modular structure allows easy expansion to more products or more page types. Only the provided dataset is used; no external APIs or additional research are involved. The fictional Product B ensures that comparison pages are predictable and consistent. No machine learning or LLM models are required, which keeps the solution reproducible and easy to run anywhere.

The final result is a clean and well-structured automation pipeline that transforms raw product data into production-ready JSON pages. The use of agents, logic blocks, and a custom template engine highlights a thoughtful architectural approach. The system is simple, maintainable, and fully aligned with the goals of the assignment: engineering clarity, modularity, and real-world automation design.



           +------------------+
           |  product.json    |
           +---------+--------+
                     |
                     v
           +----------------------+
           |  DataParserAgent     |
           |  -> Product model    |
           +----------+-----------+
                      |
                      v
           +---------------------------+
           |  QuestionGeneratorAgent   |
           |  -> categorized questions |
           +----+----------------------+
                |
        +-------+-------------------------------+
        |                                       |
        v                                       v
+-------------------+                 +----------------------+
|      FAQAgent     |                 |  ProductPageAgent    |
|  + TemplateEngine |                 |  + TemplateEngine    |
+---------+---------+                 +----------+-----------+
          |                                     |
          v                                     v
   faq.json in output/                 product_page.json in output/

                      +-------------------------------+
                      |       ComparisonAgent         |
                      |     + TemplateEngine          |
                      +---------------+---------------+
                                      |
                                      v
                         comparison_page.json in output/