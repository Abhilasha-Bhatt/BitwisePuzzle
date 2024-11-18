# Bitwise Puzzle Dashboard

## Overview
The **Bitwise Puzzle Dashboard** is an interactive command-line game designed to test your knowledge of bitwise operations. Players can solve puzzles involving bitwise operators, manage their high scores, and even customize the dashboard theme for a personalized experience.

---

## Features
1. **Learn the Rules:**
   - A detailed explanation of the game's rules and an example to understand how bitwise operations work.

2. **Puzzle Dashboard:**
   - Solve puzzles using random bitwise operations like AND (`&`), OR (`|`), XOR (`^`), right-shift (`>>`), and NOT (`~`).
   - Three difficulty levels:
     - Easy: Single-digit numbers.
     - Medium: Two-digit numbers.
     - Hard: Three-digit numbers and more complex operations.

3. **Theme Customization:**
   - Customize the color of the dashboard with options like Red, Green, Yellow, and Blue.

4. **Scoring System:**
   - Gain points for correct answers and lose points for incorrect ones.
   - High scores are tracked and displayed.

5. **Intuitive Navigation:**
   - User-friendly menu for easy navigation through features.

---

## How to Play

### Menu Options
1. **Know the Features/Rules:**
   - Displays the rules of the game with an example of a bitwise operation.

2. **Start the Puzzle:**
   - Enter the puzzle dashboard and choose a difficulty level.
   - Solve randomly generated bitwise questions.
   - Continue playing until you decide to exit the puzzle dashboard.

3. **Change the Theme:**
   - Select a color theme for the dashboard: Red, Green, Yellow, or Blue.

4. **Exit:**
   - Quit the game and display your highest score.

### Bitwise Operators Used
- **AND (`&`):** Combines binary digits of two numbers using logical AND.
- **OR (`|`):** Combines binary digits of two numbers using logical OR.
- **XOR (`^`):** Combines binary digits of two numbers using logical XOR.
- **Right-Shift (`>>`):** Shifts binary digits of a number to the right.
- **NOT (`~`):** Flips the binary digits of a number (used only in hard mode).

---

## System Requirements
- Python 3.6 or higher
- Terminal or Command Prompt that supports ANSI escape codes for colored output.

---

## How to Run
1. Save the script to a `.py` file, e.g., `bitwise_puzzle.py`.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```bash
   python bitwise_puzzle.py
   ```

---

## Customization
You can modify the following:
- **Default Theme Color:** Change the value of `color_code` at the beginning of the script. (31: Red, 32: Green, 33: Yellow, 34: Blue)
- **Difficulty Levels:** Adjust the ranges in the `if level ==` conditions to customize number ranges.

---

## Example Gameplay

### Menu
```plaintext
WELCOME TO BITWISE PUZZLE DASHBOARD

Enter:
[1] --> Know the features/rules
[2] --> Start the puzzle
[3] --> Change the theme of dashboard
[0] --> Exit
```

### Puzzle Example
```plaintext
BITWISE PUZZLE DASHBOARD
SCORE = 0
5 & 3 = 
Your Answer: 1
CORRECT!
SCORE = 1
```

---

## Notes
- Ensure the terminal supports ANSI codes for colors.
- Input validation is implemented to prevent errors from invalid entries.
- Customize the questions and theme colors as per your preferences.

## Credits
Created by [![ABHILASHA](https://img.shields.io/badge/ABHILASHA-Profile-blue?style=for-the-badge)](https://www.linkedin.com/in/abhilasha-bhatt3/)
. This project is a simple implementation of Minesweeper for practice with C programming.

## Contacts

[![Gmail](https://img.shields.io/badge/-Gmail-D14836?logo=gmail&logoColor=white&style=for-the-badge)](mailto:abhilashabhatt77@gmail.com)


[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&logoColor=white&style=for-the-badge)](https://www.linkedin.com/in/abhilasha-bhatt3/)

[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=for-the-badge)](https://github.com/Abhilasha-Bhatt)


Feel free to modify or extend this game!
