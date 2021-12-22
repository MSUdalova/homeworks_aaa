import enum
from random import randint
import click


class PizzaSize(enum.Enum):
    """Создает перечисление размеров для пиццы"""
    L = 1
    XL = 2


class PizzaBase:
    """Класс для определения базовых параметров пиццы"""
    def __init__(self, size):
        self.size = PizzaSize[size]


class Margherita(PizzaBase):
    """Рецепт пиццы Маргарита"""
    recipe = {
        'Margherita 🧀': ['tomato sauce', 'mozzarella', 'tomatoes']
    }

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def __dict__():
        return Margherita.recipe


class Pepperoni(PizzaBase):
    """Рецепт пиццы Пипперони"""
    recipe = {
        'Pepperoni 🍕': ['tomato sauce', 'mozzarella', 'pepperoni']
    }

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def __dict__():
        return Pepperoni.recipe


class Hawaiian(PizzaBase):
    """Рецепт пиццы Гавайская"""
    recipe = {
        'Hawaiian 🍍': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }

    def __init__(self, size):
        super().__init__(size)


    @staticmethod
    def __dict__():
        return Hawaiian.recipe


def log(pattern: str):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return pattern.format(
                result
            )
        return inner_wrapper
    return outer_wrapper


@log('🛵 Доставили за {}с!')
def delivery(pizza: PizzaBase):
    """Доставляет пиццу"""
    delivery_time = randint(1, 60)
    return delivery_time


@log('Забрали за {}с!')
def pickup(pizza: PizzaBase):
    """Самовывоз"""
    pickup_time = randint(30, 60)
    return pickup_time


@click.group()
def cli():
    pass


@log('👩‍🍳 ‍Приготовили за {}с!')
@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    bake_time = randint(5, 100)
    click.echo(f'👩‍🍳 ‍Приготовили за {bake_time}с!')
    if delivery:
        click.echo(f"🛵 Доставили за 1с!")


@cli.command()
def menu():
    """Выводит меню"""
    pizza1 = Margherita("XL")
    pizza2 = Hawaiian('L')
    pizza3 = Pepperoni('XL')
    click.echo(pizza1.__dict__())
    click.echo(pizza2.__dict__())
    click.echo(pizza3.__dict__())


if __name__ == '__main__':
    cli()
    m = Margherita("XL")
    h = Hawaiian('L')
    p = Pepperoni('XL')
    print(p.size)
    print(m.size)
    print(h.size)
    print(p.__dict__())
    print(m.__dict__())
    print(h.__dict__())

    print(pickup(Margherita("L")))

