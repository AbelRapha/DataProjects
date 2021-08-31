# Mini Projeto de Análise de Dados 
<div align = "center">
<h2> Tabela de conteúdos</h2>
</div>
<p align = 'center'> 
    <a href = "#sobre-o-projeto">Sobre o Projeto</a>
    <a href = "#tecnologias">Tecnologias</a>
    <a href = "#dados-utilizados">Dados Utilizados</a>
    <a href = "#storytelling">Storytelling</a>
    <a href = "#autor">Autor</a>
</p> 
<div align = "center">
<img src ="https://user-images.githubusercontent.com/79184789/131441542-c3dc4b7f-c083-4938-ac47-7d80dee5ecda.gif">
</div>

## Sobre o Projeto
<p>Roi, tudo bom? Você vem sempre aqui? hahaha.</p>
<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131442139-bd9769b7-0193-45a0-8788-1372ccb729ad.gif">
</div>
<br>
<p> Brincadeiras a parte, esta é uma breve descrição deste projeto.<br>
O que temos?<br>
Temos os dados de 2019 de uma empresa de prestação de serviços.

Cadastro Funcionarios, Cadastro Clientes e Base Serviços Prestados.<br>
O que queremos saber/fazer?<br>
1- Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?<br>
2- Qual foi o faturamento da empresa?<br>
3- Qual o % de funcionários que já fechou algum contrato?<br>
4- Calcule o total de contratos que cada área da empresa já fechou<br>
5- Calcule o total de funcionários por área <br>
6- Qual o ticket médio mensal (faturamento médio mensal) dos contratos?

</p> 

## Tecnologias
<p>
* Python<br>
* Pandas<br>
* Matplotlib<br>
</p>

## Dados Utilizados
<p align ="left">
    <a href = "https://github.com/AbelRapha/DataProjects/tree/main/Projetos%20em%20Python/Projeto%20de%20An%C3%A1lise%20de%20Dados"> Link do repositório</a>

## Storytelling
<h3>O que fiz primeiramente foi realizar a limpeza dos dados. Retirando as colunas que não eram relevantes para a minha análise, tais como a coluna estado civil e cargo. E no final ficou apenas essas colunas abaixo</h3><br>

``` bash

TabelaFuncionarios.head()
#retirar colunas estado civil e cargo
funcionarios_df = TabelaFuncionarios.drop(["Estado Civil", 'Cargo'], axis = 1)
funcionarios_df.head()

``` 

<h2>    
    
</h2><br>
<h3>
Visualizando os dados. E no caso da tabela de Serviços foi retirado a coluna Código de Serviço.
</h3><br>
<h2> Tabela Clientes</h2>

``` bash
TabelaClientes.head()
```
<div alig = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131439821-675b8042-4646-4e1f-b90f-1a6d4486a761.png">
</div>

<h2>
    Tabela Serviços
</h2>

``` bash
TabelaServicos.head()
servicos_df = TabelaServicos.drop(["Codigo do Servico"], axis = 1)
servicos_df.head()
```
<div alig = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131440244-b413054c-43d3-43e3-8568-b69378df96d5.png">
</div>

<h3> Dados limpos e organizados. Agora eu fui para a parte de responder as perguntas. Primeiramente qual o custo da folha salarial? No caso o custo da Folha de cada funcionário seria basicamente a soma do Salário, Impostos, Benefícios, Vale Refeição e Vale Transporte.</h3>
<p>
    <h3> Porém, tive um pequeno problema com o arranjo dos dados pois eles não estavam no mesmo tipo, ou seja, algumas colunas não estavam sendo consideradas como números, mas sim como palavras. E não dá para a ente fazer contas com palavras, né? Pelo menos eu acho que não dá hahahaha.
    </h3>
<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131441282-7233062b-ce42-42bb-b79b-46d5b3f97eb6.gif">
</div>    
</p> <br>
<h3> Voltando hehehe... As informações do tipo de dado que cada coluna está sendo considerada</h3>

``` bash
funcionarios_df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 114 entries, 0 to 113
Data columns (total 9 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   ID Funcionário        114 non-null    int64  
 1   Nome Completo         114 non-null    object 
 2   Salario Base          114 non-null    float64
 3   Impostos              114 non-null    float64
 4   Beneficios            114 non-null    float64
 5   VT                    114 non-null    float64
 6   VR                    114 non-null    float64
 7   Area                  114 non-null    object 
 8   Custo Total da Folha  114 non-null    float64
dtypes: float64(6), int64(1), object(2)
memory usage: 8.1+ KB
```
<br>
<h3>Conversão dos dados para serem todos conisderados números com vírgula, ou como nós programadores chamamos de float</h3>

``` bash
funcionarios_df
#Converter para float: Impostos, Beneficios, VT e VR
funcionarios_df['Impostos'] = funcionarios_df['Impostos'].apply(lambda x : str(x).replace(",","."))
funcionarios_df['Impostos'] = funcionarios_df["Impostos"].astype("float64")

funcionarios_df['Beneficios'] = funcionarios_df['Beneficios'].apply(lambda x : str(x).replace(",","."))
funcionarios_df['Beneficios'] = funcionarios_df["Beneficios"].astype("float64")

funcionarios_df['VR'] = funcionarios_df['VR'].apply(lambda x : str(x).replace(",","."))
funcionarios_df["VR"] = funcionarios_df["VR"].astype("float64")

funcionarios_df['Salario Base'] = funcionarios_df['Salario Base'].astype("float64")
funcionarios_df['VT'] = funcionarios_df['VT'].astype("float64")
```
<br>
<h3> Agora criando uma nova Coluna chamada Custo Total da Folha. Nela armazenei a soma de todas as colunas que havia considerado como parte do sálario (Salário, Impostos, Benefícios, Vale Refeição e Vale Transporte). Ao final eu somei todas as colunas linha a linha da coluna criada para obter o faturamento mensal da empresa de R$ 2.717.493,22 </h3>

