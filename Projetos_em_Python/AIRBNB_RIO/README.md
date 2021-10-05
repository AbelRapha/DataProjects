# Projeto Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para pessoas comuns
<br>

## *Contexto* 
<p> No Airbnb qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel alugando por alguma diária.</p>

<p>Você cria o seu perfil de host(pessoa que disponibiliza um imóvel para aluguel por diária) e cria o anúncio do seu imóvel.</p>

<p>Nesse anúncio, o host deve descrever as características do imóvel de forma mais completa possível, de forma a ajudar os locadores/viajantes a escolherem o melhor imóvel para eles (e de forma a tornar o anúncio mais atrativo)</p>

<p>Existem dezenas de personalizações possíveis no anúncio, desde quantidade mínima de diária, preço, quantidade de quartos, até regras de cancelamento, taxa extra para hóspedes extras, exigências de verificação de identidade do locador, etc.</p>

## *Nosso objetivo*

Construir um modelo de previsão de preço que permita uma pessoa comum que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel.

Ou ainda, para o locador comum, dado o imóvel que ele está buscando, ajudar a saber se aquele imóvel está com preço atrativo (abaixo da média para imóveis com as mesmas características) ou não.

## *O que temos disponível, inspirações e créditos*

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Elas estão disponíveis para download neste repositório (se você puxar os dados direto do Kaggle pode ser que encontre resultados diferentes dos meus, afinal as bases de dados podem ter sido atualizadas).

Caso queira uma outra solução, tive como referência a solução do usuário Allan Bruno do kaggle no Notebook: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb

Você vai perceber semelhanças entre a solução que vamos desenvolver aqui e a dele, mas também algumas diferenças significativas no processo de construção do projeto.

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

## *Expectativas Iniciais*

- Acredito que a sazonalidade pode ser um fator importante, visto que meses como dezembro costumam ser bem caros no RJ
- A localização do imóvel deve fazer muita diferença no preço, já que no Rio de Janeiro a localização pode mudar completamente as características do lugar (segurança, beleza natural, pontos turísticos)
- Adicionais/Comodidades podem ter um impacto significativo, visto que temos muitos prédios e casas antigos no Rio de Janeiro

Vamos descobrir o quanto esses fatores impactam e se temos outros fatores não tão intuitivos que são extremamente importantes.

## *Deploy do projeto*
- Clone este repositório
- baixe o link do arquivo em formato joblib [aqui](https://drive.google.com/file/d/1Ph-G8HFrYwHXXWhmAuih3q_xt6h4QK1Y/view?usp=sharing), e em seguida extraia o arquivo e coloque na mesma pasta do arquivo de deploy
- Abra a pasta em um editor de código como o VS Code
- Abra um terminal
- Certifique-se que esteja na pasta correta do arquivo em questão
- Comando para rodar a aplicação 
  ```
  streamlit run DeployAirbnb.py
  ```
## informações solicitadas para realizar a previsão da diária:

- Latitude e Longitude (Coordenadas precisas, pegar pelo google maps, por exemplo)
- Quantidade de Comodos, banheiros, quartos, camas.
- Custo extra por pessoa
- Quantidade mínima de noites para se hospedar
- Ano a ser previsto
- Mês a ser previsto
- Quantidade de itens na casa
- Se o Locador costuma responder ou não (0 para Sim, 1 para Não)
- Se o Locador é Superhost na plataforma do Airbnb
- Se o imóvel está disponível para ser alugado a qualquer momento ou não
- Tipo de imóvel
- Tipo de quarto
- Qual a política de cancelamento do contrato de locação 
