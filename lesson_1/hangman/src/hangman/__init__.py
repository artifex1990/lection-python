"""Точка входа в игру."""

from hangman.game import choose_word, play_round


def ask_yes_no(question: str) -> bool:
    """Спрашивает да/нет, пока не получит понятный ответ."""
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()
        match answer:
            case "да" | "д" | "y" | "yes":
                return True
            case "нет" | "н" | "n" | "no":
                return False
            case _:
                print("Не понял. Ответь «да» или «нет».")


def main() -> None:
    """Запускает игровую сессию с подсчётом статистики."""
    print("=" * 40)
    print("🎯 ВИСЕЛИЦА".center(40))
    print("=" * 40)
    print("Угадай слово по буквам. У тебя 6 ошибок.\n")

    stats: dict[str, int] = {"wins": 0, "losses": 0}

    while True:
        word = choose_word()
        if play_round(word):
            stats["wins"] += 1
        else:
            stats["losses"] += 1

        print(f"\n📊 Счёт - победы: {stats['wins']}, поражения: {stats['losses']}")

        if not ask_yes_no("\nСыграем ещё?"):
            break

    print("\nСпасибо за игру! 👋")
