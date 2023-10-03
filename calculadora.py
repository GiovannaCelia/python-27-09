
    
def selecao(): 
    opcao= int(input("Escolha uma opção: 1- Soma  2- Subtração  3- multiplicação  4- Divisão 5- sair : "))
    return(opcao)
    

def soma (prim,seg):
 soma= (prim+seg)
 print(soma)
 
def subtracao (prim,seg):
 subtracao= (prim-seg)
 print(subtracao)
  
def multiplicacao (prim,seg):
 multiplicacao= (prim*seg)
 print(multiplicacao)
 
def divisao (prim,seg):
 divisao= (prim/seg)
 print(divisao)

aux = 0 

while ( aux <= 4):
    
    prim= float(input('Digite um número: '));
    seg= float(input('Digite um número: '));
    
    aux = selecao()
    
    
    if aux == 1 : 
       soma(prim, seg)
    elif aux==2:
      subtracao(prim, seg)   
    elif aux ==3:
      multiplicacao(prim,seg)
    elif aux == 4:
        divisao(prim,seg)
    else :
        print('Você saiu da calculadora')
        
    
    
    