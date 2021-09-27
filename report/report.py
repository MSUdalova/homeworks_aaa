import csv
import json
from random import choice, uniform, randint
from faker import Faker


def generate_and_read_database():
    """
    Генерирует данные о сотрудниках компании в csv-файл.
    Далее считывает их и записывает в словарь.
    Возвращает:
    - database: dict
        - словарь, в котором хранятся данные по столбцам:
            - ключ: название столбца
            - значение: список всех значений столбца.

    """
    dep_marketing = 'Маркетинг'
    dep_sales = 'Продажи'
    dep_devel = 'Разработка'
    dep_analytics = 'Аналитика'
    dep_accounting = 'Бухгалтерия'
    dep_all = (
        dep_marketing,
        dep_sales,
        dep_devel,
        dep_analytics,
        dep_accounting,
    )

    occupation_by_dep = {
        dep_marketing: ('Маркетинг-менеджер',),
        dep_sales: ('Sales manager', 'Key account manager'),
        dep_devel: (
            'iOS-инженер',
            'Android-инженер',
            'Backend-инженер',
            'Frontend-инженер',
            'Продакт-менеджер',
        ),
        dep_accounting: ('Бухгалтер',),
        dep_analytics: ('ML-инженер', 'Data Science инженер',),
    }

    area_by_dep = {
        dep_marketing: ('Direct', 'Performance',),
        dep_sales: ('B2C', 'B2B', 'Госы',),
        dep_devel: ('Платформа', 'Основной продукт', 'Внутренний портал',),
        dep_accounting: ('Компенсации и льготы', 'Зарплата',),
        dep_analytics: ('DWH', 'Product',),
    }

    report_header_fields = (
        'ФИО полностью',
        'Департамент',
        'Отдел',
        'Должность',
        'Оценка',
        'Оклад',
    )

    salary_min = 55000
    salary_max = 125000

    perf_score_min = 3.5
    perf_score_max = 5.0

    faker_gen = Faker('ru_RU')
    with open('./Corp Summary.csv', 'w') as f:
        out_file = csv.writer(f, delimiter=';')
        out_file.writerow(report_header_fields)
        for _ in range(200):
            dep_name = choice(dep_all)
            area_name = choice(area_by_dep[dep_name])
            occupation = choice(occupation_by_dep[dep_name])

            out_file.writerow((
                faker_gen.name(),
                dep_name,
                area_name,
                occupation,
                '{:3.1f}'.format(uniform(perf_score_min, perf_score_max)),
                randint(salary_min, salary_max) // 100 * 100,
            ))

    with open('Corp Summary.csv', newline='') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        database = {
            'employees': [],
            'departments': [],
            'teams': [],
            'positions': [],
            'scores': [],
            'salaries': []
        }
        for row in reader:
            database['employees'].append(row[0])
            database['departments'].append(row[1])
            database['teams'].append(row[2])
            database['positions'].append(row[3])
            database['scores'].append(row[4])
            database['salaries'].append(int(row[5]))

    return database


def creat_hierarchy(
        departments_for_members: list,
        teams_for_members: list
):
    """
    Параметры:
    - departments_for_members: распределение департаментов по всем сотрудникам.
    - teams_for_members: распределение команд по всем сотрудникам.
    Возвращает:
    - hierarchy: dict
        - иерархия команд.
    """
    keys = set(departments_for_members)
    hierarchy = {}
    for key in keys:
        idx = [i for i, x in enumerate(departments_for_members) if x == key]
        teams_for_department = [teams_for_members[i] for i in idx]
        hierarchy[key] = ', '.join(list(set(teams_for_department)))
    return hierarchy


def summary_report(
        departments_for_members: list,
        salaries_for_members: list
):
    """
    Параметры:
    - departments_for_members: распределение департаментов по всем сотрудникам.
    - salaries_for_members: распределение зарплат по всем сотрудникам.
    Возвращает:
    - report: dict
        - сводный отчёт по департаментам: численность, "вилка" зарплат.
    """
    keys = set(departments_for_members)
    report = {}
    for key in keys:
        idx = [i for i, x in enumerate(departments_for_members) if x == key]
        salaries_of_depart = [salaries_for_members[i] for i in idx]
        report[key] = {
            'Департамент': key,
            'Численность': len(idx),
            'Минимальная зарплата': min(salaries_of_depart),
            'Максимальная зарплата': max(salaries_of_depart),
            'Средняя зарплата': round(sum(salaries_of_depart) / len(idx))
        }
    return report


def write_report_to_csv(
        departments_for_members: list,
        salaries_for_members: list
):
    """
    Записывает словарь из функции summary_report() в csv файл.
    """
    report_to_scv = summary_report(departments_for_members,
                                   salaries_for_members)
    with open('Summary report.csv', 'w', newline='') as f:
        fieldnames = [
            'Департамент',
            'Численность',
            'Минимальная зарплата',
            'Максимальная зарплата',
            'Средняя зарплата']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for key in report_to_scv.keys():
            writer.writerow(report_to_scv[key])
    print('Сводный отчет сохранен в файл "Summary report.csv"')


def menu():
    """
    Старт программы.
    Запрашивает одно из трех действий у пользователя
    и выводит результат вызовом соответствующей функции.
    """
    print(
        """Выберите номер того, что необходимо вывести:
        1) Иерархия департаментов;
        2) Сводный отчёт по департаментам;
        3) Сохранить сводный отчёт по департаментам в виде csv-файла."""
    )
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    data = generate_and_read_database()

    if option == options[0]:
        json_print = json.dumps(
            creat_hierarchy(data["departments"], data["teams"]),
            ensure_ascii=False,
            sort_keys=True,
            indent=3)
        print(
            f'Департаменты и их команды:\n '
            f'{json_print}')

    elif option == options[1]:
        sum_report = summary_report(data["departments"], data["salaries"])
        print(f'Сводный отчёт по департаментам:\n\n')
        for key in sum_report.keys():
            print(
                f'{key}\n\n'
                f'{json.dumps(sum_report[key], ensure_ascii=False, indent=3)}'
            )

    else:
        write_report_to_csv(data["departments"], data["salaries"])


if __name__ == '__main__':
    menu()
