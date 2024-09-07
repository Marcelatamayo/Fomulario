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

# función inical, se encarga de orquestar la app indicando que metodos se deben renderizar desde el inicio SEGUNDO
def init_app():
    insert_element()
    list_elements_button()
   
    
# Ejecuta las consultas cuando se inicia la aplicación PRIMERO
if __name__ == "__main__":
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    init_app()

