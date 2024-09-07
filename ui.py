import streamlit as st
from db import insert_record, get_all_records, delete_record_by_name, update_record

# Función para insertar un elemento
def insert_element():
    name = st.text_input("Nombre")
    pet = st.text_input("Mascota")
    if st.button("Insertar registro"):
        if name and pet:
            try:
                insert_record(name, pet)
                st.success("Registro insertado exitosamente")
                list_elements()
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
        else:
            st.warning("Por favor, completa todos los campos")

# Función para listar los elementos
def list_elements():
    try:
        records = get_all_records()
        if records:
            for record in records:
                st.write(f"Nombre: {record[0]}, Mascota: {record[1]}")
        else:
            st.write("No se encontraron registros.")
    except Exception as e:
        st.error(f"Ocurrió un error al listar los registros: {e}")

# Botón para listar los elementos
def list_elements_button():
    if st.button("Listar registros"):
        list_elements()

# Función para eliminar un registro
def delete_element():
    name_to_delete = st.text_input("Nombre del registro a eliminar")
    if st.button("Eliminar registro"):
        if name_to_delete:
            try:
                rows_affected = delete_record_by_name(name_to_delete)
                if rows_affected > 0:
                    st.success("Registro eliminado exitosamente")
                    list_elements()
                else:
                    st.warning("No se encontró un registro con ese nombre.")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
        else:
            st.warning("Por favor, ingresa el nombre del registro a eliminar")

# Función para actualizar un registro
def update_element():
    name_to_update = st.text_input("Nombre del registro a actualizar")
    new_name = st.text_input("Nuevo nombre")
    new_pet = st.text_input("Nueva mascota")
    if st.button("Actualizar registro"):
        if name_to_update and new_name and new_pet:
            try:
                rows_affected = update_record(name_to_update, new_name, new_pet)
                if rows_affected > 0:
                    st.success("Registro actualizado exitosamente")
                    list_elements()
                else:
                    st.warning("No se encontró un registro con ese nombre.")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
        else:
            st.warning("Por favor, completa todos los campos")
