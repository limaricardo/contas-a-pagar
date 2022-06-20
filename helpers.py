from ast import Raise
from psycopg2.extras import RealDictCursor

def checkNotas(conn, fornecedor):
    if not fornecedor:
        raise Exception('Não é possivel adicionar nova nota se fornecedor não for selecionado')
    else:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT nota_fiscal.id FROM fornecedor JOIN nota_fiscal ON fornecedor.id = nota_fiscal.fornecedor WHERE fornecedor.id = %s", (fornecedor, ))
        checkedNotas = cursor.fetchall()
        cursor.close()
        return {"data": checkedNotas}

def selectFornecedor(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    postgreSQL_select_Query = "select * from fornecedor"
    cursor.execute(postgreSQL_select_Query)
    listFornecedor = cursor.fetchall()
    cursor.close()
    return listFornecedor

def selectNotaFiscal(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    postgreSQL_select_Query = "select * from nota_fiscal"
    cursor.execute(postgreSQL_select_Query)
    listNotaFiscal = cursor.fetchall()
    cursor.close()
    return listNotaFiscal

def selectContasAPagar(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    postgreSQL_select_Query = "select * from contas_a_pagar"
    cursor.execute(postgreSQL_select_Query)
    listContasAPagar = cursor.fetchall()
    cursor.close()
    return listContasAPagar

    