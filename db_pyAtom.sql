create table cpf(

    id int identity(1,1) primary key,
    iddocumento int,
    cpf varchar(11),
    dataemissao date,
    idpessoa int
);

create table rg(

    id int identity(1,1) primary key,
    iddocumento int,
    rg varchar(11),
    dataemissao date,
    idpessoa int
);

create table pessoa_endereco(

    id int identity(1,1) primary key,
    idpessoa int,
    logradouro varchar(255),
    bairro varchar(70),
    numero varchar(10),
    complemento varchar(50),
    cep varchar(8)
);

create table pessoa_telefone(

    id int identity(1,1) primary key,
    idpessoa int,
    telefone varchar(20),
    tipo int
);

create table pessoa(

    id int identity(1,1) primary key,
    nome varchar(250),
    idade int,
    idTipoPessoa int
);

create table documentos(

    id int identity(1,1) primary key,
    idpessoa int
);


create table tipo_pessoa(

    id int identity(1,1) primary key,
    descricao varchar(50)
);


insert into tipo_pessoa(descricao) values('Fornecedor'),('Cliente'),('Usuário');