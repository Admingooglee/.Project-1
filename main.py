import time
from data_source import fetch_senders
from mailer import send_email
from templates import build_message
from config import SMTP_SERVERS, RECEIVERS, DELAY, LOOP_DELAY
from logger import logger
from db import init_db

def get_smtp(email):
    domain = email.split("@")[1]
    return SMTP_SERVERS.get(domain)


def main():
    init_db()
    logger.info("START SCRIPT")

    data = {
        "username": "test_user",
        "id": "123456",
        "link": "https://example.com"
    }

    while True:
        senders = fetch_senders()

        if not senders:
            logger.warning("NO SENDERS FOUND")
            time.sleep(LOOP_DELAY)
            continue

        for sender in senders:
            smtp = get_smtp(sender["email"])

            if not smtp:
                logger.error(f"SMTP NOT FOUND: {sender['email']}")
                continue

            for receiver in RECEIVERS:
                body = build_message(data)

                send_email(
                    sender,
                    receiver,
                    "Тест сообщение",
                    body,
                    smtp
                )

                time.sleep(DELAY)

        logger.info("CYCLE COMPLETE")
        time.sleep(LOOP_DELAY)


if __name__ == "__main__":
    main()
