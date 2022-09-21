from models.cliente import Cliente
from models.conta import Conta


felicity: Cliente = Cliente('felicity jones', 'feliciti@gmail.com', '123.456.789-99', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '123.456.584-99', '03/09/1988')

#print(felicity)
#print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

#print(contaf)
#print(contaa)