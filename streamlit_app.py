import streamlit as st
from ui import insert_element, list_elements_button, delete_element, update_element

# Función inicial para organizar las funcionalidades
def init_app():
    st.title("🎈 My new app")
    insert_element()  # Formulario para insertar elementos
    st.write("---")
    list_elements_button()  # Botón para listar elementos
    st.write("---")
    delete_element()  # Formulario para eliminar un registro
    st.write("---")
    update_element()  # Formulario para actualizar un registro

# Ejecuta la aplicación
if __name__ == "__main__":
    init_app()