from Interpolacion import table, get_corner, draw_picture, newton, lagrange
from Metodos_numericos import RK4


def main():
    while True:
        print("MENU")
        inp = int(input("1.- Inter\n2.- RK4\n3.- Salir\n"))
        if inp == 1:
            x = float(input("x : "))  # 0.54
            x_1 = [
                float(item) for item in input("lista x_1 : ").split(",")
            ]  # [0.4, 0.5, 0.6, 0.7, 0.8]
            y_1 = [
                float(item) for item in input("lista y_1 : ").split(",")
            ]  # [-0.9163, -0.6931, -0.5108, -0.3567, -0.2231]
            middle = table(x_1, y_1)
            n = get_corner(middle)
            newt = newton(n, x, x_1)
            lagr = lagrange(x_1, y_1, 0.54)
            # print("Verdadero valor: {}".format(math.log(0.54, math.e)))
            print("Interpolación de Lagrange: {}".format(lagr))
            print("Interpolación de Newton: {}".format(newt))
            # Dibujar
            draw_picture(x_1, y_1, (x, newt))
        if inp == 2:
            string_user = input("Introduce ecuacion: ")  # "1"
            t0 = int(input("Introduce el valor de t0:"))
            y0 = int(input("Introduce y0: "))
            h = float(input("Introduce el valor de h: "))
            n = int(input("Introduce el valor de n: "))
            val = RK4(string_user, t0, y0, h, n)  # t0 = 0 | y0 = 2 | h = 0.01 | n = 100
            print("Valor al que se debe aproximar por ejemplo: " + val)
        if inp == 3:
            break
    pass


if __name__ == "__main__":
    main()
