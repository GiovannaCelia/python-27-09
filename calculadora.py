
    
def selecao(): 
    opcao= int(input("Escolha uma opção: 1- Soma  2- Subtração  3- multiplicação  4- Divisão 5- sair : "))
    return(opcao)
    

def soma (prim,seg):
 soma= (prim+seg)
 print (soma)
 return soma

def subtracao (prim,seg):
 subtracao= (prim-seg)
 print(subtracao)
 return subtracao
 
def multiplicacao (prim,seg):
 multiplicacao= (prim*seg)
 print(multiplicacao)
 return multiplicacao
 
def divisao (prim,seg):
 divisao= (prim/seg)
 print (divisao)
 return divisao

aux = 0 
resultado=0
vetor = []


while ( aux <= 4 and aux <= 10):
    
    prim= float(input('Digite um número: '));
    seg= float(input('Digite um número: '));
    
    aux = selecao()

    if aux == 1 : 
       resultado= soma(prim, seg)
    elif aux==2:
       resultado= subtracao(prim, seg)   
    elif aux ==3:
      resultado= multiplicacao(prim,seg)
    elif aux == 4:
        resultado= divisao(prim,seg)
    else :
      print('Você saiu da calculadora')
    vetor.append(resultado)
    
print(' vetor dos resultados: ')
for i in vetor: 
 print(i, " ")
    else :
        print('Você saiu da calculadora')
        
    
    
    
