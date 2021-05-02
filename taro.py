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
    previous_seeds: set = set()

    def __init__(self):
        self.previous_seed = 0
        for suit in range(1, 5):
            for order in range(1, 15):
                self.cards.append(MinorArcane(suit=suit, order=order))
        for order in range(0, 21):
            self.cards.append(MajorArcane(order=order))

    def __repr__(self):
        return repr(self.cards)

    def shuffle(self, seed: str, amount: int) -> list[object]:
        new_seed = bytearray(seed, "utf8")
        if new_seed == self.previous_seeds:
            random.shuffle(new_seed)
        self.previous_seeds.add(new_seed[:50])
        random.seed(new_seed)
        cards = random.sample(self.cards, len(self.cards))
        for i in random.sample(range(len(cards)-1), 10):
            cards[i].is_flipped = cards[i].is_flipped ^ True
        return random.sample(cards, amount)


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
            if amount_of_cards not in range(1, 79):
                raise ValueError
        except ValueError:
            print("Введите правильное число в границах от 1 до 78.")
            continue

        print(
            deck.shuffle(
                seed=seed,
                amount=amount_of_cards
            )
        )
        proceed = True if input("Продолжаем?(y/n): ") in "yну" else False


if __name__ == '__main__':
    main()
