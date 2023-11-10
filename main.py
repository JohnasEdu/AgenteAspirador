from AgenteAspirador import Aspirador

def main():
    aspirador = Aspirador()
    aspirador.mostrar_status()

    while not aspirador.objetivo_alcancado() and aspirador.energia > 0:
        aspirador.aspirar_novamente()

    aspirador.mostrar_status_final()
if __name__ == "__main__":
    main()