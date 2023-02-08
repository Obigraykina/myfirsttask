####51 Найдите сумму цифр трехзначного числа.

a= int(input())
summernumber = 0

while a:
    summernumber += a % 10
    a//=10

print(summernumber)
