
import sqlite3
import os

# ==========================================
# MODULO 1. CREACION DE LA BASE DE DATOS
# ==========================================

def crear_bd():
    os.makedirs("database", exist_ok=True)

    conexion = sqlite3.connect("database/alumnos.db")

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumno (
                matricula TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                calle TEXT,
                colonia TEXT,
                padre_tutor TEXT,
                tel_tutor TEXT
            )
        """)

        conexion.commit()
        print("Base de datos creada correctamente.")

    except sqlite3.Error as error:
        print(f"Error al crear la base de datos: {error}")

    finally:
        conexion.close()


# ==========================================
# MODULO 2. ALTA DE ALUMNOS
# ==========================================

def alta_alumno():
    conexion = sqlite3.connect("database/alumnos.db")

    try:
        cursor = conexion.cursor()

        print("\n===== ALTA DE ALUMNO =====")

        matricula = input("Matricula: ").strip()
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        calle = input("Calle: ").strip()
        colonia = input("Colonia: ").strip()
        padre_tutor = input("Nombre del padre o tutor: ").strip()
        tel_tutor = input("Telefono del tutor: ").strip()

        # Validar campos obligatorios
        if not matricula or not nombre or not apellido:
            print("Error: matricula, nombre y apellido son obligatorios.")
            return

        # Registrar al alumno
        cursor.execute("""
            INSERT INTO alumno (
                matricula,
                nombre,
                apellido,
                calle,
                colonia,
                padre_tutor,
                tel_tutor
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            matricula,
            nombre,
            apellido,
            calle,
            colonia,
            padre_tutor,
            tel_tutor
        ))

        conexion.commit()
        print("\nAlumno registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: la matricula ya existe.")

    except sqlite3.Error as error:
        print(f"Error al registrar al alumno: {error}")

    finally:
        conexion.close()


# ==========================================
# MODULO 3. CONSULTAR ALUMNOS
# ==========================================

def consultar_alumnos():
    conexion = sqlite3.connect("database/alumnos.db")

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT matricula, nombre, apellido, calle,
                   colonia, padre_tutor, tel_tutor
            FROM alumno
            ORDER BY apellido, nombre
        """)

        alumnos = cursor.fetchall()

        print("\n===== LISTA DE ALUMNOS =====")

        if not alumnos:
            print("No hay alumnos registrados.")
            return

        for alumno in alumnos:
            print("-" * 40)
            print(f"Matricula: {alumno[0]}")
            print(f"Nombre: {alumno[1]} {alumno[2]}")
            print(f"Calle: {alumno[3] or 'No registrada'}")
            print(f"Colonia: {alumno[4] or 'No registrada'}")
            print(f"Padre o tutor: {alumno[5] or 'No registrado'}")
            print(f"Telefono: {alumno[6] or 'No registrado'}")

    except sqlite3.Error as error:
        print(f"Error al consultar alumnos: {error}")

    finally:
        conexion.close()


# ==========================================
# MODULO 4. MENU PRINCIPAL
# ==========================================

def menu():
    crear_bd()

    while True:
        print("\n===== SISTEMA DE ALUMNOS =====")
        print("1. Registrar alumno")
        print("2. Consultar alumnos")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            alta_alumno()

        elif opcion == "2":
            consultar_alumnos()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


# ==========================================
# EJECUCION DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    menu()
