money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0

while money_capital >= 0:
    months += 1
    if months > 1:
        spend *= (1 + increase)
    money_capital = money_capital + salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", months-1)
