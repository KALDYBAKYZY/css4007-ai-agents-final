# Project Proposal — Semester Week 10

## Project Title

Finly — Personal Finance Assistant Agent

## Problem Description

Many students do not know how much money they spend and on what. Bank statements are hard and slow to read. Simple apps show charts, but you cannot ask them a question.
 
Finly is an AI agent. The user asks a question in simple English, for example: "How much did I spend on food in October?" The agent chooses a tool, reads the data, and gives an answer.
 
Why this is important:
- The answer needs correct numbers, not a guess from the model.
- The model does not know my transactions, so it must call tools to get them.
I use **mock (test) data only**. No real bank data.

## Target Users

- University students who want to track their spending.
- Anyone who wants a quick answer about their budget.   

## Selected Difficulty

C level

## Expected Functionality

1. The user asks a question in a command-line chat.
2. The LLM chooses a tool (or no tool for general questions).
3. The code checks the tool arguments before running the tool.
4. The tool reads mock data and returns a result.
5. The LLM writes the final answer using only the tool result.
6. The agent handles errors: wrong category, wrong month, no data, tool error, API error.
7. The agent answers general questions without tools (for example, "What can you do?").
8. Every tool call is saved in a log file.

## Proposed Functions

Data files: `data/transactions.json`, `data/budgets.json`. Currency: KZT. Month format: `YYYY-MM`.
 
**Tools (the LLM can call them):**
 
1. `get_transactions(month, category=None) -> list`
   - Returns transactions for a month (and one category, if given).
   - Output: date, category, description, amount. Or an error dictionary.
2. `calculate_total(category, month) -> dict`
   - Returns the total spending for a category in a month.
   - Output: `{"category", "month", "total", "transaction_count"}` or an error.
3. `get_budget(category) -> dict`
   - Returns the monthly limit for a category.
   - Output: `{"category", "monthly_limit"}` or an error ("Budget not found").
**Helper functions (not tools):**
 
4. `validate_month(month) -> bool` — checks the format `YYYY-MM` and a real month.
5. `validate_category(category) -> bool` — checks the category: food, transport, entertainment, education, shopping, rent.
6. `validate_tool_args(tool_name, args) -> dict` — checks required fields, types, and values.
7. `execute_tool(tool_name, args) -> dict` — validates, runs the tool, catches errors, logs the call.
8. `log_tool_call(tool_name, args, result, error)` — writes one line to `logs/tool_calls.log`. It never logs API keys.
9. `run_agent(user_message) -> str` — main loop: send message and tool schemas to the LLM, run tools, send results back, return the final answer.
10. `main()` — command-line chat loop.

## Proposed Agent Tools
 
| Tool | Why the agent needs it |
|---|---|
| `get_transactions` | The model does not know my transactions. |
| `calculate_total` | LLMs make math mistakes. The tool gives a correct sum. |
| `get_budget` | The agent needs the limit to answer "Did I go over budget?" It uses this with `calculate_total`. |
 
The LLM chooses the tools. The code does not use keyword matching.

## Model Selection

- Provider: OpenAI API, with function calling (tool calling).
- Model: `gpt-5.6-luna` (GPT Luna). It is a small and cheap model with function calling support.
- I will use this one model and this one version for the whole project. This keeps test results and reports comparable. I will check that the model name works with my API key in Week 11.
- The model name is stored in `.env` (`LLM_MODEL`), not in the code.
- The API key is in a `.env` file (not committed). `.env.example` has only the variable name.

## Architecture

```
User Request
     |
     v
   LLM (OpenAI, with tool schemas)
     |
     +--> no tool needed --> Answer
     |
     v
Tool Selection (LLM chooses tool + arguments)
     |
     v
Argument Validation (month, category, types)
     |   invalid --> error sent back to LLM
     v
Tool Execution (reads mock JSON data)
     |
     v
Logging (logs/tool_calls.log)
     |
     v
Tool result sent back to LLM
     |
     v
LLM writes final answer (only from tool results)
```

Project structure:
```
src/      agent.py, tools.py, validators.py, logger.py
data/     transactions.json, budgets.json
tests/    test_tools.py, test_validators.py, test_agent.py
logs/     tool_calls.log (not committed)
reports/  proposal.md, week-10.md ... week-17.md, final-report.md
```


## Example Requests

1. "How much did I spend on food in October 2026?" → `calculate_total`
2. "Did I go over my transport budget in October 2026?" → `calculate_total` + `get_budget`
3. "Show me all my entertainment transactions in September 2026." → `get_transactions`
4. "How much did I spend on pets in October?" → category does not exist. The agent says this and shows the valid categories.
5. "What can you help me with?" → no tool
6. "How much did I spend in March 2020?" → no data. The agent does not invent numbers.

## Evaluation Plan

I will use `pytest`. Tool tests use fixed mock data. Agent tests use a mocked LLM client. Target: 10+ tests (minimum 8).
 
1. `calculate_total` gives the correct sum.
2. `get_transactions` gives the correct list.
3. `get_budget` gives the correct limit.
4. Unknown category returns an error.
5. `validate_month` rejects bad formats (`"October"`, `"2026-13"`).
6. Wrong or missing arguments are rejected before the tool runs.
7. A month with no data returns a clear "no data" result.
8. The agent chooses `calculate_total` for a spending question.
9. The agent answers without a tool when no tool is needed.
10. A tool failure gives a safe message.
11. An API failure does not crash the agent.
12. A tool call is written to the log, and the log has no API key.
I will also check by hand that the final answers match the tool results. I will write the results in `reports/week-16.md`.


## Weekly Milestones

- **Week 10 (2–8 Nov):** Fork repo, write proposal, create structure and mock data.
- **Week 11 (9–15 Nov):** Set up `.env` and dependencies. First OpenAI request. Basic README.
- **Week 12 (16–22 Nov):** Write the 3 tools and validators. First tests.
- **Week 13 (23–29 Nov):** Register tools with the LLM. Run tools and return results to the LLM.
- **Week 14 (30 Nov–6 Dec):** Full workflow (multi-tool questions). Error handling. Logs.
- **Week 15 (7–13 Dec):** Make it more reliable. Edge cases. At least 8–10 tests.
- **Week 16 (14–20 Dec):** Run all tests. Write `reports/week-16.md`. Fix failures. Update docs.
- **Week 17 (21–22 Dec):** Final README, final report, final commit hash. Demo and defense.
I will make 2–4 commits each week and write a weekly report. If the plan changes, I will write it in the report.

For each function give its name, purpose, inputs, outputs, and dependencies. For C/A identify model-callable tools and their purpose; D may write “Not applicable — D level”. Give at least three example requests and milestones for Weeks 10–17.

## AI Assistant Use
 
I will use AI coding assistants for help. I will test all generated code, understand it, and explain it in the defense. I will describe the AI use in the final statement.