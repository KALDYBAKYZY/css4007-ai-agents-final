# Semester Week 12 Progress Report

## Completed Work

- Wrote two validators in `src/validators.py`:
  - `validate_month(month)` checks the format `YYYY-MM` and a real month (01–12).
  - `validate_category(category)` checks that the category is in the list of 10 categories.
- Wrote three tools in `src/tools.py`. They read the mock data in `data/`:
  - `get_transactions(month, category=None)` returns the transactions for a month, or for one category in a month.
  - `calculate_total(category, month)` returns the total spending and the number of transactions.
  - `get_budget(category)` returns the monthly limit for a category.
- All tools return a structured dictionary. If something is wrong, they return `{"error": "..."}` and do not crash.
- Added `pytest.ini` and the first 5 tests with pytest.
- Checked that all functions work without the LLM.

## Important Commits

- `e9b108d` — Add month and category validators — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/e9b108d
- `b9bae6e` — Add get_transactions tool with data loading — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/b9bae6e
- `d7dd1d5` — Add calculate_total and get_budget tools — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/d7dd1d5
- `2764027` — Add first pytest tests for validators and tools — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/2764027
- `9b4faa9` — Fix validators module content and imports — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/9b4faa9
- `5a9c991` — Add week 12 report — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/5a9c991

## Current Functionality

- The three tools work with the mock data. The LLM is not connected to the tools yet.
- Rules for errors and empty data:
  - Wrong month (for example `2026-13`) → error.
  - Unknown category (for example `pizza`) → error.
  - A month with no data at all (for example `2026-11`) → error "No data for 2026-11."
  - A month with data, but no spending in the category → total `0`. This is not an error.
- The tools clean the category before the check: `"Food "` becomes `"food"`.
- Manual check in the terminal (without the LLM):

```
calculate_total("food", "2026-10")
{'category': 'food', 'month': '2026-10', 'total': 51100, 'transaction_count': 12}

get_budget("food")
{'category': 'food', 'monthly_limit': 70000}

get_transactions("2026-11")
{'error': 'No data for 2026-11.'}

get_budget("pizza")
{'error': 'Unknown category: pizza.'}
```

- Test result: `pytest` → `5 passed`.

| Test | What it checks |
|---|---|
| `test_validate_month_accepts_correct_month` | `2026-10` is valid |
| `test_validate_month_rejects_wrong_month` | `2026-13`, `2026-9`, `October`, and a number are not valid |
| `test_validate_category` | `food` is valid, `pizza` is not valid |
| `test_calculate_total_food_october` | food in October 2026 = 51100 KZT, 12 transactions |
| `test_get_budget_unknown_category` | an unknown category returns an error |

## Problems Encountered

- My proposal had only 6 categories for `validate_category`. But the mock data and `budgets.json` have 10 categories. With 6 categories, a question about `phone` or `health` would give an error, even though the data exists.
- I first thought about checking the month with `datetime.strptime(month, "%Y-%m")`. But it accepts `2026-9`, and this is not the `YYYY-MM` format.
- The tests could not import `tools` and `validators`, because the code is in the `src/` folder.
- When I first ran `pytest`, both test files failed with `ImportError: ... circular import`. By mistake, `validators.py` had the line `from validators import ...`, so the module imported itself.

## Solutions

- I use all 10 categories from the data. This is a small change from the proposal.
- I check the month with a strict regular expression: 4 digits, a dash, and a month from 01 to 12.
- I added `pytest.ini` with `pythonpath = src`. Now pytest finds the code in `src/`.
- The data path is built from the location of `tools.py`, so the tools work from any folder.
- I removed the wrong import line from `validators.py`. After this fix, `pytest` showed `5 passed`.

## What I Learned

- Tools should return an error dictionary instead of raising an exception. Later the LLM can read the error and explain it to the user.
- "No data" and "zero spending" are different answers. The agent must not mix them.
- The same result format every time makes the tools easier to test and easier for the LLM to read.
- How to write simple pytest tests with `assert` and run them with `pytest`.

## Next Week

- Register the tools with the LLM (tool schemas).
- Let the LLM choose a tool and run the real tool call.
- Send the tool result back to the LLM for the final answer.
- Add more tests.