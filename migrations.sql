CREATE TABLE fornecedor(
    id uuid DEFAULT uuid_generate_v4 (),
    nome VARCHAR,
    cnpj VARCHAR,
    telefone VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE nota_fiscal(
    id uuid DEFAULT uuid_generate_v4 (),
    numero_nota INT,
    fornecedor uuid,
    data_emissao DATE,
    nome_produto VARCHAR,
    categoria_produto VARCHAR,
    quantidade NUMERIC(1000, 2),
    valor_total NUMERIC(1000, 2),
    CONSTRAINT fk_nota_fiscal_fornecedor FOREIGN KEY(fornecedor) REFERENCES fornecedor(id),
    PRIMARY KEY (id)
);

CREATE TABLE contas_a_pagar (
    id uuid DEFAULT uuid_generate_v4 (),
    fornecedor uuid,
    data_vencimento DATE,
    pago BOOLEAN,
    notas_fiscais uuid [],
    CONSTRAINT fk_contas_a_pagar_fornecedor FOREIGN KEY(fornecedor) REFERENCES fornecedor(id),
    CONSTRAINT fk_contas_a_pagar_nota_fiscal FOREIGN KEY(nota_fiscal) REFERENCES nota_fiscal(id),
    PRIMARY KEY (id)
);