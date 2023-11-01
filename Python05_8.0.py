fav_dict = {'Livro' : 'Use a cabeça com Python',
             'Som' : 'Sem medo de ser feliz',
             'Árvore' : 'Mangueira',
             'Organismo' : 'Cachorro'}

while True:
    print("Essas são as chaves existentes no dicionário")
    for x in fav_dict.keys():
        print(f'.{x}')
    fav_thing = input("Digite a chave do dicionário para Alteração: ")
    if fav_thing in fav_dict.keys():
       alterado = input(f"Digite seu {fav_thing} favorito: ")
       fav_dict[fav_thing] = alterado
    else:
        print("Digite uma chave existente por favor!")
        continue