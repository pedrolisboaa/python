# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000, para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

ANO_DE_EMPRESTIMO = 5
emprestimo_maria = 1000000
valor_parcela = 1000000 / (5 * 12)
data_do_emprestimo = datetime(2020, 12, 20)
data_fim_do_emprestimo = (data_do_emprestimo + timedelta(days=5*365)).strftime("%d/%m/%Y")
data_pagamento = data_do_emprestimo + timedelta(days=30)

print(f'O emprestimo será pago em {data_fim_do_emprestimo}')

for x in range(ANO_DE_EMPRESTIMO * 12):
    print(f'A {x+1}ª parcela será em - {data_pagamento} - R$ {valor_parcela}')
    data_pagamento += timedelta(days=30)