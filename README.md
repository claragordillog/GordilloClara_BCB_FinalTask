# **GordilloClara\_BCB\_FinalTask**

Final task for the Basic Digital Skills for Computational Biology course- Clara Gordillo

### 

Este proyecto forma parte del Final Task del Curso de Competencias Digitales Básicas para Biología Computacional del CSIC y consiste en el análisis de archivos SAM (Sequence Alignment/Map) mediante un script en Python y su integración en un workflow de Nextflow que ejecuta el programa, utilizando uv para gestionar dependencias.

### 

### **Descripción del proyecto:**

El objetivo es procesar un archivo SAM para que:



* Cuente el número total de lecturas alineadas
* Identifique cuántas tienen un valor de MAPQ = 60
* Calcular el porcentaje correspondiente



El programa ignora las cabeceras del archivo SAM y analiza únicamente las líneas de alineamiento.



Para ello, las tecnologías empleadas son:

* Python 3
* Librería rich para formateo de salida
* uv para gestión del entorno y dependencias
* Nextflow para el pipeline





### **Estructura del proyecto:**

Dentro del proyecto-sam/

* main.py--> # Script principal en Python
* main.nf--> # Pipeline de Nextflow
* pyproject.toml--> # Configuración del proyecto (uv)
* README.md--> # Documentación



### **Instalación:**

1. **Clonar el repositorio:**



*git clone https://github.com/claragordillog/GordilloClara\_BCB\_FinalTask.git*

*cd proyecto-sam*



**2. Inicializar entorno con uv:**



*uv sync*



Ejecutar el script directamente

uv run python3 main.py ruta/al/archivo.sam



**Ejemplo entrada esperada:**

*python3 main.py \~/dia9/nf/2-Align/WT.sam*



**3. Pipeline con Nextflow:**



Para ejecutar el análisis mediante pipeline:



nextflow run main.nf --sam ruta/al/archivo.sam





Finalmente, lo que muestra el programa es una tabla resumen con dos columnas con métricas analizadas (total de lecturas alineadas, lecturas con MAPQ y porcentaje) y valor obtenido de cada una de ellas. 





### **Conocimiento necesario:**

FASTQ: contiene lecturas crudas de secuenciación

SAM: contiene esas lecturas alineadas al genoma

MAPQ: calidad del alineamiento

