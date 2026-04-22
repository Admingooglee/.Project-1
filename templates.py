import random

VIOLATIONS = {
    "1": ("spam", "Spam / Advertising"),
    "2": ("doxxing", "Personal Data Exposure"),
    "3": ("harassment", "Harassment / Abuse"),
    "4": ("illegal_goods", "Drug-related content"),
    "5": ("illegal_goods", "Drug involvement"),
    "6": ("minor_safety", "Illegal sexual content"),
    "7": ("minor_safety", "Minor exploitation"),
    "8": ("hate_speech", "Hate speech (ethnicity)"),
    "9": ("hate_speech", "Hate speech (religion)"),
    "10": ("violence", "Graphic violence"),
    "11": ("violence", "Animal abuse"),
    "12": ("nsfw", "Adult content"),
    "13": ("illegal_services", "Illegal services"),
    "14": ("self_harm", "Self-harm encouragement"),
    "15": ("extremism", "Terrorism / extremism"),
    "16": ("threats", "Blackmail / threats"),
    "17": ("threats", "Violent threats"),
}

DETAILS = {
    "spam": {
        "en": "repeated unsolicited messages or links",
        "de": "wiederholte unerwünschte Nachrichten oder Links",
        "ua": "повторювані небажані повідомлення або посилання"
    },
    "doxxing": {
        "en": "possible sharing of personal/private data",
        "de": "mögliche Veröffentlichung persönlicher Daten",
        "ua": "можливе поширення особистих даних"
    },
    "harassment": {
        "en": "abusive or hostile behavior toward others",
        "de": "beleidigendes oder агресивне Verhalten",
        "ua": "образлива або агресивна поведінка"
    },
    "illegal_goods": {
        "en": "content related to illegal substances or activities",
        "de": "Inhalte zu illegalen Substanzen oder Aktivitäten",
        "ua": "контент, пов’язаний з незаконними речовинами"
    },
    "minor_safety": {
        "en": "content that may involve minors in unsafe context",
        "de": "Inhalte, die Minderjährige gefährden könnten",
        "ua": "контент, що може загрожувати неповнолітнім"
    },
    "hate_speech": {
        "en": "content targeting protected groups",
        "de": "Inhalte gegen geschützte Gruppen",
        "ua": "контент, спрямований проти захищених груп"
    },
    "violence": {
        "en": "graphic or violent material",
        "de": "gewalttätige oder schockierende Inhalte",
        "ua": "жорстокий або шокуючий контент"
    },
    "threats": {
        "en": "threats or intimidation",
        "de": "Bedrohungen oder Einschüchterung",
        "ua": "погрози або залякування"
    }
}


def generate_report(username, user_id, chat_link, violation_link, violation_key):
    violation_type, label = VIOLATIONS[violation_key]

    en = DETAILS[violation_type]["en"]
    de = DETAILS[violation_type]["de"]
    ua = DETAILS[violation_type]["ua"]

    return f"""
--- ENGLISH ---

Hello,

I would like to report a potential violation.

User: {username}
User ID: {user_id}
Chat: {chat_link}
Evidence: {violation_link}

Reason: {label}

Details:
The reported content shows {en}.

Please review this case.


--- DEUTSCH ---

Guten Tag,

ich möchte einen möglichen Verstoß melden.

Benutzer: {username}
Benutzer-ID: {user_id}
Chat: {chat_link}
Beweis: {violation_link}

Grund: {label}

Details:
Der gemeldete Inhalt zeigt {de}.

Bitte überprüfen Sie den Fall.


--- УКРАЇНСЬКА ---

Вітаю,

хочу повідомити про можливе порушення.

Користувач: {username}
ID: {user_id}
Чат: {chat_link}
Доказ: {violation_link}

Причина: {label}

Деталі:
Контент містить {ua}.

Прошу перевірити.
"""


def main():
    print("=== Multi-language Report Generator ===\n")

    for key, (_, label) in VIOLATIONS.items():
        print(f"{key}. {label}")

    print("----------------------------------")
    choice = input("Select violation > ").strip()

    if choice not in VIOLATIONS:
        print("Invalid choice.")
        return

    username = input("Username: ").strip()
    user_id = input("User ID: ").strip()
    chat_link = input("Chat link: ").strip()
    violation_link = input("Violation link: ").strip()

    report = generate_report(username, user_id, chat_link, violation_link, choice)

    print("\n--- REPORT ---\n")
    print(report)


if __name__ == "__main__":
    main()
