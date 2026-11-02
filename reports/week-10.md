# Semester Week 10 Progress Report

## Completed Work

- Forked the instructor repository.
- Chose the project: Finly, a personal finance assistant agent for students (difficulty C).
- Wrote and checked the project proposal (`reports/proposal.md`). `npm run proposal` passes.
- Created the project structure: `src/`, `data/`, `tests/`, `logs/`.
- Created empty files for the code (`agent.py`, `tools.py`, `validators.py`, `logger.py`) and for the tests.
- Created mock data for a student in Almaty (KZT): `data/transactions.json` (85 transactions for September and October 2026) and `data/budgets.json` (10 categories).
- Added requirements.txt and updated .gitignore.
- Chose the model: `gpt-5.6-luna` (one model for the whole project).

## Important Commits

- `d84ea46` — Add project proposal
- `1345aa4` — Add project structure
- `7764752` — Add mock transactions and budgets data
- Add week 10 report

## Current Functionality

The application code is not written yet. This week I prepared the plan and the data.
- The proposal defines 3 tools (`get_transactions`, `calculate_total`, `get_budget`) and 7 helper functions.
- The mock data is ready. Categories: food, transport, rent, utilities, phone, entertainment, subscriptions, education, shopping, health.
- Known totals are ready for tests (for example, entertainment in October 2026 is 23000 KZT, the budget is 20000 KZT).

## Problems Encountered

No big problems this week. The main problem was the project structure. I was not sure which files and folders I need to create, so that there is nothing extra, but I also do not miss anything important. I was not sure which files in the instructor repository I can delete and which ones I must keep.

## Solutions
 
I read the repository README and C.md to see the required files and the level C requirements.
I kept all required folders and files (reports/, scripts/, .github/workflows/, README.md, C.md) and did not delete anything from the instructor repository.
I made my project structure from the proposal. I created only the files that my functions and tests need: 4 files in src/, 3 test files in tests/, 2 data files in data/, and requirements.txt.

## What I Learned
 
- An agent needs tools because the LLM does not know the user's data and can make math mistakes.
- It is better to plan functions, tests and test data before writing code.
- Mock data with known totals makes tests simple and stable.

## Next Week
 
- Set up the environment (`.env`, dependencies).
- Connect to the OpenAI API and make the first working request.
- Write a basic README with setup steps.