
from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression: check_guess type normalization bug ---
# Bug: secret was sometimes stored/passed as a string (e.g. "50"), causing
# int vs str comparisons to always return "Too Low" or "Too High" even on
# a correct guess.

def test_check_guess_secret_as_string_correct():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_secret_as_string_too_high():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_secret_as_string_too_low():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"


# --- Regression: update_score failed-attempt penalty bug ---
# Bug: failed attempts were adding to the score instead of subtracting.

def test_update_score_too_high_decreases_score():
    new_score = update_score(50, "Too High", attempt_number=2)
    assert new_score < 50

def test_update_score_too_low_decreases_score():
    new_score = update_score(50, "Too Low", attempt_number=3)
    assert new_score < 50

def test_update_score_no_negative_scores():
    # Penalty should floor at 0, not go negative.
    new_score = update_score(3, "Too High", attempt_number=1)
    assert new_score >= 0

def test_update_score_win_increases_score():
    new_score = update_score(0, "Win", attempt_number=1)
    assert new_score > 0


# --- Regression: parse_guess edge cases ---
# Bug: old version had unnecessary steps that could mishandle float strings
# like "3.7" or whitespace-only input.

def test_parse_guess_float_string_truncates():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
