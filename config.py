SMTP_SERVERS = {
    "gmail.com": ("smtp.gmail.com", 587),
    "mail.ru": ("smtp.mail.ru", 587),
    "rambler.ru": ("smtp.rambler.ru", 587),
    "outlook.com": ("smtp.office365.com", 587),
}

DELAY = 5  # задержка между отправками
LOOP_DELAY = 60  # пауза между циклами

RECEIVERS = [
    "test@example.com"
]
