
# PyAtom Ferramenta de ORM    

 O projeto foi criado no intuito de aprendizado para reproduzir a e entender como os ORMs funcionam    
no mesmo intuito fio desenvolvido para dar mais liberdade e facilidade para manipulação entre multiplos banco de dados uma vez que é possível controlar as conexões.    
    
Outro diferencial, é que o mapeamento é feito do banco para o objeto e não o contrario, com isto é capaz de gerar todas as classes necessárias com base nas tabelas já criadas, facilitanto também na migração de sistemas.    
    
Aqui está sendo usado em uma API mas assim que estiver pronta será separada    
    
    
## Suporte e conexões com DB    
 ### conexão com sqlserver   
 pip install pymssql   
  
### conexao com postgres   
 pip install py-postgresql   
### conexao com mysql   
 pip install mysql-connector  
 
## Configurações iniciais

no diretorio root de sua aplicação crie um arquivo .json com o nome pyAtom_config.json
e insira as segintes configurações:

    {  
      "app_name": "nome_aplicação",  
      "generate_models": true,  
      "generate_handler": true,  
      "generate_controllers": true,  
      "connection_db": {  
	      "db": "nome_banco",  
	      "url": "host",  
	      "port": "porta_db",
	      "db_name": "batatinha"  
	      "password": "sua_senha",  
	      "user": "seu_usuario"  
      },  
      "ignore_gen": [  
        "controller","handler"  
      ]  
    }

 - app_name: nome aplicação
 - generate_models: true para gerar os models com base nas tabelas do banco
 - generate_handler: true para gerar os handlers com base nas tablelas do banco
 - generate_controllers: true para gerar os codigos das classes dos endpoints com base nas tabelas do banco
 - connection_db: objeto que contem as configurações de conexão padrão
	 - db: nome do banco de dados, valores aceitos:
		 - MSSQL: Sql Server
		 - POSTGRES: postgres
		 - MYSQL: MySql
		 - FIREBIRD: Firebird
	 - url: host da conexao
	 - port: porta da conexão com banco
	 - db_name: nome do banco
	 - password: senha do banco
	 - user: usuario
 - ignore_gen: ignora na hora de regerar as classes, valores aceitos:
	 - controller
	 - handler
	 - model
