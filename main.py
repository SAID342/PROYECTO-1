def saludo (nombre: str ) -> str:
    return f"hola,{nombre}! bienvenido a Git."

if __name__ == "__main__":
    nombre =input("¿tu nombre?")
    print(saludo(nombre))