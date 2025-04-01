
class SistemaSolar:
    def __init__(self):
        """ Inicializa o sistema com uma lista vazia para armazenar os planetas """
        self.planetas = []

    def inserir_planeta(self, nome, localização, diametro):
        """ Adiciona um novo planeta ao sistema """
        planeta = {
            "nome": nome,
            "localização": localização,
            "diametro": diametro
        }
        self.planetas.append(planeta)
        print("\n✅ planeta cadastrado com sucesso!\n")

    def listar_planetas(self):
        """ Lista todas os planetas cadastrados """
        if not self.planetas:
            print("\n⚠ Nenhuma planeta cadastrada.\n")
            return
        print("\n📋 Planetas cadastrados:")
        for i, planeta in enumerate(self.planetas, 1):
            print(f"{i}. Nome: {planeta['nome']}, Localização: {planeta['localização']}, Diametro: {planeta['diametro']}")
        print()

    def gerar_relatorio_sistema_solar(self):
        """ Gera um relatório geral do sistema solar """
        print("\n📊 Relatório do Sistema Solar")
        print(f"Total de planetas cadastrados: {len(self.planetas)}\n")
        for i, planeta in enumerate(self.planetas, 1):
            print(f"Planeta {i}:")
            print(f"   📌 Nome: {planeta['nome']}")
            print(f"   📍 Localização: {planeta['localização']}")
            print(f"   🪐 Diametro: {planeta['diametro']}\n")