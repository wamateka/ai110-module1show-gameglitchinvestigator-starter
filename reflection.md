# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  * the game alowed me to input a number and guess what the secret number was. when i guess the number and it's not correct, it would tell me whether i should go higher or lower, if the hint option is checked. If the guess number is correct, it would terminate the game. it also has options to choose difficulty.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  * Hints were not accurate (they are backwards)
  * can not start a new game after winning or losing  one game
  * The instruction heading does not have correct information after any setting change. eg. if you change the difficulty, the heading does not show the correct range and attempts for the current game
  * the attempts avariable is one more than the actuall attemps
  * easy difficulty level should have a higher number of attempts than normal difficulty level
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 * Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
* ai suggested a simpler logic for parse guess
* I run the code and worked as expect. It also passed the test
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
* none
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
 * If the logic made more sense. and the code works as expected and i run it
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  * I ran a test to check whether the secret us always within range. I ran it manually by changing the difficulty and checking wether it automatically updated.
- Did AI help you design or understand any tests? How?
* Yes. I broke down concepts, changes and suggestion in a way i can understand.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
* The secret number itself never actually changed — st.session_state.secret always held the same integer. What changed was how the secret was represented when compared to your guess.

On odd-numbered attempts, the secret was passed to check_guess as an integer (e.g., 42). On even-numbered attempts, it was converted to a string first (e.g., "42"). Python's check_guess function then compared your integer guess against that string using > and <.

When you compare a string to a string in Python, it uses lexicographic (alphabetical) ordering, not numeric ordering. So "5" > "42" is True because "5" comes after "4" alphabetically — even though 5 < 42 numerically. This made the hints appear to flip or give nonsensical direction every other guess, as if the target had moved
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you interact with a Streamlit app — click a button, type in a box — the entire Python script reruns from top to bottom.

That means any regular variable you set would be wiped out on the next interaction. session_state is a dictionary that persists across those reruns, so things like your score, attempts, and the secret number survive each time the script re-executes.
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
