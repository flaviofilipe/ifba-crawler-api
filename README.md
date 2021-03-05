
# IFBA Crawler API
Este projeto é um crawler do site do IFBA de Vitória da Conquista.
Ele acessa as noticias [deste site](https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista) e fornece uma API no formato JSON utilizando o microframework Flask .
  
  
# Pré Requesitos  
  
- Python v3.x
  
# Instalação  
  
**Instalando dependências**  
```  
pipenv install  
```  
  
**Terminal do ambiente virtual**  
```  
pipenv shell  
```  
  
# Variáveis de ambiente  
  
- Copie o arquivo _.env_example_ para a raiz do projeto renomeando para **.env**;  
  
# Executar a aplicação  
  
  Execute o comando dentro do seu ambiente virtual
  ```
 flask run
  ```
# Endpoint
|Método| url | Descrição | Parâmetros
|--|--|--|--
| GET  | /noticias | Lista as noticias | b_start: Início da lista

