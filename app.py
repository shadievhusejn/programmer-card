import os
from flask import Flask, render_template, send_from_directory
import datetime
import random

app = Flask(__name__)


def is_programmer_day(date: datetime.date) -> bool:
    return date.timetuple().tm_yday == 256


def days_until_programmer_day(date: datetime.date) -> int:
    year = date.year
    target = datetime.date(year, 1, 1) + datetime.timedelta(days=255)
    if target < date:
        target = datetime.date(year + 1, 1, 1) + datetime.timedelta(days=255)
    return (target - date).days


WISHES = [
    "✅ Пусть код компилируется с первого раза",
    "🐞 Пусть баги обходят тебя стороной",
    "☕ Пусть кофе никогда не заканчивается",
    "🚀 Пусть дедлайны будут милосердны",
    "💚 Пусть ревью проходит без комментариев",
    "⚡ Пусть CI/CD всегда будет зелёным",
    "🧠 Пусть сложные задачи решаются легко",
]

CODE_SNIPPETS = [
    'while True:\n    print("Ты — лучший разработчик! 💚")\n    break  # потому что это правда',
    'def celebrate(dev):\n    return "🎉" * dev.skill_level',
    'if bugs_found == 0:\n    print("Это магия! ✨")',
    'git commit -m "С праздником, коллега!"',
]


@app.route("/")
def index():
    today = datetime.date.today()
    return render_template(
        "index.html",
        is_today=is_programmer_day(today),
        today=today.strftime("%d.%m.%Y"),
        days_left=days_until_programmer_day(today),
        wishes=random.sample(WISHES, 4),
        code=random.choice(CODE_SNIPPETS),
        year=today.year,
    )

@app.route("/yandex_4ffe4630252809fc.html")
def yandex_verify():
    return send_from_directory("static", "yandex_4ffe4630252809fc.html")




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)