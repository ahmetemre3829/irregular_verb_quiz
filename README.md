# Irregular Verb Quiz

This Python script is a simple command-line quiz designed to help you learn irregular verbs in English, with Turkish meanings provided for context. It uses the `colorama` library for colored text output and `msvcrt` for waiting for user input before exiting.

## Features

- **Randomized Quizzes:** The quiz selects random irregular verbs from a predefined list.
- **Interactive Gameplay:** The user is prompted to enter the past simple and past participle forms of the verb.
- **Feedback:** The script provides immediate feedback, indicating whether the answer is correct or incorrect and displaying the correct answer.
- **Customizable Quiz Length:** Users can choose how many verbs they want to be quizzed on.
- **Score Tracking:** The quiz keeps track of the user's correct and wrong answers.
- **Colored Output:** The use of `colorama` makes the text output more engaging and readable.
- **Multi-Platform:** It's designed to work on Windows due to using msvcrt library for waiting for a key press but can also work on other platforms without this feature

## Prerequisites

- **Python 3.x**
- **colorama** library

    You can install `colorama` using pip:

    ```bash
    pip install colorama
    ```
- **msvcrt** library

    This library is only used for Windows, can be removed or modified for other systems
