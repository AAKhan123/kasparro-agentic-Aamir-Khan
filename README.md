# kasparro-agentic-Aamir-Khan

# Multi-Agent Content Generation System

This project is a small **multi-agent automation system**.  
It takes one product's data (a Vitamin C serum) and automatically creates:

- an FAQ page (as JSON)
- a Product Description page (as JSON)
- a Comparison page (as JSON)
- 
## 1. What this project does (in simple words)

1. Reads product details from `data/product.json`
2. Converts it into a Python `Product` object
3. Generates more than 15 user questions about the product (usage, safety, etc.)
4. Uses templates to build:
   - `faq.json`
   - `product_page.json`
   - `comparison_page.json`
5. Saves these JSON files into the `output` folder.

You can think of it as a small content engine:
**input: product → output: multiple content pages in JSON.**


## 2. Project structure

Your folder structure looks like this:

```text
.
├── data/
│   └── product.json                 # Input product data (GlowBoost Vitamin C Serum)
│
├── docs/
│   └── projectdocumentation.md      # Written explanation of the system
│
├── output/
│   ├── faq.json                     # Generated FAQ page
│   ├── product_page.json            # Generated Product page
│   └── comparison_page.json         # Generated Comparison page
│
├── src/
│   ├── __init__.py
│   ├── orchestrator.py              # Main file that runs everything
│   │
│   ├── agents/                      # All agents (workers)
│   │   ├── __init__.py
│   │   ├── data_parser_agent.py     # Reads product.json -> Product model
│   │   ├── question_generator_agent.py
│   │   ├── faq_agent.py
│   │   ├── product_page_agent.py
│   │   └── comparison_agent.py
│   │
│   ├── logic_blocks/                # Reusable logic functions
│   │   ├── __init__.py
│   │   ├── question_blocks.py       # Functions to generate questions
│   │   └── content_blocks.py        # Functions to prepare product data & comparisons
│   │
│   ├── models/                      # Data models
│   │   ├── __init__.py
│   │   ├── product_model.py         # Product dataclass + loader
│   │   └── question_model.py        # Question dataclass
│   │
│   ├── template_engine/             # Custom mini template system
│   │   ├── __init__.py
│   │   └── engine.py                # Replaces {{placeholders}} in templates
│   │
│   └── templates/                   # Page templates
│       ├── __init__.py
│       ├── faq_template.json
│       ├── product_template.json
│       └── comparison_template.json
│
└── README.md                        # This file
````

---

## 3. Requirements

* Python 3.10+ (recommended)
* No external libraries required (only Python standard library is used)

You **do not need** to install `openai`, `numpy`, etc.

If you want to create a virtual environment (optional but good practice):

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

No `pip install` is needed for this project.

---

## 4. How to run the project

### Step 1: Go to the project folder

In terminal (or VS Code terminal):

```bash
cd path/to/your/project
# for example:
cd C:\Users\Admin\Desktop\kasparro-ai-agentic-content-generation-system-aamir-khan
```

### Step 2: Run the orchestrator

```bash
python -m src.orchestrator
```

If everything is correct, you will see logs like:

```text
🚀 Starting orchestration pipeline...
📥 Parsing product data...
❓ Generating categorized questions...
📄 Loading templates...
🧩 Building FAQ page...
🧴 Building Product page...
⚖️ Building Comparison page...
✅ Pipeline complete.
   - FAQ: output/faq.json
   - Product Page: output/product_page.json
   - Comparison Page: output/product_page.json
```

---

## 5. Where to see the output

After running the command above, open the `output` folder:

```text
output/
├── faq.json
├── product_page.json
└── comparison_page.json
```

You can open these files in VS Code:

* `faq.json`
  Contains the FAQ page:

  * `page_type`
  * `title`
  * `questions` (list of `{ question, category }`)

* `product_page.json`
  Contains the main product information:

  * `name`
  * `concentration`
  * `skin_type`
  * `key_ingredients`
  * `benefits`
  * `how_to_use`
  * `side_effects`
  * `price`

* `comparison_page.json`
  Contains:

  * `product_a` (GlowBoost Vitamin C Serum)
  * `product_b` (a fictional competing serum)
  * `comparison_summary` (short text comparing both)

---

## 6. Simple explanation of the system

* The **DataParserAgent** reads the product JSON and creates a `Product` object.
* The **QuestionGeneratorAgent** generates more than 15 questions about the product.
* The **TemplateEngine** fills JSON templates using placeholder values like `{{product_name}}`.
* The **FAQAgent**, **ProductPageAgent**, and **ComparisonAgent** each build one page.
* The **Orchestrator** is the “boss” that calls all these agents in the correct order and writes the final JSON files.

