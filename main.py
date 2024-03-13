from production_optimization.main import main as run_production_optimization
from integral.main import main as run_integral


def main():
    try:
        print("Which app do you want to run? \n (1) Production optimization \n (2) Integral \n (q) Quit \n")
        action = input()

        if action == "1":
            run_production_optimization()

        elif action == "2":
            run_integral()

        elif action == "q":
            print("\nGood bye!")
            return
        else:
            print("\033[91mI don't understand that command\033[0m")

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


if __name__ == "__main__":
    main()
