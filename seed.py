import pandas as pd
from flask import Flask
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from cryptography import encrypt, decrypt


load_dotenv()

s = os.getenv('s')
t = os.getenv('t')

# Import CSV file(fornecedor) to get as DataFrame
data = pd.read_csv (r"C:\Users\ricar\Desktop\csv-files\fornecedor\fornecedor.csv", sep=';', usecols=[0,1,2,3])
fornecedores = pd.DataFrame(data)

# Import CSV file(nota fiscal) to get as DataFrame
data = pd.read_csv (r"C:\Users\ricar\Desktop\csv-files\notaFiscal\notaFiscal.csv", sep=';', usecols=[0,1,2,3,4,5,6])
nota_fiscal = pd.DataFrame(data)

# Create Engine from sqlAlchemy to connect Dataframe to database

engine = create_engine('postgresql://postgres:1234@localhost:5432/lucrorural')





# Encrypt phone number 
for index, row in fornecedores.iterrows():
    row['telefone'] = encrypt(row['telefone'], s, t)
    print(row['telefone'])
    row['telefone'] = decrypt(row['telefone'], s, t)
    print(row['telefone'])


    # row['telefone'] = fernet.encrypt((row['telefone']).encode())
    # print(row['telefone'])
    # print(fernet.decrypt(row['telefone']).decode())

# Send data from imported csv file (fornecedor) to Database
# fornecedores.to_sql('fornecedor', engine, if_exists='append', index = False)

# Send data from imported csv file (nota fiscal) to Database
# nota_fiscal.to_sql('nota_fiscal', engine, if_exists='append', index = False)
