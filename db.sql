create table tca_tco.pessoa(

    id int identity(1,1) primary key,
    nome nvarchar(255)
);

create table tca_tco.pessoa_documentos(

    id int identity(1,1) primary key,
    cpf nvarchar(20),
    rg varchar(15),
    data_nascimento date
);

create table tca_tco.grade(

    id int identity(1,1) primary key,
    descricao varchar(150)
);

create table tca_tco.produto(

    id int identity(1,1) primary key,
    descricao varchar(255),
    id_ncm int,
    grade int
);

create table tca_tco.produto_grade(

    id int identity(1,1) primary key,
    id_produto int,
    id_grade int,
    valor_custo_un decimal(18,2),
    valor_venda_un decimal(18,2)
);

create table tca_tco.vendas(

    id int identity(1,1) primary key

);

