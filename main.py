##Programa en Python: análisis simple de un archivo SAM

import sys
from rich.console import Console
from rich.table import Table

console = Console()
def main():
# 1. Comprobar argumento
    if len(sys.argv) != 2:
        console.print("[bold red]La forma de ejecutar el programa es: python main.py <archivo.sam>[/bold red]")
        sys.exit(1)

    ruta = sys.argv[1]

    total_lecturas = 0
    mapq_60 = 0

# 2. Leer archivo línea a línea
    with open(ruta, mode="r", encoding ="utf-8") as f:
        for linea in f:
            linea = linea.strip()

# 3. Ignorar cabeceras
            if linea.startswith("@"):
                continue

# Contar lecturas
            total_lecturas += 1

# 4. Extraer MAPQ (columna 5)
            columnas = linea.split("\t")
            mapq = int(columnas[4]) # Con esto convertimos el str de la columna 5 (mapq) en un número 
        #Se pone 4 porque Python empieza por 0, entonces la columna 5 es el índice 4#

# 5. Contar MAPQ = 60
            if mapq == 60:
                mapq_60 += 1

# 6. Calcular porcentaje
    if total_lecturas > 0: # Esto lo hacemos porque un número entre 0 da error, así nos aseguramos que el cálculo se puede hacer.
        porcentaje = (mapq_60 / total_lecturas) * 100
    else:
        porcentaje = 0
#Mostramos los resultados y en vez de hacerlo con print sin más, nos aprovechamos de la librería rich para que se imprima como una tabla y quede visualmente más bonito
    tabla = Table(title="Resultados del análisis SAM")

    tabla.add_column("Métricas analizadas", style="cyan", justify="left")
    tabla.add_column("Valor obtenido", style="black", justify="left")

    tabla.add_row("Total de lecturas alineadas", total_lecturas, justify="left")
    tabla.add_row("Lecturas con MAPQ = 60", mapq_60, justify="left")
    tabla.add_row("Porcentaje", f"{porcentaje:.1f}%", justify="left")

    console.print(tabla)


if __name__ == "__main__":
    main()

