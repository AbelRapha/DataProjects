# Mini Projeto de Análise de Dados 
<h2> Tabela de conteúdos</h2>
<p align = 'center'> 
    <a href = "#sobre-o-projeto">Sobre o Projeto</a>
    <a href = "#tecnologias">Tecnologias</a>
    <a href = "#dados-utilizados">Dados Utilizados</a>
    <a href = "#storytelling">Storytelling</a>
    <a href = "#autor">Autor</a>
</p> 

## Sobre o Projeto
<p> Uma breve descrição deste projeto.<br>
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
<h3>Primeiramente foi realizado a limpeza dos dados. Retirando as colunas que não eram relevantes para a minha análise, tais como a coluna estado civil e cargo. E no final ficou apenas essas colunas abaixo</h3><br>

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
<h2>
    Tabela Serviços
</h2>

``` bash
TabelaServicos.head()
servicos_df = TabelaServicos.drop(["Codigo do Servico"], axis = 1)
servicos_df.head()
```
<h3> Dados limpos e organizados. Agora eu fui para a parte de responder as perguntas. Primeiramente qual o custo da folha salarial? No caso o custo da Folha de cada funcionário seria basicamente a soma do Salário, Impostos, Benefícios, Vale Refeição e Vale Transporte.</h3>
<p>
    <h3> Porém, tive um pequeno problema com o arranjo dos dados pois eles não estavam no mesmo tipo, ou seja, algumas colunas não estavam sendo consideradas como números, mas sim como palavras. E não dá para a ente fazer contas com palavras, né? Pelo menos eu acho que não dá hahahaha.
    </h3>
</p> <br>
<h3> Informações do tipo de dado que cada coluna está sendo considerada</h3>

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