``` bash
funcionarios_df["Custo Total da Folha"] = funcionarios_df['Salario Base']+funcionarios_df['VR']+funcionarios_df['VT']+funcionarios_df['Beneficios']+funcionarios_df['Impostos']
print("Total da Folha Salarial mensal {:,}".format(funcionarios_df['Custo Total da Folha'].sum()))

```

<h2> 2ª Pergunta: Qual o valor de Faturamento da empresa?</h2>
<p>
Primeiramente eu verifiquei se o tempo de contrato e o valor de contrato estavam com o mesmo tipo, ou seja, número.
</p>
<h3> Tabela Clientes</h3>

``` bash
TabelaClientes.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 320 entries, 0 to 319
Data columns (total 3 columns):
 #   Column                 Non-Null Count  Dtype 
---  ------                 --------------  ----- 
 0   ID Cliente             320 non-null    int64 
 1   Cliente                320 non-null    object
 2   Valor Contrato Mensal  320 non-null    int64 
dtypes: int64(2), object(1)
memory usage: 7.6+ KB
```
<h3> Serviços</h3>

``` bash
TabelaServicos.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 237 entries, 0 to 236
Data columns (total 4 columns):
 #   Column                           Non-Null Count  Dtype 
---  ------                           --------------  ----- 
 0   Codigo do Servico                237 non-null    object
 1   ID Funcionário                   237 non-null    int64 
 2   ID Cliente                       237 non-null    int64 
 3   Tempo Total de Contrato (Meses)  237 non-null    int64 
dtypes: int64(3), object(1)
memory usage: 7.5+ KB
```
</p>

<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131443153-e071e80f-1573-42bc-a1cc-6bd8308f16b9.jpg" width = 300px>
</div>

<p> Show de Bola! Agora eu posso seguir. Depois eu fiz o uso do ID Cliente, da tabela serviços, para saber quantas vezes um mesmo cliente fechou um contrato. Utilizando a função value_counts.
</p>

``` bash
servicos_df['ID Cliente'].value_counts()
311    2
320    1
101    1
115    1
113    1
      ..
208    1
206    1
205    1
204    1
1      1
Name: ID Cliente, Length: 236, dtype: int64
```
<div align = "center">
<h1> Joia!</h1>
<img src = "https://user-images.githubusercontent.com/79184789/131443775-1219f79a-5eb5-4a00-b827-0723cba16ee3.gif" width = 300px >
</div>

<p>
Show, agora eu posso fazer a mescla entre as tabelas clientes e serviços para eu poder criar uma nova tabela chamada Faturamento. E nela eu vou poder fazer os cálculos de forma mais fácil. Multiplicando apenas a coluna <a <strong>Tempo Total de Contrato</strong> </a> com a coluna <a <strong>Valor Contrato Mensal.</strong></a> E o final de tudo isso iremos obter o valor de faturamento de R$ 5.519.160,00
</p>

``` bash
faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente','Valor Contrato Mensal']], on = "ID Cliente")
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)']*faturamentos_df['Valor Contrato Mensal']
print("O faturamento total e R$ {:,} ". format(faturamentos_df['Faturamento Total'].sum()))
```
<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131444446-d13652f8-aac4-4e77-9753-cc951201a355.gif" width = 300px>
</div>

<h2>Tabela de Faturamento Criada</h2>
<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131440345-128ed672-9df8-4420-b1ba-3e757561686c.png" >
</div>
<br>
<h2> 3ª Pergunta: Qual a % de funcionários que já fechou algum contrato</h2>
<p>Bom, para responder a essa pergunta eu utilizei novamente a função value_counts para saber quantos funcionários fecharam mais de 1 contrato. e o resultado do TOP 5 funcionários, dividos pelo seu ID, foi:</p>

``` bash
funcionariosQueFecharamContratos = servicos_df['ID Funcionário'].value_counts()
funcionariosQueFecharamContratos[:5].plot(kind = 'bar', figsize = (15,5))
```

<div align = "center">
<img src = "https://user-images.githubusercontent.com/79184789/131440560-86250b0f-2b58-4d07-956a-c507b6feed62.png" >
</div>
<p> Beleza! Já armazenei a coluna gerada com a quantidade de contratos fechads por cada funcionário. Agora, para saber quantos % dos funcionários fecham contratos, então basta dividirmos a quantidade de funcionários que fecharam algum contrato com a quantidade total de funcionários na empresa. O que resultou em uma porcentagem de 86,8%
</p>

``` bash
totalFechado = len(funcionariosQueFecharamContratos)
totalDeFuncionarios = len(funcionarios_df['ID Funcionário'])
print("O percentual de funcionarios que ja fechou algum contrato foi de {:.1%}".format(totalFechado/totalDeFuncionarios))

O percentual de funcionários que já fecharam algum contrato foi de 86,8%
```

<h2>4ª Pergunta: Quantidade de contrato fechados por cada área da empresa? </h2>
