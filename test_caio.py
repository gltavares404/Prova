usuarios = []

while True:
    print('Bem vindo ao NossoApp')
    print()
    print('Escolha uma das opções a baixo')
    print()
    print('1 - Fazer cadastro')
    print('2 - Fazer login')
    print('3 - Sair do sistema')
    print()
    valor_opcao = input('Digite o número de qual opção você deseja: ')

    if valor_opcao == '1':
        usuario = input('Cadastre seu usuário: ')
        senha = input('Cadastre sua senha: ')
        usuarios.append({'usuario': usuario, 'senha': senha})
        print('Cadastro realizado com sucesso!')

    elif valor_opcao == '2':
        usuario = input('Digite o nome do usuário: ')
        senha = input('Digite a senha: ')
        for user in usuarios:
            if user['usuario'] == usuario and user['senha'] == senha:
                print('Login realizado com sucesso!')
                while True:
                    print('====PÁGINA INICIAL=====')
                    print('1 - Voltar para página de login')
                    print('2 - Sair do sistema')
                    print()
                    valor_opcao = int(input('Digite o número de qual opção você deseja: '))
                    if valor_opcao == 1:
                        break
                    elif valor_opcao == 2:
                        print('Você saiu do sistema!')
                        exit()
        else:
            print('Usuário ou senha incorretos, digite novamente.')
    elif valor_opcao == '3':
        print('Você saiu do sistema!')
        break
    elif valor_opcao != '3' and valor_opcao != '2' and valor_opcao != '1':
        print('Opção inválida, digite novamente.')
