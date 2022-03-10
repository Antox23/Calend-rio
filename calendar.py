import calendar 
# import module

ano = 2022
mes = 10
# perguntar o mes e o ano ao usuário
ano = int(input("Coloque o ano: "))
mes = int(input("Coloque um mês: "))
#mostrar o mes e o ano
print(calendar.month(ano,mes))