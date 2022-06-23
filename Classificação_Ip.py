#!/usr/bin/env python3

#Importar a os módulos de interface entre o script e o index da página.
import cgitb, cgi
cgitb.enable(display=0, logdir="./")

# Instanciar o objeto 'form' para receber os valores passados pelo Cliente.
form = cgi.FieldStorage()

# Guardar o resultado do método 'getvalue', que corresponde ao ip repassado pelo Cliente, em uma variável local.
ip_ = form.getvalue('endereco_ip')

# Separar a string recebida através da função 'split' e, assim, gerar uma lista com os elementos repartidos.
ip = ip_.split('.')

#Atribuição de um tipo para cada elemento da lista. Isso me possibilitará trabalhar com cada dado individualmente.
oct_1 = int (ip[0])
oct_2 = int (ip[1])
oct_3 = int (ip[2])
oct_4 = int (ip[3])

print("Content-type:text/html\r\n\r\n")
print('<html>')
print ('<body style="background-color: #D8D8D8;" > ')
print ('<center>')
print('<h1> RESULTADO DA VERIFICAÇÃO <h1>')
print ('<h3>Classificação do IP {}: <h3>'.format(ip_))

# Verificação dos IPs Válidos e Inválidos dentro do limite de Endereçamento (255 bytes/octetos):
if (oct_1 <= 255) and (oct_2 <= 255) and (oct_3 <= 255) and (oct_4 <= 255) :

    # Análise quanto aos casos de Invalidez do IP:
    # IPs Inválidos (IP de Loopback, IPs Locais e os que tem o primeiro octeto iguail ou menor que 0)
    # Loopback:
    if oct_1 == 127 and oct_2 == 0 and oct_3 == 0 and oct_4 == 1:
        print ('<h4> ENDEREÇO DE LOOPBACK, INVÁLIDO <h4>')

    #IPs locais:
    elif (oct_1 == 10) or (oct_1 == 172) or (oct_1 == 192 and oct_2 == 168) :
        print ('<h4> ENDEREÇO LOCAL, INVÁLIDO <h4>')
    
    # Classificação dos IPs que começam com '0' e os de Classe 'D' e 'E'...
    # Como na atividade é solicitado que classifiquemos os IPs válidos apenas nas classes A, B ou C, considerei 
    # como sendo Inválidos os IPs pertencentes as classes D e E.
    elif (oct_1 <= 0) or (oct_1 >= 224 and oct_1 <= 239) or (oct_1 >= 240 and oct_1 <= 255): 
        print ('<h4> ENDEREÇO INVÁLIDO <h4>')
    
    # Se o IP não se encaixar em nenhum dos parâmetros de invalidade, ele afirmará que o IP será válido e determinará sua Classe entre A,B ou C:
    else:
        if oct_1 >= 1 and oct_1 <= 127:
            print ('<h4> ENDEREÇO VÁLIDO, CLASSE A <h4>')
    
        elif oct_1 >= 128 and oct_1 <= 191:
            print ('<h4> ENDEREÇO VÁLIDO, CLASSE B <h4>')

        elif oct_1 >= 192 and oct_1 <= 223:
            print ('<h4> ENDEREÇO VÁLIDO, CLASSE C <h4>')

# IPs com octetos maiores que '255'. Nesse caso, pedirá para o usuário inserir um endereço dentro dos padrões de endereçamento IP.
elif (oct_1 > 255) or (oct_2 > 255) or (oct_3 > 255) or (oct_4 > 255) :
    print ('<h4 style="color:#DF0101;"> ERRO: Algum dos octetos excedem o limite de endereçamento (255 bytes/octeto) <br> </h4>')
    print ('Por favor, insira outro endereço. ')

print('<a href=../index.html><h6>VERIFICAR OUTRO ENDEREÇO <h6></a>')
print ('<center>')
print('</body>')
print('</html>')
