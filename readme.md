

🏋️‍♂️================================================== 🏋️‍♂️
    REGISTRO DE ENTRENAMIENTOS (GYM) - README
🏋️‍♂️ ================================================== 🏋️‍♂️

📌 DESCRIPCIÓN
Programa en Python que permite registrar ejercicios, ver el historial
semanal, calcular el progreso y buscar ejercicios pasados.


🧩 ELEMENTOS QUE UTILIZAMOS
--------------------------------------------------

📋 Historial = []
   Lista global donde guardamos todos los entrenamientos.
   Cada entrenamiento se guarda como un DICCIONARIO con las claves:
   "dia", "ejercicio", "peso" y "reps".
   ➡️ Nos permite tener varios datos organizados bajo un mismo registro.

🛠️ def (funciones)
   Separan cada tarea del programa para que el código quede ordenado.
   ➡️ Cada función se encarga de una sola cosa (agregar, ver, calcular, buscar).

🔁 while
   Se usa en dos lugares:
   1️⃣ En el menú principal, para seguir mostrando las opciones hasta
       que el usuario elija "salir".
   2️⃣ Dentro de ejercicio_del_dia(), para validar que el usuario
       escriba un número y no otra cosa.

🔀 if / elif / else
   Decide qué función ejecutar según la opción elegida en el menú.
   ➡️ También compara si el peso subió, bajó o se mantuvo igual.

⌨️ input()
   Pide datos al usuario: ejercicio, peso, repeticiones, día, opción, etc.

🔎 for
   Recorre el Historial y filtra los ejercicios que coinciden con
   lo que el usuario busca.


⚙️ PARA QUÉ SIRVE CADA FUNCIÓN
--------------------------------------------------

🖥️ mostrar_menu()
   Imprime las opciones disponibles en pantalla.

➕ ejercicio_del_dia()
   Registra un nuevo ejercicio (día, nombre, peso, repeticiones)
   en Historial.

📅 ver_historial_semanal()
   Muestra todos los ejercicios guardados hasta el momento.

📈 calcular_progreso()
   Compara el primer y el último registro de un ejercicio para
   saber si hubo mejora.

🔍 buscar_ejercicio()
   Busca coincidencias por nombre dentro del Historial.


🎯 QUÉ BUSCAMOS CON ESTE PROGRAMA
--------------------------------------------------

El objetivo es que el usuario lleve un control simple de su rutina
de gym sin necesidad de anotarlo en papel:

   ✅ Que quede un registro ordenado de lo que entrenó cada día.
   ✅ Poder ver de un vistazo todo lo hecho en la semana.
   ✅ Saber si está progresando (subiendo peso) en un ejercicio.
   ✅ Encontrar rápido si ya hizo cierto ejercicio antes.

💡 En resumen: practicar el uso de FUNCIONES, LISTAS, DICCIONARIOS,
   BUCLES (while/for) y CONDICIONALES (if/elif/else) aplicados a
   un caso real y útil.

🏋️‍♂️ ================================================== 🏋️‍♂️
