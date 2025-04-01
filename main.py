from function import SistemaSolar

# ========================== Execução do Sistema ==========================
def main():
    """ Função principal do sistema """
    sistema = SistemaSolar()

    while True:
        print("\n📚 Sistema de Planetas")
        print("1️⃣ - Adicionar Planeta")
        print("2️⃣ - Listar Planetas")
        print("3️⃣ - Gerar Relatório")
        print("4️⃣ - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("📖 Nome do planeta: ")
            localização = input("⏳ Localização: ")
            diametro = input("🎯 Diametro do planeta: ")
            sistema.inserir_planeta(nome, localização, diametro)

        elif escolha == "2":
            sistema.listar_planetas()

        elif escolha == "3":
            sistema.gerar_relatorio_sistema_solar()

        elif escolha == "4":
            print("\n✅ Sistema finalizado. Até logo!\n")
            break

        else:
            print("\n⚠ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
