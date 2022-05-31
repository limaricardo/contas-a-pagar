
from flask import Flask, request, redirect
import psycopg2
import json
from decimal import *
from helpers import checkNotas,selectFornecedor, selectContasAPagar, selectNotaFiscal
from contasAPagar import contasAPagarList, getTotal
import os
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "https://lucrorural-front-end.herokuapp.com/"}})

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

# Connect to database and set a cursor
HOST = os.environ['HOST']
DBNAME = os.environ['DATABASE_NAME']
USER = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASSWORD']

conn = psycopg2.connect("host={HOST} dbname={DBNAME} user={USER} password={PASSWORD}", sslmode='require')
cursos = conn.cursor()

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


listFornecedor = selectFornecedor(conn)


listNotaFiscal = selectNotaFiscal(conn)


listContasAPagar = selectContasAPagar(conn)


@app.route("/fornecedores")
def getFornecedor():
    listFornecedor = selectFornecedor(conn)
    listFornecedor = json.dumps(listFornecedor, cls=DecimalEncoder, default=str)

    return {"data": listFornecedor}

@app.route("/notas-fiscais")
def getNotaFiscal():
    listNotasFiscais = selectNotaFiscal(conn)
    listNotasFiscais = json.dumps(listNotasFiscais, cls=DecimalEncoder, default=str)
    return {"data": listNotasFiscais}

@app.route("/contas-a-pagar", methods=["GET", "POST"])
def getContasAPagar():
    listContasAPagar = selectContasAPagar(conn)

    if request.method == "GET":
        return {"data": listContasAPagar}

    elif request.method == "POST":

        # Get data from front-end form
        req = request.json
        fornecedor = req['data']['fornecedor']
        data_vencimento = req['data']['dataVencimento']
        pago = req['data']['pago']
        notas_fiscais = req['data']['notasFiscais'][0]

        # Treat data to check if fornecedor id is the same for the Notas Fiscais
        checkedNotas = checkNotas(conn, fornecedor)
        checkedNotas = checkedNotas['data']
        
        treatedCheck = []
        notas = []
        countOK = 0
        countNOTOK = 0

        for row in checkedNotas:
            treatedCheck.append(row['id'])

        for nota in notas_fiscais:
            notas.append(nota)

        for row in notas:
            if row in treatedCheck:
                countOK += 1
            else: 
                countNOTOK += 1

        

        # If any Nota Fiscal is from another Fornecedor, we won't insert in database and will return an error
        if countNOTOK > 0:
            raise ValueError('Uma ou mais Notas Fiscais não pertencem ao mesmo fornecedor')

        # If there aren't Notas Fiscais, will be inserted as NULL
        elif notas == []:
            cursor = conn.cursor()           
            cursor.execute("INSERT INTO contas_a_pagar (fornecedor, data_vencimento, pago) VALUES(%s, %s, %s)", (fornecedor, data_vencimento, pago))
            conn.commit()
            cursor.close()
            return redirect("/contas-a-pagar")

        # If there are Notas Fiscais, everything will be inserted as expected
        elif countNOTOK <= 0: 
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contas_a_pagar (fornecedor, data_vencimento, pago, notas_fiscais) VALUES(%s, %s, %s, %s)", (fornecedor, data_vencimento, pago, notas))
            conn.commit()
            cursor.close()
            return redirect("/contas-a-pagar")

@app.route("/contas-a-pagar-list")
def getContasAPagarList():
    contasAPagar = contasAPagarList(conn)
    contasAPagar = json.dumps(contasAPagar, cls=DecimalEncoder, default=str)

    return {"data": contasAPagar}


@app.route("/total-das-notas")
def getTotalNotas():
    total = getTotal(conn)
    total = json.dumps(total, cls=DecimalEncoder, default=str)

    return total

@app.route("/contas-a-pagar-delete", methods=["GET", "POST"])
def getContasAPagarDelete():
    listContasAPagar = selectContasAPagar(conn)
    listContas = json.dumps(listContasAPagar, cls=DecimalEncoder, default=str)

    if request.method == "GET":
        return {"data": listContas}

    elif request.method == "POST":

        
        req = request.json
        
        id = req['data']['id']

        cursor = conn.cursor()
        cursor.execute("DELETE FROM contas_a_pagar WHERE id = %s AND notas_fiscais IS NULL", (id, ))
        cursorCount = cursor.rowcount
        conn.commit()
        cursor.close()
        
        if(cursorCount == 0 ) :
            raise ValueError('Não é permitido excluir caso haja Nota Fiscal Vinculada')
        else: 
            return redirect("/contas-a-pagar")


@app.route("/contas-a-pagar-edit", methods=["GET", "POST"])
def getContasAPagarEdit():
    listContasAPagarEdit = selectContasAPagar(conn)

    if request.method == "GET":
        return {"data": listContasAPagarEdit}

    elif request.method == "POST":

        # Get data from front-end form
        req = request.json
        fornecedor = req['data']['fornecedor']
        data_vencimento = req['data']['dataVencimento']
        pago = req['data']['pago']
        notas_fiscais = req['data']['notasFiscais'][0]
        id = req['data']['id']

        # Treat data to check if fornecedor id is the same for the Notas Fiscais
        checkedNotas = checkNotas(conn, fornecedor)
        checkedNotas = checkedNotas['data']
        
        treatedCheck = []
        notas = []
        countOK = 0
        countNOTOK = 0

        for row in checkedNotas:
            treatedCheck.append(row['id'])

        for nota in notas_fiscais:
            notas.append(nota)

        for row in notas:
            if row in treatedCheck:
                countOK += 1
            else: 
                countNOTOK += 1

        

        # If any Nota Fiscal is from another Fornecedor, we won't insert in database and will return an error
        if countNOTOK > 0:
            raise ValueError('Uma ou mais Notas Fiscais não pertencem ao mesmo fornecedor')

        # If there aren't Notas Fiscais, will be inserted as NULL
        elif notas == []:
            cursor = conn.cursor()           
            cursor.execute("UPDATE contas_a_pagar SET fornecedor = %s, data_vencimento = %s, pago = %s WHERE id = %s VALUES(%s, %s, %s, %s)", (fornecedor, data_vencimento, pago, id))
            conn.commit()
            cursor.close()
            return redirect("/contas-a-pagar")

        # If there are Notas Fiscais, everything will be inserted as expected
        elif countNOTOK <= 0: 
            cursor = conn.cursor()
            cursor.execute("UPDATE contas_a_pagar SET fornecedor = %s, data_vencimento = %s, pago = %s, notas_fiscais = %s  WHERE id = %s VALUES(%s, %s, %s, %s, %s)", (fornecedor, data_vencimento, pago, notas, id))
            conn.commit()
            cursor.close()
            return redirect("/contas-a-pagar")
        

if __name__ == "__main__":
    app.run(debug=True) 