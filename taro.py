import random

from dataclasses import dataclass


@dataclass(order=True)
class Arcane:
    order: int = 0
    is_flipped: bool = False


@dataclass(order=True)
class MajorArcane(Arcane):
    def __repr__(self):
        names = ['Шут', 'Маг', 'Жрица', 'Императрица', 'Император', 'Жрец', 'Влюбленные', 'Колесница',
                 'Сила','Отшельник', 'Фортуна', 'Справедливость', 'Повешенный', 'Смерть', 'Умеренность',
                 'Дьявол', 'Башня','Звезда', 'Луна', 'Солнце', 'Суд', 'Мир']
        return (f"{names[self.order - 1]}"
                f"{' перевёрнут.' if self.is_flipped else ''}")


@dataclass(order=True)
class MinorArcane(Arcane):
    suit: int = 0

    def __repr__(self):
        order_strings = ['туз', 'двойка', 'тройка', 'четвёрка', 'пятёрка', 'шестёрка', 'семёрка',
                         'восьмёрка', 'девятка', 'десятка', 'паж', 'рыцарь', 'королева', 'король']
        suits_strings = ["жезлов", "кубков", "мечей", "пенткалей"]
        return (f"{order_strings[self.order - 1].capitalize()}"
                f" {suits_strings[self.suit - 1].capitalize()}"
                f"{' перевёрнут.' if self.is_flipped else ''}")


class Deck:
    cards: list[Arcane] = []

    def __init__(self):
        for suit in range(1, 5):
            for order in range(1, 15):
                self.cards.append(MinorArcane(suit=suit, order=order))
        for order in range(0, 21):
            self.cards.append(MajorArcane(order=order))

    def __repr__(self):
        return repr(self.cards)

    def shuffle(self, seed: str, amount: int) -> list[object]:
        if len(seed) < 5 or len(set(seed)) < 2:
            raise ValueError
        if amount not in range(1, 79):
            raise ValueError
        new_seed = list(seed)
        random.shuffle(new_seed)
        new_seed = "".join(new_seed)
        random.seed(new_seed)
        random.shuffle(self.cards)
        for i in random.sample(range(len(self.cards)-1), random.randint(1, 4)):
            self.cards[i].is_flipped = self.cards[i].is_flipped ^ True
        return random.sample(self.cards, amount)


def main():
    deck = Deck()
    print("Приветствуем в КиберТаро.")
    proceed = True
    while proceed:
        try:
            seed = input("Впишите последовательность, которую транслирует Ваше подсознание:\n")
        except ValueError:
            print("Квинтессенция недоступна, попробуйте другую последовательность.")
            continue

        try:
            amount_of_cards = int(input("Введите количество карт: "))
        except ValueError:
            print("Введите правильное число в границах от 1 до 78.")
            continue

        print(
            deck.shuffle(
                seed=seed,
                amount=amount_of_cards
            )
        )
        proceed = True if input("Продолжаем?(y/n): ") in "yнуYНУ" else False


if __name__ == '__main__':
    main()
