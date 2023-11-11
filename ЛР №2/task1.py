salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

spend_total = 0
for month in range(months):
    spend_total += spend * (1 + increase) ** month

salary_total = salary * months

money_capital = spend_total - salary_total

money_capital = round(money_capital, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
