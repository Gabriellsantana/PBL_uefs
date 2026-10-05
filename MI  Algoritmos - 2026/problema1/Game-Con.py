import os #importando bibiotleca para cls

#Variaveis supostamente declaradas 
funcionario:str;
kids=0;
adultos=0.0;
jovens=0.0;
universitystudent=0.0;
lotacaoMax=0;
idade:int;
senha:str;
contLotacao:int;
contLotacao=0;
dinheiro=0.0;
troco:float
quantJovens=0;
quantAdultos=0;
quantEstudantes=0;
quantPagantes =0;
opcaoPagamento =0;
complementoP=0.0;
lucro = 0.0;
vagasRestantes= 0;

#menu inicial/que determina pin e lotação
print("\n[      Adiministrado do Cuca     ]\n");
print("Infomer Capacidade Máxima do Dia: ",end="");
lotacaoMax = input();

while not lotacaoMax.isdigit():# estou negando literalmente se user não digita numeros 
    print("\033[31mCapacidade inválida. Digite apenas números.\033[0m");
    lotacaoMax = input("Informe novamente a capacidade: ");
    os.system("cls")
lotacaoMax = int(lotacaoMax);
senha=input("Crie um senha para o dia: "); 
os.system("cls") #limpa tela 

opcao ="" 
while opcao!= "2":
    print("\n-----------==[Entradas Visitante]==-----------");
    print("\033[32m[1]Vender>\033[0m");
    print("\033[36m[2]Encerra>\033[0m\n");
    opcao =input("\033[34m>_\033[0m")
    os.system("cls") 

    match opcao:
     case "1":
        if contLotacao < lotacaoMax:
           print("Idade do visitante: ",end="");
           idade =input("\033[34m>_\033[0m");
           if idade.isdigit():
            idade = int(idade);
           else:
            print("\033[31mIdade inválida. Digite apenas números.\033[0m");
            idade =0;
           if idade >=1 and idade <=9:#>>>>>INICIO_SESSÃO_CRIANÇA<<<<<<<<<<<<<<
              print("\033[32mINGRESSO VENDIDO\033[0m");
              print("Categoria:Kids");
              print("Valor:R$ 0.00\n");

              print("ingressos vendidos:%d"%contLotacao);
              print("Capacidade local:%d"%lotacaoMax);
              contLotacao+=1;
              kids+=1
              #>>>>>>>>>>>FIM_SESSÃO_CRIANÇA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
           
           elif idade >=10 and idade <=17:#>>>>>>>>INICIOSESSÂOADOLECENTE<<<<<<<<
              #opreçãofinceira
              print("\nCATEGORIA:JOVENS:PREÇO:R$15,00\n");
              pagamento=float(input("Digite o valor pago $:").replace(",","."));
              if pagamento >= 15.00:#validação pagamento menores que valor do ingresso
               troco = pagamento-15.00;
               print("\n\033[32mINGRESSO VENDIDO\033[0m");
               print("Categoria:Adolecente");
               print("\033[33mValor:R$ 15,00\033[0m");
               print("troco R$:%.2f"%troco);
               quantJovens+=1;
               quantPagantes+=1;
               contLotacao+=1
               dinheiro+=15.00;
               jovens+=15.00;
               #informativos
               print("\ningressos vendidos:%d"%contLotacao);
               print("Capacidade local:%d"%lotacaoMax);
              else:
                 print("\033[31m[Pagamneto insuficente]\033[0m");
                 opcaoPagamento = ""
                 while opcaoPagamento !="1" and opcaoPagamento !="2":
                   print("\n\n[1]Completar pagamento");
                   print("[2]Cancelar compra\n");
                   opcaoPagamento=input("\033[34m>_\033[0m");
                   os.system("cls");
                   if opcaoPagamento !="1" and opcaoPagamento !="2":
                     print("\033[31m[Opção invâlida]\033[0m");
                 
                 if opcaoPagamento =="1":
                   print("Valor restante: R$ %.2f" % (15-pagamento));
                   complementoP=float(input("Digite o valor restante: R$ ").replace(",", "."))

                   if (pagamento+complementoP) >= 15.00:#>>>verificando se soma do complemento e pagamento é maior que valor minimo
                    troco = (pagamento + complementoP) - 15;
                    print("\n\033[32mINGRESSO VENDIDO\033[0m");
                    print("Categoria:Adolecente");
                    print("Valor:\033[33mR$ 15,00\033[0m");
                    print("troco R$:%.2f"%troco);

                    #>>>>>>>>variaveis acumaladoras de dados<<<<<<<
                    quantJovens+=1;
                    quantPagantes+=1;
                    contLotacao+=1
                    dinheiro+=15.00;
                    jovens+=15.00;
                    #>>>>>>>>>>>>>>FIM DA SESSÃO ADOLECENTE<<<<<<<<<<<<<<
                   else:
                     print("Pagamento insuficiente/VENDA CANCELADA");
           elif idade >=18:#>>>>>>>INICIO DA SESSÃO ADULTO<<<<<<<<<<<<<<
              uefs ="";
              while uefs != "1" and uefs !="2":#>>>>VERIFICAÇÃO DE ADULTO UEFS
               print("Desconto Estudantil para Universitario Uefs %:"); 
               uefs=input("\n[1] Sim [2] Não:");
               input("\nPressione ENTER para confirmar....");
               os.system("cls");

               match uefs:#>>>>>>INICIO DA SESSÃO ESTUDANTE<<<<<<<<<<<<<<<<
                case "1": 
                 matricula=input("Informe a Matricula: ");
                 if len(matricula) == 9 and matricula.isdigit():#>>MATRICULA<<
                  print("\nCATEGORIA:ESTUDANTE:PREÇO:R$20,00\n");
                  pagamento=float(input("Digite o valor pago $: ").replace(",","."));
                  if pagamento >=20:#aqui ainda verifico o valordo pagamento
                   troco =pagamento -20;
                   print("\n\033[32mINGRESSO VENDIDO\033[0m");
                   print("Categoria:Estudante");
                   print("\033[33mValor:R$ 20,00\033[0m\n");  
                   print("Troco:R$ %.2f"%troco);
                   quantEstudantes+=1
                   quantPagantes+=1;
                   contLotacao+=1
                   dinheiro+=20.00;
                   universitystudent+=20.00
                   print("\ningressos vendidos:%d"%contLotacao);
                   print("Capacidade local:%d"%lotacaoMax);
                  else:
                      print("\033[31m[Pagamneto insuficente]\033[0m");
                      opcaoPagamento = ""
                      while opcaoPagamento !="1" and opcaoPagamento !="2":
                        print("\n\n[1]Completar pagamento");
                        print("[2]Cancelar compra");
                        opcaoPagamento=input("\033[34m>_\033[0m");
                        os.system("cls");
                        if opcaoPagamento !="1" and opcaoPagamento !="2":
                         print("\033[91mopção invalida\033[0m");
                      if opcaoPagamento =="1":
                         print("Valor restante: R$ %.2f" % (20-pagamento));
                         complementoP=float(input("Digite o valor restante: R$ ").replace(",", "."))
                         if (pagamento+complementoP) >= 20.00:#>>>verificando se soma do complemento e pagamento é maior que valor minimo
                          troco = (pagamento + complementoP) - 20;
                          print("\n\033[32mINGRESSO VENDIDO\033[0m");
                          print("Categoria:Estudante");
                          print("Valor:\033[33mR$ 20,00\033[0m");
                          print("troco R$:%.2f"%troco);
                          #>>>>>>>>variaveis acumaladoras de dados<<<<<<<
                          quantEstudantes+=1
                          quantPagantes+=1;
                          contLotacao+=1
                          dinheiro+=20.00;
                          universitystudent+=20.00
                         else:
                          print("Pagamento insuficiente/VENDA CANCELADA")      
                 else:
                  print("\033[31m[Matricua Uefs invalida]\033[0m");#>>>>>>>>>FIM SESSÃO ESTUDANTE<<<
                 #>>>>>>>>>INICIO_SESSÃO ADULTO<<<<<<<<<<<<<<<<<
                  print("\nCATEGORIA:ADULTO:PREÇO:R$40,00\n");
                  pagamento=float(input("Digite o valor pago $:").replace(",","."));
                  if pagamento >= 40.00:#validação pagamento menores que valor do 
                   troco = pagamento-40.00;
                   print("\n\033[32mINGRESSO VENDIDO\033[0m");
                   print("Categoria:Adulto");
                   print("\033[33mValor:R$ 40,00\033[0m");
                   print("troco R$:%.2f"%troco);
                   quantAdultos+=1;
                   quantPagantes+=1;
                   contLotacao+=1;
                   dinheiro+=40.00;
                   adultos+=40.00;
                   print("\ningressos vendidos:%d"%contLotacao);
                   print("Capacidade local:%d"%lotacaoMax);
                  else:
                    print("\n\033[91Pagamento insuficiente!\033[0m\n");
                    opcaoPagamento = "";
                    while opcaoPagamento !="1" and opcaoPagamento !="2":
                      print("\n\n[1]Completar pagamento");
                      print("[2]Cancelar compra");
                      opcaoPagamento=input("\033[34m>_\033[0m");
                      os.system("cls");
                      if opcaoPagamento !="1" and opcaoPagamento !="2":
                       print("\033[31m[Pagamneto insificiente]\033[0m");
                    if opcaoPagamento =="1":
                      print("Valor restante: R$ %.2f" % (40-pagamento));
                      complementoP=float(input("Digite o valor restante: R$ ").replace(",", "."))
                      if (pagamento+complementoP) >= 40.00:#>>>verificando se soma do complemento e pagamento é maior que valor minimo
                       troco = (pagamento + complementoP) - 40;
                       print("\n\033[32mINGRESSO VENDIDO\033[0m");
                       print("Categoria:Adulto");
                       print("Valor:\033[33mR$ 40,00\033[0m");
                       print("troco R$:%.2f"%troco);
                       #>>>>>>>>variaveis acumaladoras de dados<<<<<<<
                       quantAdultos+=1;
                       quantPagantes+=1;
                       contLotacao+=1;
                       dinheiro+=40.00;
                       adultos+=40.00;            
                      else:
                        print("Pagamento insuficiente/VENDA CANCELADA");
                 #>>>>>>>>>>>>>>>>>>>FIM SESSÃO ADULTO<<<<<<<<<<<<<<<<<<<<<
                case "2":
                    print("\nCATEGORIA:ADULTO:PREÇO:R$40,00\n");
                    pagamento=float(input("Digite o valor pago $:").replace(",","."));
                    if pagamento >= 40.00:#validação pagamento menores que valor do 
                     troco = pagamento-40.00;
                     print("\n\033[32mINGRESSO VENDIDO\033[0m");
                     print("Categoria:Adulto");
                     print("\033[33mValor:R$ 40,00\033[0m");
                     print("troco R$:%.2f"%troco);
                     quantAdultos+=1;
                     quantPagantes+=1;
                     contLotacao+=1;
                     dinheiro+=40.00;
                     adultos+=40.00;
                     print("\ningressos vendidos:%d"%contLotacao);
                     print("Capacidade local:%d"%lotacaoMax);
                    else:
                     print("\033[31m[Pagamneto insuficiente]\033[0m");
                     opcaoPagamento = "";
                     while opcaoPagamento !="1" and opcaoPagamento !="2":
                       print("\n\n[1]Completar pagamento");
                       print("[2]Cancelar compra");
                       opcaoPagamento=input("\033[34m>_\033[0m");
                       os.system("cls");
                       if opcaoPagamento !="1" and opcaoPagamento !="2":
                         print("\033[91mopção invalida\033[0m");
                     if opcaoPagamento =="1":
                        print("Valor restante: R$ %.2f" % (40-pagamento));
                        complementoP=float(input("Digite o valor restante: R$ ").replace(",", "."))
                        if (pagamento+complementoP) >= 40.00:#>>>verificando se soma do complemento e pagamento é maior que valor minimo
                         troco = (pagamento + complementoP) - 40;
                         print("\n\033[32mINGRESSO VENDIDO\033[0m");
                         print("Categoria:Adulto");
                         print("Valor:\033[33mR$ 40,00\033[0m");
                         print("troco R$:%.2f"%troco);
                       #>>>>>>>>variaveis acumaladoras de dados<<<<<<<
                         quantAdultos+=1;
                         quantPagantes+=1;
                         contLotacao+=1;
                         dinheiro+=40.00;
                         adultos+=40.00;            
                     else:
                      print("Pagamento insuficiente/VENDA CANCELADA");
                case _:#outrocaso
                  print("\033[91mValor inválido. Insira um número válido\033[0m");

        else:#fim Lotação maxima !!!!!!!!!!!!!!!!!!fechamneto!!!!!!!!!!!!!!!!!!!!!!
            print("Lotação Maxima Atingida Obrigado por Hoje :)\n");
     case "2":
          confirmaSenha=input("Confirma Senha:");
          if confirmaSenha == senha:
             print("$--Caixa Encerrado--$\n");
          else:
             print("\033[31mSenha Invalida Contantar Administrador\033[0m\n");
             print("Tente Novamente")
             opcao ="" #limpei a varivel do meu laço para não ecerra quando adm erra senha 
     case _:#outro caso  
          print("\033[31m[Valor inválido. Insira um número válido]\033[0m");

