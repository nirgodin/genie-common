from contextlib import contextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from traceback import format_exc
from typing import List, Optional

from genie_common.tools.logs import logger


class EmailSender:
    def __init__(self, user: str, password: str):
        self._user = user
        self._password = password

    def send(self, recipients: List[str], subject: str, body: str) -> None:
        message = MIMEMultipart()
        message.attach(MIMEText(body, 'plain'))

        self.send_multipart(
            recipients=recipients,
            subject=subject,
            message=message
        )

    def send_multipart(self, recipients: List[str], subject: str, message: MIMEMultipart) -> None:
        message['Subject'] = subject
        message['From'] = self._user
        message['To'] = ",".join(recipients)

        try:
            self._send_mail(recipients, message.as_string())
            logger.info("Successfully sent mail")

        except Exception:
            logger.exception("Failed to send mail")

    @contextmanager
    def notify_failure(self, recipients: Optional[List[str]] = None) -> None:
        try:
            yield

        except Exception as e:
            exception_traceback = format_exc()
            self.send(
                recipients=recipients or [self._user],
                subject="Failure Notice",
                body=f"Failed due to the following exception: {e}\n{exception_traceback}"
            )
            raise

        finally:
            pass

    def _send_mail(self, recipients: List[str], message: str) -> None:
        with SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(user=self._user, password=self._password)
            server.sendmail(from_addr=self._user, to_addrs=recipients, msg=message)
