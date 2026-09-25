import random
import secrets
import string


def show_menu():
    print("\n1. Generate a password")
    print("2. Generate a batch of passwords")
    print("3. Explain the two engines")
    print("4. Exit")


def ask_yes_no(question):
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer in ("y", "yes")


def ask_length():
    while True:
        length = input("Password length (8-64): ").strip()
        if length.isdigit() and 8 <= int(length) <= 64:
            return int(length)
        print("Enter a whole number between 8 and 64.")


def build_charset(use_upper, use_lower, use_digits, use_symbols):
    groups = []

    if use_lower and use_upper:
        groups.append(string.ascii_letters)
    else:
        if use_lower:
            groups.append(string.ascii_lowercase)
        if use_upper:
            groups.append(string.ascii_uppercase)

    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append(string.punctuation)

    return groups


def generate_password(length, groups, secure=True):
    pool = "".join(groups)

    if secure:
        system_random = secrets.SystemRandom()
        pick = system_random.choice
        shuffle = system_random.shuffle
    else:
        pick = random.choice
        shuffle = random.shuffle

    characters = [pick(group) for group in groups]
    while len(characters) < length:
        characters.append(pick(pool))

    shuffle(characters)
    return "".join(characters)


def rate_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(character.islower() for character in password):
        score += 1
    if any(character.isupper() for character in password):
        score += 1
    if any(character.isdigit() for character in password):
        score += 1
    if any(not character.isalnum() for character in password):
        score += 1

    labels = ["Very Weak", "Weak", "Fair", "Fair", "Good", "Good", "Strong", "Very Strong"]
    return labels[score], score


def generate_one():
    secure = ask_yes_no("Use the secure engine (secrets)?")
    length = ask_length()

    groups = build_charset(
        ask_yes_no("Include lowercase letters?"),
        ask_yes_no("Include uppercase letters?"),
        ask_yes_no("Include digits?"),
        ask_yes_no("Include symbols?"),
    )
    if not groups:
        print("Select at least one character type. Nothing generated.")
        return

    password = generate_password(length, groups, secure)
    label, score = rate_password(password)

    print(f"\nPassword: {password}")
    print(f"Length: {len(password)}  |  Strength: {label} ({score}/7)")
    if not secure:
        print("WARNING: random is not cryptographically secure. Never use it for real accounts.")


def generate_batch():
    amount = input("How many passwords? ").strip()
    if not amount.isdigit() or int(amount) < 1:
        print("Enter a positive whole number.")
        return

    amount = min(int(amount), 50)
    length = ask_length()
    groups = build_charset(True, True, True, ask_yes_no("Include symbols?"))
    if not groups:
        print("Select at least one character type. Nothing generated.")
        return

    print(f"\n{'#':<4}{'PASSWORD':<26}{'LENGTH':<8}STRENGTH")
    for index in range(amount):
        password = generate_password(length, groups, True)
        label, score = rate_password(password)
        print(f"{index + 1:<4}{password:<26}{len(password):<8}{label} ({score}/7)")


def explain():
    print("\nrandom  - fast, predictable, seeded by an algorithm. Fine for games and")
    print("         study demos, unsafe for anything that protects an account.")
    print("secrets - reads the operating system CSPRNG. The only correct choice for")
    print("         real passwords, API keys and tokens.")


def main():
    print("=== Password Generator ===")
    while True:
        show_menu()
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            generate_one()
        elif option == "2":
            generate_batch()
        elif option == "3":
            explain()
        elif option == "4":
            print("Goodbye.")
            break
        else:
            print("Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
