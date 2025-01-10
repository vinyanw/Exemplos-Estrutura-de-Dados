class Playlist:
    def __init__(self):
        self.stack = []

    def adicionarMusica(self, music):
        self.stack.append(music)
        print(f'Música "{music}" adicionada à playlist.')

    def tocarUltimaAdicionada(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Não há música adicionada (NULL)"

    def exibirMusicas(self):
        if self.stack:
            print("\nPlaylist:")
            for idx, music in enumerate(self.stack[::-1], start=1):
                print(f"{idx}. {music}")
        else:
            print("\nPlaylist:\n1. NULL")

playlist = Playlist()

while (1):
    print("\nMenu:")
    print("1. Adicionar música à playlist")
    print("2. Tocar última música adicionada")
    print("3. Exibir lista total")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        musica = input("Digite o nome da música: ")
        playlist.adicionarMusica(musica)
    elif escolha == "2":
        print(f"Tocando: {playlist.tocarUltimaAdicionada()}")
    elif escolha == "3":
        playlist.exibirMusicas()
    elif escolha == "4":
        print("Encerrando o programa.")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
