import random

color_code = 32  # Green
high_score = 0

while True:
    # Clear the screen before displaying the main menu
    print("\033[2J\033[H", end="")
    
    text = (
        "\n***************************************************\t\n"
        "\tWELCOME TO BITWISE PUZZLE DASHBOARD\t\n"
        "***************************************************\n\n"
        "Enter:\n[1] --> Know the features/rules\n[2] --> Start the puzzle\n"
        "[3] --> Change the theme of dashboard\n[0] --> Exit\n"
    )
    print(f"\033[{color_code}m{text}\033[0m")

    # Menu choice input
    choice = input("Enter your choice: ")
    if not choice.isdigit():
        print("\033[31mInvalid input. Please enter a valid number.\033[0m")
        continue
    choice = int(choice)

    # Rules
    if choice == 1:
        # Clear the screen before showing rules
        print("\033[2J\033[H", end="")
        
        rule = (
            "\n=================================================\n"
            "\t\tRules\n"
            "=================================================\n"
            "# You will choose a bitwise operator\n"
            "# For the bitwise operator you choose, you will be given 5 questions\n"
            "# For each expression, input your answer\n"
            "# Correct answers increase your score, wrong answers decrease it\n"
            "\nExample:\n  5 & 3 = 1\n  (Binary: 0101 & 0011 = 0001)\n"
        )
        print(f"\033[{color_code}m{rule}\033[0m")
        input("Press Enter to return to the home screen...")

    # Puzzle Dashboard
    elif choice == 2:
        exit_dashboard = 'n'
        score = 0
        while exit_dashboard == 'n':
            # Clear the screen before showing the puzzle dashboard
            print("\033[2J\033[H", end="")
            
            text2 = (
                "\n=================================================\n"
                "\t\tBITWISE PUZZLE DASHBOARD\n"
                "=================================================\n\n"
            )
            print(f"\033[{color_code}m{text2}\033[0m")

            level = input("[1] for easy mode\n[2] for medium mode\n[3] for hard mode\nEnter mode: ")
            if not level.isdigit():
                print("\033[31mInvalid input. Please enter a valid number.\033[0m")
                continue
            level = int(level)

            exit_mode = 'y'
            while exit_mode == 'y':
                # Clear the screen before showing the current question
                print("\033[2J\033[H", end="")
                
                print(f"\033[{color_code}m{text2}\033[0m")
                print("SCORE =", score)

                # Generate random operator and operands based on level
                if level == 1:
                    op1, op2 = random.randint(1, 9), random.randint(1, 9)
                elif level == 2:
                    op1, op2 = random.randint(10, 99), random.randint(10, 99)
                elif level == 3:
                    op1, op2 = random.randint(100, 999), random.randint(10, 99)
                else:
                    print("\033[31mInvalid level! Returning to main menu.\033[0m")
                    break

                operator = random.randint(1, 5)
                if operator == 1:
                    print(f"{op1} & {op2} = ", end="")
                    correct_answer = op1 & op2
                elif operator == 2:
                    print(f"{op1} | {op2} = ", end="")
                    correct_answer = op1 | op2
                elif operator == 3:
                    print(f"{op1} ^ {op2} = ", end="")
                    correct_answer = op1 ^ op2
                elif operator == 4:
                    print(f"{op1} >> {op2} = ", end="")
                    correct_answer = op1 >> op2
                elif operator == 5 and level == 3:  # Include NOT only in hard mode
                    print(f"~{op1} = ", end="")
                    correct_answer = ~op1
                    op2 = None  # Not used in NOT operator

                ans = input()
                if not ans.isdigit() and not (ans.startswith('-') and ans[1:].isdigit()):
                    print("\033[31mInvalid input. Please enter a valid number.\033[0m")
                    continue
                ans = int(ans)

                if ans == correct_answer:
                    print(f"\033[{color_code}mCORRECT!\033[0m")
                    score += 1
                else:
                    print(f"\033[{color_code}mCORRECT IS: {correct_answer}\033[0m")
                    score -= 1

                exit_mode = input("Would you like another question [y/n]? ").lower()

            exit_dashboard = input("Would you like to exit the puzzle dashboard [y/n]? ").lower()

        # Update high score
        if score > high_score:
            high_score = score
            print(f"\033[{color_code}mNEW HIGH SCORE: {high_score}!\033[0m")
        print(f"\033[{color_code}mTOTAL SCORE: {score}\033[0m\n")

    # Change Theme
    elif choice == 3:
        while True:
            # Clear the screen before showing the theme menu
            print("\033[2J\033[H", end="")
            
            text3 = (
                "\n=================================================\n"
                "\t\tCHANGE THEME\n"
                "=================================================\n\n"
                "Choose a color: \n[31] Red\n[32] Green\n[33] Yellow\n[34] Blue\n"
            )
            print(f"\033[{color_code}m{text3}\033[0m")

            new_color = input("Enter your choice for color: ")
            if not new_color.isdigit() or int(new_color) not in [31, 32, 33, 34]:
                print("\033[31mInvalid choice. Please choose a valid color.\033[0m")
            else:
                color_code = int(new_color)
                break

    # Exit
    elif choice == 0:
        confirm_exit = input("Are you sure you want to exit? [y/n]: ").lower()
        if confirm_exit == 'y':
            print("\033[2J\033[H", end="")
            
            print(f"\033[{color_code}mTHANK YOU FOR PLAYING!\033[0m")
            print(f"\033[{color_code}mYOUR HIGHEST SCORE: {high_score}\033[0m")
            break
    else:
        print("\033[31mInvalid choice! Please try again.\033[0m")
