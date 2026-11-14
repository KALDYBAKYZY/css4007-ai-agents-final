# Finly — Setup and Run

Finly is a personal finance assistant agent for students (CSS 4007 final project, level C).

## Requirements

- Python 3.10 or later
- An OpenAI API key

## Install

1. Clone the repository:

```bash
git clone https://github.com/KALDYBAKYZY/css4007-ai-agents-final.git
cd css4007-ai-agents-final
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows use `.venv\Scripts\activate`.

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configure

1. Copy the example file:

```bash
cp .env.example .env
```

2. Open `.env` and fill in your values:

```text
LLM_API_KEY=your-openai-api-key
LLM_MODEL=gpt-5.6-luna
```

The `.env` file is in `.gitignore`. Never commit your API key.

## Run

From the project folder:

```bash
python src/agent.py
```

Type a question and press Enter. Finly sends it to the model and prints the answer.

Example:

```text
You: Hello! Who are you?
Finly: ...
```