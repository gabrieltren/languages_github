# Script para buscar as linguagens mais utilizadas no GitHub

-> Script leva em consideração todas os repositórios privados e públicos do usuário, com isso necessita de autorização
 - Uso do Token Classic gerado pelo próprio GitHub.

### Variáveis de ambiente 

 ## TOKEN
  - Token Classic (Obrigatório)

 ## IGNORE
  - Tupla (CSV) de Linguagens a serem utilizadas (Opcional)



### Uso

-> Pode ser usado para portfólios, para mostra o uso das linguagens mesmo aquelas que se usa em repositório privado
-> Interessante utilizar com algum agendador de tarefa (por exemplo: Celery), se usa diariamente o GitHub, pois pode ficar atualizando já que não é tao performático por ter que fica usando a API do GitHub


# Obs:
### Em `api_github.repos`, na função `repos_user()`, pode-se retirar o parâmetro `"affiliation": "owner"`, nesse caso irá retornar para todos os repositórios que o usuário do token tenha acesso.


