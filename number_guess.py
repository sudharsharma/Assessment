import streamlit as st
import random

if 'hidden_num' not in st.session_state:
    st.session_state.hidden_num = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10
    st.session_state.game_over = False

st.title(" Number Guessing Game")

st.markdown("""
    Guess the number between 1 and 100.
    You have a maximum of 10 attempts.
    After each guess, you'll receive feedback on whether your guess was too high, too low, or correct.
""")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    submit_button = st.button("Submit Guess")

    if submit_button:
        st.session_state.attempts += 1

        if guess < st.session_state.hidden_num:
            st.warning(f"Attempt {st.session_state.attempts}: {guess} is too low! Try again.")
        elif guess > st.session_state.hidden_num:
            st.warning(f"Attempt {st.session_state.attempts}: {guess} is too high! Try again.")
        else:
            st.success(f"Correct! You've guessed the number {st.session_state.hidden_num} in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

        if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
            st.error(f"Game Over! The correct number was {st.session_state.hidden_num}.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.hidden_num = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
