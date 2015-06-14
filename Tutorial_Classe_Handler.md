## CLASSE HANDLER

A classe Handler basicamente executa métodos JSON-RFC no Kodi, bastando
ao usuário informar o método (e seus parâmetros, se necessário), que
a classe faz o resto

### COMO USÁ-LA

Passo 1: importe a classe

from Handler import Handler


Passo 2: instancie-a

handler = Handler()


Passo 3: Defina o método JSON-RFC que vai rodar no Kodi

handler.method = "<nome do método>"

handler.params = {chave1:valor1, chave2:valor2, ...}


Passo 4: bote pra rodar o método usando GET ou POST

handler.get()

OU

handler.post()

Passo 5: Vá ao Kodi e veja o resultado...

### NOTAS ADICIONAIS

#### Permissões
Antes de tudo, é preciso que o Kodi "permita que apps mexam nele". Para
isso, deve-se ir em "Settings -> Services -> Webserver" e habilitar a 
opcao "Allow control of Kodi via HTTP"

#### Acessando remotamente
Se você quiser usar essa classe para controlar um Kodi "remoto", ou
seja, localizado em outra máquina da rede, e so informar o IP e a
porta desse Kodi no construtor da classe, exemplo:

handler = Handler(10.45.2.30,8585)
