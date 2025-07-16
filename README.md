<img src="https://img.shields.io/badge/Django-RESTFramework 5+-green.svg">
<img src="https://img.shields.io/badge/MongoDB-4.4-orange.svg">
<img src="https://img.shields.io/badge/PyMongo-4.5+-green?logo=mongodb&logoColor=white&color=47A248&labelColor=gray">

<h1>📌 Visão geral </h1>
<p>💻Back-end baseado em uma locadora de veículos, onde temos 3 modelos de dados. 💾cliente(client),💾carros para aluguel(car_for_rent) e 💾contratos de aluguel(contract).</p>

<p>📌Este projeto utiliza Django REST Framework como backend API integrado com MongoDB. ✨Funcionalidades Principais de uma API RESTful Python.</p>


<p>🛠 Integração perfeita com MongoDB utilizando apenas pymongo puro! e pydantic como modelo,validador e serielizador tudo em 1!</p>

<h2>⛔Modelo baseado pydantic</h2>
<img src="https://img.shields.io/badge/Pydantic-2.5+-blue?logo=pydantic&logoColor=white&color=blue&labelColor=gray" alt="Pydantic">
<p>Devido a natureza python e a estrutura dinâmica de um banco de dados não relacional,não há campos fixos. Para resolver isso foi utilizado modelo Pydantic, com integração MongoDB. Com isso, modelos ficam com a coêrencia de um banco relacional!</p>
<img src="image.png"/>
<ul> Exemplo de validação, onde falta do id_car impede a criação do contrato. </ul>
<br>
<h1>💻Instalação/implementação</h1>
<h2>⚠️Requisitos: MongoDb(local) e python 3.8+ ou mais recente.</h2>
<ul>
<li>Clone-o</li>

```
git clone https://github.com/NikolaosKtec/Django-Pymongo_hacks/tree/main
```
<li>Mude para a pasta: Django_api/</li>

```
Django-Pymongo_hacks/Django_api/
```

<li>Crie um ambiente virtual: python -m venv myenv</li>

```
python -m venv myenv
```

<li> Ative o ambiente virtual:   # Windows </li>

```
myenv\Scripts\activate
```
<li> Instale as dependências:  </li>

```
python -m pip install -r requirements.txt
```
<li>entre na pasta: </li>

```
/Django_api/api_core/
```
<li>inicie o servidor: </li>

```
python manage.py runserver
```
<br>
</ul>

<h1>🛜End points </h1>
<h3> o servidor estará rodando localmente:  
&lt;http://localhost:8000/&gt;</h3>
<ul>
<li>contracts/ -GET-POST-PUT DELETE</li>
<li>cars/ -GET-POST-PUT DELETE</li>
<li>client/ -GET-POST-PUT DELETE</li>
</ul>
<p>Basicamente esta é uma API de locadora de carros, onde temos modelos(cars), clientes(client) e contratos de aluguel(contracts)</p>
<h2>Exemplos de uso</h2>
<br/>

![GET](https://img.shields.io/badge/GET-00AAFF?style=flat-square&logo=azurepipelines&logoColor=white)

<h3>para toda busca é obrigatório o parametro 
&lt;page:int&gt; ex:</h3>
<li>contracts?page=1 || cars?page=2 || client?page=3<li>
 o mesmo para todos os endpoints

<br/>

![POST](https://img.shields.io/badge/POST-00BB00?style=flat-square&logo=azurepipelines&logoColor=white)

<li>contracts/ | cars/ | client/<li>
para cadastrar um novo item(funciona com todos os endpoints)
<li>*OBS: verifique todos os campos necessarios no escopo do modelo</li>
<br/>

![PUT](https://img.shields.io/badge/PUT-FFAA00?style=flat-square&logo=azurepipelines&logoColor=white)



<li>contracts/ | cars/ | client/<li>
para editar um item existente(funciona com todos os endpoints)
<li>*OBS: verifique todos os campos necessarios no escopo do modelo</li>
<br/>

![DELETE](https://img.shields.io/badge/DELETE-FF0000?style=flat-square&logo=azurepipelines&logoColor=white)

<h3>para deleção é obrigatório o parametro &lt;id:str&gt;
 que corresponde ao ObjectID(id) do objeto Mongo</h3>

<li>cars?id=ao84eqc77d0bf67<li>
para apagar um item existente,(funciona com todos os endpoints) caso id seja inválido será mostrado status 400 ou 404

## 🗂 Estrutura de Diretórios

Abaixo está uma explicação dos principais diretórios e arquivos deste projeto:

```
Django-Pymongo_hacks/
├── Django_api/
│   ├── api_core/         # Aplicação principal
|       ...
│       ├──myapp/         # Principais arquivos como views,modelos,repositorio etc...
|          ├──controller  # Views com os end-points
|          ├──db          # Camada db ou repositorio
|          ├──model       # Modelos representações de objetos MongoDB, com validações Pydantic
│       ├── manage.py     # Script utilitário para comandos Django
│   └── requirements.txt  # Dependências do projeto

```

- **Django_api/**: Diretório raiz do backend Django.
- **api_core/**: Contém a lógica da API, incluindo integração com MongoDB, validação Pydantic e endpoints.
- **api_core/api_core/** (interno): Configurações globais do Django, como settings.py e urls.py.
- **manage.py**: Utilitário para executar comandos administrativos do Django.
- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.

Essa estrutura segue o padrão de projetos Django, adaptada para integração com MongoDB.
