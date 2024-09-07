import streamlit as st
import psycopg2


# Esta conexión se utiliza para consultas más especializadas CUARTO
def get_connection():
    conn = psycopg2.connect(
        host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
        database="db_ejemplo",  # Cambia esto al nombre de tu base de datos
        user="postgres",  # Cambia esto al usuario de PostgreSQL
        password="root"  # Cambia esto a tu contraseña de PostgreSQL
    )
    return conn

# Esta función renderiza el formulario y tiene la lógica para insertar elementos TERCERO
def insert_element():    
# Botón para insertar datos
    name = st.text_input("Nombre")
    pet = st.text_input("Mascota")
    if st.button("Insertar registro"):
        if name and pet:
            try:
                # Conecta a la base de datos
                conn = get_connection()
                cursor = conn.cursor()
                print("hola3")

                # Inserta los datos
                insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
                cursor.execute(insert_query, (name, pet))
                
                # Confirma la transacción
                conn.commit()
                list_elements(cursor, conn)
                st.success("Registro insertado exitosamente")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            st.warning("Por favor, completa todos los campos")

def list_elements(cursor, conn):
    try:
        # Realiza la consulta para obtener todos los registros
        select_query = "SELECT * FROM mytable"
        cursor.execute(select_query)
        registros = cursor.fetchall()
        # Muestra los registros
        if registros:
            for registro in registros:
                st.write(f"Nombre: {registro[0]}, Mascota: {registro[1]}")
        else:
            st.write("No se encontraron registros.")

    except Exception as e:
        st.error(f"Ocurrió un error al listar los registros: {e}")

def list_elements_button():
    if st.button("Listar registros"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            # Realiza la consulta para obtener todos los registros
            select_query = "SELECT * FROM mytable"
            cursor.execute(select_query)
            registros = cursor.fetchall()
            # Muestra los registros
            if registros:
                for registro in registros:
                    st.write(f"Nombre: {registro[0]}, Mascota: {registro[1]}")
            else:
                st.write("No se encontraron registros.")

        except Exception as e:
            st.error(f"Ocurrió un error al listar los registros: {e}")
        finally:
            cursor.close()
            conn.close()
            print("hola")
            print("hola2")

def update_element():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Obtener todos los nombres para listar
        select_query = "SELECT name FROM mytable"
        cursor.execute(select_query)
        nombres = cursor.fetchall()

        # Lista desplegable para seleccionar el nombre
        nombre_seleccionado = st.selectbox("Selecciona el nombre a actualizar", [n[0] for n in nombres])

        # Nuevos valores para actualizar
        new_pet = st.text_input("Nueva mascota")

        if st.button("Actualizar registro"):
            if nombre_seleccionado and new_pet:
                try:
                    # Consulta de actualización
                    update_query = "UPDATE mytable SET pet = %s WHERE name = %s"
                    cursor.execute(update_query, (new_pet, nombre_seleccionado))

                    # Confirma la transacción
                    conn.commit()
                    list_elements(cursor, conn)
                    st.success(f"Registro actualizado exitosamente: {nombre_seleccionado} ahora tiene la mascota {new_pet}")
                except Exception as e:
                    st.error(f"Ocurrió un error al actualizar el registro: {e}")
                finally:
                    cursor.close()
                    conn.close()
            else:
                st.warning("Por favor, completa todos los campos para actualizar")

    except Exception as e:
        st.error(f"Ocurrió un error al conectar a la base de datos: {e}")
    finally:
        if conn:
            conn.close()


# función inical, se encarga de orquestar la app indicando que metodos se deben renderizar desde el inicio SEGUNDO
def init_app():
    insert_element()
    list_elements_button()
    update_element()
   
    
# Ejecuta las consultas cuando se inicia la aplicación PRIMERO
if __name__ == "__main__":
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    init_app()

