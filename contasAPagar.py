from psycopg2.extras import RealDictCursor
from cryptography import decrypt

def contasAPagarList(conn):
  cursor = conn.cursor(cursor_factory=RealDictCursor)
  cursor.execute("SELECT fornecedor.id, fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, cp.id, cp.data_vencimento, cp.pago, SUM  (nota_fiscal.valor_total) AS valor_total FROM contas_a_pagar AS cp LEFT JOIN fornecedor ON cp.fornecedor = fornecedor.id LEFT JOIN nota_fiscal ON nota_fiscal.id::text = ANY(cp.notas_fiscais) GROUP BY fornecedor.id, fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, cp.id, cp.data_vencimento, cp.pago")
  contasAPagarList = cursor.fetchall()
  for row in contasAPagarList:
    row['telefone'] = decrypt(row['telefone'])
  cursor.close()
  return {"data": contasAPagarList}


def getTotal(conn):
  cursor = conn.cursor(cursor_factory=RealDictCursor)
  cursor.execute("SELECT SUM(valor_total) FROM contas_a_pagar AS cp LEFT JOIN fornecedor ON cp.fornecedor = fornecedor.id LEFT JOIN nota_fiscal ON nota_fiscal.id::text = ANY(cp.notas_fiscais)")
  total = cursor.fetchall()
  cursor.close()
  return {"data": total}

