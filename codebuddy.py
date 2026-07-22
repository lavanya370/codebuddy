print("👋 Welcome to CodeBuddy - Your Coding Helper")

while True:
    problem = input("\nWhat coding difficulty are you facing? (type 'exit' to quit): ").lower()

    if problem == "exit":
        print("👋 Goodbye macha! Keep coding!")
        break

    elif "loop" in problem:
        print("👉 Loops repeat a task multiple times.")
        print("👉 Try: Print numbers from 1 to 10")

    elif "array" in problem or "list" in problem:
        print("👉 Lists store multiple values.")
        print("👉 Try: Find largest number in a list")

    elif "error" in problem:
        print("👉 Read error carefully and fix step by step")

    else:
        print("👉 Keep practicing daily!")

    print("💡 Tip: Don't give up!")