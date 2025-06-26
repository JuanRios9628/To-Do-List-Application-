# To-Do-List-Application-
# 📝 To-Do List Manager (Python CLI App)

Este proyecto fue desarrollado como parte de una colaboración en grupo para aprender los conceptos básicos de programación en Python, gestión de tareas, estructuras de datos y visualización. Es una aplicación simple de consola para gestionar listas de tareas.

## 📌 Funcionalidades principales

- ✅ Agregar tareas con:
  - Nombre
  - Categoría (ej. Escuela, Trabajo, Salud...)
  - Prioridad (🔥 Muy alta - 🟣 Muy baja)
  - Fecha de entrega
  - Frecuencia (diaria, semanal, mensual, ninguna)
  Ver tareas organizadas por prioridad y fecha
  Mostrar progreso con gráfico circular (matplotlib)
  Marcar tareas como completadas
  Simular envío de tarea por correo electrónico
   Recomendaciones de tareas importantes y resumen por categoría

## 🧠 Lógica especial

- Si una tarea ya existe y se repite, su **prioridad aumenta automáticamente** (disminuye el número, por ejemplo de 3 a 2).
- Se muestra una **barra de progreso en porcentaje** con un gráfico de pastel para visualizar el estado general de las tareas.
- Las tareas se **ordenan automáticamente** por prioridad y fecha.
- Las sugerencias ayudan a enfocarse en tareas de prioridad alta y próximas a vencer.

## 📂 Estructura del código

El programa está dividido en las siguientes secciones:

1. **Configuración global**: listas, etiquetas de prioridad y categorías.
2. **Funciones auxiliares**: validación de fechas, selección de categoría, frecuencia.
3. **Funciones principales**:
   - `add_task()`: Añadir nueva tarea o subir prioridad si ya existe.
   - `view_tasks()`: Ver tareas y progreso.
   - `mark_task_completed()`: Marcar como completada.
   - `simulate_send_email()`: Simular envío de correo.
   - `suggest_task()`: Sugerencias y resumen por categoría.
4. **Menú interactivo** con ciclo `while`.

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `matplotlib` (para gráficos)

Puedes instalar matplotlib con:

```bash
pip install matplotlib
🚀 Cómo ejecutar
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/to-do-list-python.git
cd to-do-list-python
Ejecuta el script principal:

bash
Copiar
Editar
python nombre_del_archivo.py
