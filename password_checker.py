import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short — use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  12+ characters = much stronger")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")

    common = ["password", "123456", "qwerty",
              "abc123", "password123", "admin",
              "letmein", "welcome", "monkey"]
    if password.lower() in common:
        score = 0
        feedback.append("❌ This is a very common password!")

    if score <= 2:
        rating = "🔴 WEAK"
    elif score <= 4:
        rating = "🟡 MODERATE"
    elif score == 5:
        rating = "🟢 STRONG"
    else:
        rating = "✅ VERY STRONG"

    return score, rating, feedback


def main():
    print("=" * 45)
    print("   🔐 Password Strength Checker")
    print("   by Kanthi Phoosorn")
    print("=" * 45)

    while True:
        print("\n1. Check password strength")
        print("2. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            password = input("Enter password: ")
            score, rating, feedback = check_password_strength(password)

            print(f"\n{'='*45}")
            print(f"Score:  {score}/6")
            print(f"Rating: {rating}")
            print(f"{'='*45}")

            if feedback:
                print("\n📋 Suggestions:")
                for tip in feedback:
                    print(f"  {tip}")
            else:
                print("\n🎉 Perfect password!")

        elif choice == "2":
            print("\nGoodbye! 👋")
            break

main()
