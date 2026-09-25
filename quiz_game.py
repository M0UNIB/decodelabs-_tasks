import random


QUESTIONS = [
    {
        "topic": "Geography",
        "question": "What is the capital of France?",
        "answer": "paris",
        "hint": "It is also the most visited city in the world.",
    },
    {
        "topic": "Geography",
        "question": "Which country has the most people?",
        "answer": "india",
        "hint": "It overtook China in 2023.",
    },
    {
        "topic": "Science",
        "question": "How many planets are in our solar system?",
        "answer": "8",
        "hint": "Pluto was reclassified in 2006.",
    },
    {
        "topic": "Science",
        "question": "What gas do plants absorb from the air?",
        "answer": "carbon dioxide",
        "hint": "They release oxygen in return.",
    },
    {
        "topic": "Science",
        "question": "What is the chemical symbol for gold?",
        "answer": "au",
        "hint": "It comes from the Latin word aurum.",
    },
    {
        "topic": "Technology",
        "question": "What does CPU stand for?",
        "answer": "central processing unit",
        "hint": "It is the brain of the computer.",
    },
    {
        "topic": "Technology",
        "question": "In which year did the first human land on the Moon?",
        "answer": "1969",
        "hint": "Apollo 11. Neil Armstrong was the first to step out.",
    },
    {
        "topic": "History",
        "question": "Who was the first President of the United States?",
        "answer": "george washington",
        "hint": "He served two terms from 1789.",
    },
]


def show_menu():
    print("\n1. Quick round (3 questions)")
    print("2. Full challenge (all questions)")
    print("3. How scoring works")
    print("4. Exit")


def normalize(text):
    cleaned = text.strip().lower()
    for symbol in (" ", "'", ".", ",", "-"):
        cleaned = cleaned.replace(symbol, "")
    return cleaned


def ask_count(questions, quick):
    if quick:
        return min(3, len(questions))

    while True:
        answer = input(f"How many questions? (1-{len(questions)}): ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(questions):
            return int(answer)
        print(f"Enter a whole number between 1 and {len(questions)}.")


def play_round(questions, quick):
    count = ask_count(questions, quick)
    selected = random.sample(questions, count)

    score = 0
    print(f"\n=== Quiz: {count} questions, 1 point each ===")

    for number in range(len(selected)):
        item = selected[number]
        print(f"\nQuestion {number + 1} of {len(selected)} [{item['topic']}]")
        print(item["question"])

        while True:
            guess = input("Your answer: ")
            if guess.strip() == "":
                print("Please type an answer before continuing.")
                continue
            break

        if normalize(guess) == normalize(item["answer"]):
            score = score + 1
            print("Correct! +1 point")
        else:
            print(f"Not quite. {item['hint']}")
            print(f"Answer: {item['answer'].title()} (+0 points)")

    print("\n=== Final Results ===")
    print(f"Score: {score}/{len(selected)}")
    print(f"Percentage: {score / len(selected) * 100:.0f}%")
    print(final_message(score, len(selected)))
    return score


def final_message(score, total):
    percentage = score / total
    if percentage == 1:
        return "Perfect score. Outstanding."
    if percentage >= 0.75:
        return "Strong result. You have a solid grip on this."
    if percentage >= 0.5:
        return "Passable. Review the topics you missed and try again."
    if percentage > 0:
        return "Below average. Worth a second run through the material."
    return "No points this round. Reset and try the full challenge."


def explain():
    print("\nEach correct answer adds exactly 1 point. Wrong answers add 0 and reveal")
    print("a hint. Answers are compared case-insensitively, so 'Paris' and 'paris' both")
    print("count, and spaces, apostrophes and full stops are ignored.")
    print(f"Question bank: {len(QUESTIONS)} questions. Passing needs 75 percent.")


def main():
    print("=== General Knowledge Quiz ===")
    while True:
        show_menu()
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            play_round(QUESTIONS, True)
        elif option == "2":
            play_round(QUESTIONS, False)
        elif option == "3":
            explain()
        elif option == "4":
            print("Goodbye.")
            break
        else:
            print("Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
