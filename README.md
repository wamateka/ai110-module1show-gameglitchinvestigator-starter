# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose

A number guessing game built with Streamlit where the player tries to guess a secret number within a chosen difficulty range (Easy: 1–20, Normal: 1–50, Hard: 1–100). The player has a limited number of attempts and receives hints after each wrong guess. Points are awarded for winning, with a bonus for guessing in fewer attempts.

### Bugs Found

1. **Backwards hints** — The "Go Higher" and "Go Lower" hint messages were swapped, so the game actively misled the player.
2. **Secret number reset on every click** — The secret was generated with `random.randint()` at the top level of the script, so every Streamlit rerun (triggered by any button click) picked a new number, making the game impossible to win.
3. **No way to start a new game** — After winning or losing, the app had no reset mechanism; the game was stuck in a finished state with no way to play again.
4. **Instruction heading out of sync with difficulty** — The displayed range and attempt count did not update when the player changed difficulty mid-session.
5. **Attempts counter off by one** — The attempt count was incremented twice on a valid guess (once unconditionally, once inside the `if not ok` branch's else), so the displayed remaining attempts was always one lower than the actual count.
6. **Type inconsistency on secret** — The secret was alternately cast to `str` and `int` depending on the attempt parity, causing correct guesses to be treated as misses.

### Fixes Applied

- **State bug**: Wrapped the secret generation in `if "secret" not in st.session_state` so it is only generated once and persists across reruns. Added similar guards for `attempts`, `score`, `status`, and `history`.
- **Hint logic**: Fixed `check_guess()` in `logic_utils.py` — when `guess > secret` the outcome is `"Too High"` (go lower), and when `guess < secret` the outcome is `"Too Low"` (go higher).
- **New Game button**: Added a "New Game" button that resets all session state keys and calls `st.rerun()`.
- **Range guard**: Added a check after difficulty changes — if the stored secret falls outside the new difficulty range, a fresh secret is generated for that range.
- **Double-increment fix**: Removed the extra `st.session_state.attempts += 1` that fired before input validation, keeping only the single increment inside the valid-guess path.
- **Type fix**: Removed the even/odd `str`/`int` casting glitch; `secret` is now always read as `st.session_state.secret` (an int) and both values are explicitly cast with `int()` inside `check_guess()`.
- **Refactor**: Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py` for testability, then verified all functions with `pytest`.

## 📸 Demo

- [./image.png] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