if dinheiro <=300.00:  #sessão premiação 
   print("Premiaçoes do DIa ");
   premiacao = dinheiro*0.10;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n3 lugar R$:%.2f"%(valor1,valor2,valor3));
if dinheiro >=300.01 and dinheiro <700.00:  
   print("\o/ Premiaçoes do DIa \o/");
   premiacao = dinheiro*0.15;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n3 lugar R$:%.2f"%(valor1,valor2,valor3));
if dinheiro >=700.00:  
   print("\o/ Premiaçoes do DIa \o/");
   premiacao = dinheiro*0.20;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n3 lugar R$:%.2f"%(valor1,valor2,valor3));
    
input("\nPressione ENTER para >>>DETALHES DO CAIXA$<<<<");
os.system("cls")
print("$-----$--$-----$--[Relatorio]--$-----$--$-----$");
print("\nDetalhamento Caixa");

#>>>>>>>>>Valores por categoria<<<<<<<<<<<<<<<<<<<<<
print("\nValores por Categoria");
print("Jovens R$:%.2f.........."%jovens);
print("Adultos R$:%.2f........."%adultos);
print("Estudantes Uefs R$:%.2f.."%universitystudent)
print("Não Pagantes crianças:%d........."%kids);

#>>>>>>>>Ingresso vendido por categ<<<<<<<<<<<<<<<<<<<<
print("\nIngressos vendido por Categoria")
print("Criança %d"%kids);
print("Jovens %d"%quantJovens);
print("Adultos %d"%quantAdultos);
print("Estudantes %d"%quantEstudantes)

