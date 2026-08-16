"""Логика игры «Виселица»."""

import random

from hangman.art import draw_gallows
from hangman.words import WORDS

MAX_MISTAKES: int = 6
ALPHABET: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def choose_word(words: tuple[str, ...] = WORDS) -> str:
    """Возвращает случайное слово из словаря в нижнем регистре."""
    return random.choice(words).lower()


def make_mask(word: str, guessed: set[str]) -> str:
    """Собирает маску слова: открытые буквы + подчёркивания.

    >>> make_mask("питон", {"п", "н"})
    'п _ _ _ н'
    """
    return " ".join(letter if letter in guessed else "_" for letter in word)


def is_won(word: str, guessed: set[str]) -> bool:
    """True, если все буквы слова уже названы."""
    return {ch for ch in word if ch in ALPHABET} <= guessed


def validate_letter(raw: str, guessed: set[str]) -> str | None:
    """Проверяет ввод пользователя.

    Возвращает None, если всё в порядке, иначе - текст ошибки.
    """
    letter = raw.strip().lower()

    match letter:
        case "":
            return "Пустой ввод. Введи букву."
        case _ if len(letter) != 1:
            return "Нужна ровно ОДНА буква."
        case _ if letter not in ALPHABET:
            return "Только русские буквы."
        case _ if letter in guessed:
            return f"Букву «{letter}» ты уже называл(а)."
        case _:
            return None


def play_round(word: str) -> bool:
    """Проводит один раунд. Возвращает True при победе."""
    guessed: set[str] = set()
    mistakes: int = 0

    while mistakes < MAX_MISTAKES and not is_won(word, guessed):
        print(draw_gallows(mistakes))
        print(f"\nСлово: {make_mask(word, guessed)}")
        print(f"Ошибки: {mistakes}/{MAX_MISTAKES}")
        if guessed:
            print(f"Названы: {', '.join(sorted(guessed))}")

        raw = input("\nТвоя буква: ")
        letter = raw.strip().lower()
        error = validate_letter(letter, guessed)

        if error is not None:
            print(f"⚠️  {error}")
            continue

        guessed.add(letter)

        if letter in word:
            print("✅ Есть такая буква!")
        else:
            mistakes += 1
            print("❌ Мимо.")

    print(draw_gallows(mistakes))
    won = is_won(word, guessed)

    if won:
        print(f"\n🎉 Победа! Слово: {word.upper()}")
    else:
        print(f"\n💀 Проигрыш. Слово было: {word.upper()}")

    return won
