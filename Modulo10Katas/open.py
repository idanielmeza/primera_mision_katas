#def main():
#    open("/path/to/mars.jpg")

# def main():
#     try:
#         open('config.txt')
#     except FileNotFoundError:
#         print('Error al abrir el archivo')

def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()