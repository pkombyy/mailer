from config import ADMIN_IDS, API_TOKEN,SMTP_SERVER,SMTP_PORT,EMAIL_PASSWORD, FROM_EMAIL
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_admin(user_id):
    """Проверяет, является ли пользователь администратором."""
    return user_id in ADMIN_IDS

async def get_user_id_by_username(username):
    from aiogram import Bot

    bot = Bot(token=API_TOKEN)  
    try:
        user = await bot.get_chat(username)
        return user.id
    except Exception as e:
        print(f"Ошибка при получении ID пользователя {username}: {e}")
        return None
    

async def send_email(to_email: str, link: str) -> bool:
    # Создание HTML-шаблона
    html_template = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.5;
                    color: #555;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                }}
                a:hover {{
                    background-color: #0056b3;
                }}
                footer {{
                    margin-top: 20px;
                    font-size: 12px;
                    color: #aaa;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Привет!</h1>
                <p>Мы рады сообщить вам, что ваша ссылка готова. Пожалуйста, нажмите на кнопку ниже, чтобы перейти по ней:</p>
                <a href="{link}">Перейти по ссылке</a>
                <footer>
                    <p>Спасибо, что вы с нами!</p>
                </footer>
            </div>
        </body>
    </html>
    """

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = "Тема письма"

    # Прикрепление HTML-содержимого
    msg.attach(MIMEText(html_template, 'html'))

    # Отправка письма
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Защита соединения
        server.login(FROM_EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Письмо успешно отправлено!")
        return True
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return False
    finally:
        server.quit()