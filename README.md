# lucrorural-dev

Ao clicar no link do projeto, aperte "ctrl" + "F5" para tirar o servidor Heroku do modo 'idle'. A inatividade do nível gratuito permite que o Heroku ofereça esse nível para desenvolvimento/teste, sem um grande custo indireto de servidores em execução constante.

# Sobre o projeto

https://lucrorural-front-end.herokuapp.com/

Lucro Rural dev é um projeto realizado para vaga de desenvolvedor na empresa Lucro Rural.

A aplicação consiste em uma tabela de Contas a Pagar, onde o cliente poderá criar, editar ou excluir contas a pagar de fornecedores. Requisitos para adicionar notas fiscais:
- Vincular as Notas Fiscais a uma Conta a Pagar desde que sejam do mesmo Fornecedor.
- Não permitir excluir Contas a Pagar se houver Nota Fiscal vinculada.

## Layout 
### Página principal
![image](https://user-images.githubusercontent.com/81928006/171308922-61779962-6278-4cbd-8cbe-c9d8c1916233.png)
### Adicionar nova conta a pagar
![image](https://user-images.githubusercontent.com/81928006/171309006-4bf6c61f-0ed8-4717-ac4e-60a617313501.png)
### Mensagem de sucesso ao adicionar nova conta a pagar
![image](https://user-images.githubusercontent.com/81928006/171317110-b3e2d781-7915-4005-bab7-3b0e53855976.png)
### Mensagem de erro ao tentar adicionar fornecedor com nota fiscal de outro fornecedor
![image](https://user-images.githubusercontent.com/81928006/171317206-60331508-ac59-4cf2-b11b-97423881d625.png)
### Tela para deletar uma conta a pagar
![image](https://user-images.githubusercontent.com/81928006/171309186-e089add9-392a-419f-b5aa-e5cbe07f0301.png)
### Mensagem de erro ao tentar deletar conta com nota fiscal vinculada
![image](https://user-images.githubusercontent.com/81928006/171309211-7d5188a1-5fb4-41dd-8c9d-c9435a2575ea.png)
### Mensagem ao deletar conta com sucesso
![image](https://user-images.githubusercontent.com/81928006/171315571-1276a013-145e-42db-a6a2-754795d3f7f9.png)
### Tela para editar conta
![image](https://user-images.githubusercontent.com/81928006/171316907-bc265637-5ce4-4e9f-9ac7-1c0ad67b1f4c.png)
### Mensagem ao editar conta com sucesso
![image](https://user-images.githubusercontent.com/81928006/171317000-ba957187-656e-41b8-8cc0-23e50cb15c8f.png)






# Tecnologias utilizadas
## Back end
- Python
- Flask
- PSYCOPG
- SQLAlchemy
## Front end
- HTML / CSS / JS
- ReactJS
- React Hooks
- Material UI
- Bootstrap
## Implantação em produção
- Back end: Heroku
- Front end web: Heroku
- Banco de dados: Postgresql

# Como executar o projeto

## Back end

Pré-requisitos: Python 3

```bash
# clonar repositório
git clone https://github.com/limaricardo/lucrorural-dev.git

# instalar dependências do projeto, caso necessário:
pip install Flask
pip install psycopg2
pip install SQLAlchemy
pip install cryptographyS
pip install python-dotenvSS
pip install -U flask-cors
pip install simplejson

# executar o projeto
python app.py
```

## Front end web
Pré-requisitos: npm / yarn

```bash
# clonar repositório
git clone https://github.com/limaricardo/lucrorural-front-end.git


# instalar dependências do projeto, caso necessário:
npm install

npm install react-datepicker --save
npm install axios --save
npm i react-bootstrap-icons --save
npm install @mui/material @emotion/react @emotion/styled --save
npm install @mui/icons-material --save
npm install --save react-toastify --save

# executar o projeto
npm start
```

# Autor

Ricardo Pereira Lima

https://www.linkedin.com/in/ricardo-pereira-274b22aa/
