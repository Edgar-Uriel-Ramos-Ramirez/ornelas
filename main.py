# from Interpolacion import mamadas_kramer
from Metodos_numericos import RK4


def main():
    while True:
        print("MENU")
        inp = int(input("1.- Inter\n2.- RK4\n3.- Salir\n"))
        if inp == 2:
            string_user = input("introduce ecuacion ")  # "t * exp(3 * t) - 2 * y"
            val = RK4(string_user, 0, 2, 0.01, 100)
            print(val)
        if inp == 3:
            break
    pass


if __name__ == "__main__":
    main()
