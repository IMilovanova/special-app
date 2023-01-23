print('проект для работы с git')

# 
accuracy = float(input('Ââåäèòå òî÷íîñòü: '))

x = int(input('Ââåäèòå x: '))

n = 0

number_series = 1

summ_series = 0

while accuracy < abs(number_series):
 
 x_2n = 1

  i = 1
 
  fact_2n = 1

  for k in range(1, n + 1):

    i *= -1
  
  for k in range(1, 2 * n + 1):

    fact_2n *= k

    x_2n *= x

  number_series = i * x_2n / fact_2n

  summ_series += number_series

  n += 1

print('Ñóììà ðÿäà =',summ_series)
