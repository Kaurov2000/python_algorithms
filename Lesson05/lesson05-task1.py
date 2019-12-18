from collections import namedtuple

def get_year_profit(q1, q2, q3, q4):
    return q1 + q2 + q3 + q4

n = int(input("Введите количество предприятий: "))
New_Enterprise = namedtuple('New_Enterprise', 'name, quarter_1, quarter_2, quarter_3, quarter_4, year_profit')
enterprise = []
sum_profit = 0
for i in range(n):
    name = input("Введите назвние предприятия номер {}: ".format(i + 1))
    quarter_1, quarter_2, quarter_3, quarter_4 = map(int, input("Введите прибыль в каждом из 4х кварталов: ").split())
    enterprise.append(New_Enterprise(name, quarter_1, quarter_2, quarter_3, quarter_4,
                                     get_year_profit(quarter_1, quarter_2, quarter_3, quarter_4)))
    sum_profit += enterprise[i].year_profit
avg_profit = sum_profit / n
print("Средняя прибыль за год составляет {}".format(avg_profit))

above_avg = [ent.name for ent in enterprise if ent.year_profit > avg_profit]
print("Прибыль выше средней у {}".format(above_avg))
under_avg = [ent.name for ent in enterprise if ent.year_profit < avg_profit]
print("Прибыль ниже средней у {}".format(under_avg))