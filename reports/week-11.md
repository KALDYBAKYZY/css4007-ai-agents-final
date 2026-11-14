# Semester Week 11 Progress Report

## Completed Work

- Created a Python virtual environment (`.venv`) and installed the dependencies from `requirements.txt` (`openai`, `python-dotenv`).
- Created a local `.env` file with my API key and the model name (`gpt-5.6-luna`). I checked with `git status` that `.env` is not tracked by git.
- Wrote the first working request to the model in `src/agent.py` with the OpenAI Chat Completions API.
  - `ask_llm(message)` sends one user message to the model and returns the answer text.
  - `main()` asks the user for one question in the terminal and prints the answer.
- Found and fixed a bug: the API key was not loaded from `.env`.
- Wrote `SETUP.md` with steps to install, configure, and run Finly. I kept the instructor's `README.md` without changes.

## Important Commits

- `312ee6b` — Add first LLM request with OpenAI Chat Completions — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/312ee6b
- `f2fce1a` — Fix API key loading: read .env with python-dotenv — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/f2fce1a
- `0f50200` — Add setup and run instructions — https://github.com/KALDYBAKYZY/css4007-ai-agents-final/commit/0f50200
- Add week 11 report

## Current Functionality

- The application connects to the OpenAI API and gets a real answer from `gpt-5.6-luna`.
- The user runs `python src/agent.py`, types one question, and sees the model's answer.
- The API key and the model name are read from `.env`, not written in the code.
- The tools (`get_transactions`, `calculate_total`, `get_budget`) are not written yet. The agent cannot read the mock data yet.

## Problems Encountered

- My first version of `agent.py` did not work. It stopped with this error:
  `openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable`.
  The key was in `.env`, but `os.getenv("LLM_API_KEY")` returned `None`.
- VS Code showed a message that packages may be installed into the global Python environment.

## Solutions

- Python does not read the `.env` file by itself. I added `load_dotenv()` from the `python-dotenv` library. It reads `.env` and puts the values into environment variables. It must run before `OpenAI(...)` is created. After this fix the request worked.
- I created the virtual environment with `python3 -m venv .venv`, activated it with `source .venv/bin/activate`, and selected `.venv` as the interpreter in VS Code. Now the packages are installed only for this project.

## What I Learned

- How to send a request with the Chat Completions API: the model name and a list of messages with `role` and `content`. The answer text is in `response.choices[0].message.content`.
- Why secrets must be in `.env`: the key is not in the code and not in git. `.env.example` shows only the variable names.
- `.env` values are not loaded automatically. `load_dotenv()` must be called first.
- A virtual environment keeps the project's packages separate from other projects.

## Next Week

- Write the main functions: `get_transactions`, `calculate_total`, `get_budget`.
- Write `validate_month` and `validate_category`.
- Add the first 3–5 tests with pytest.
- Check that the functions work without the LLM.