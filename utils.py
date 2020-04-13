from models import Pessoas, Usuarios
# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=27)
    print(pessoa)
    pessoa.save()
# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Igor').first()
    print(pessoa.idade)
#  Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Igor').first()
    pessoa.idade = 21
    pessoa.save()
#  Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Luiz','123')
    insere_usuario('Felipe', '123')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()