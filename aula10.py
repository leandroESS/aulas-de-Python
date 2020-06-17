from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = (data_atual.strftime('%d/%m/%y')) #converte pra string
    # mostra  o dia da semana, mês e ano  --- > data_atual_str = print(data_atual.strftime('%A - %B - %Y'))
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y - - %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.weekday())
    tupla = ('segunda','terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20 , 15, 30 ,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '08/06/2020 12:00:29'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y  %H:%M:%S')
    #O método datetime.strptime serve para fazer o parsing (provavelmente por isso o P)
    # de uma data em um determinado formato. Ou seja,
    # ele recebe uma string, faz o parsing e retorna um objeto datime.
    print(data_convertida)
    print(type(data_convertida))
    print(data_convertida.weekday())
    nova_data = data_convertida - timedelta(days = 365)
    print(nova_data)






def trabalhando_com_time():
    horario = time(hour = 15, minute = 18, second =30)
    print(horario.strftime('%H: %M : %S'))
    print(horario)

    print(type(horario))

if __name__ == '__main__':
 #trabalhando_com_date()
 #trabalhando_com_time()
 trabalhando_com_datetime()