#>>>>>>>>>>>>>>>>Ticket médio<<<<<<<<<<<<<<<<<<<<<<
if contLotacao > 0:
    print("Ticket médio geral R$:%.2f"%(dinheiro/contLotacao));
else:
    print("Ticket médio geral R$:0.00");
if quantPagantes > 0:
    print("Média de pagantes R$:%.2f"%(dinheiro/quantPagantes));
else:
    print("Média de pagantes R$:0.00");

print("Total do dia R$:%.2f"%dinheiro);

vagasRestantes = lotacaoMax - contLotacao;
print("\nVagas restantes: %d \n"%vagasRestantes);

#>>>>>>>>>>>>>>maior receita e empates<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if jovens == adultos and jovens == universitystudent:
    print("Maior receita: empate entre todas as categorias");
elif jovens ==adultos and jovens >universitystudent:
    print("Maior receita: empate entre Jovens e Adultos");
elif jovens == universitystudent and jovens > adultos:
    print("Maior receita: empate entre Jovens e Estudantes UEFS");
elif adultos== universitystudent and adultos > jovens:
    print("Maior receita: empate entre Adultos e Estudantes UEFS");

elif jovens > adultos and jovens > universitystudent:
    print("Maior receita: Jovens");
elif adultos >jovens and adultos > universitystudent:
    print("Maior receita: Adultos");
else:
    print("Maior receita: Estudantes UEFS");

#>>>>>>>>>>>>>>>>>Menor receita e empates<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if jovens == adultos and jovens == universitystudent:
    print("Menor receita: empate entre todas as categorias");
elif jovens == adultos and jovens < universitystudent:
    print("Menor receita: empate entre Jovens e Adultos");
elif jovens == universitystudent and jovens < adultos:
    print("Menor receita: empate entre Jovens e Estudantes UEFS");
elif adultos == universitystudent and adultos < jovens:
    print("Menor receita: empate entre Adultos e Estudantes UEFS");

elif jovens < adultos and jovens < universitystudent:
    print("Menor receita: Jovens");
elif adultos < jovens and adultos < universitystudent:
    print("Menor receita: Adultos");
else:
    print("Menor receita: Estudantes UEFS");

lucro = dinheiro - premiacao
print("\n\nCUCA LUCRO  TOTAL FINAL R$:%.2f\n"%lucro);


         