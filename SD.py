import streamlit as st

class Paciente:
    def __init__(self, nombre_completo, fecha_ingreso, habitacion_cama, frecuencia_respiratoria, frecuencia_cardiaca, presion_arterial, temperatura, saturacion_oxigeno, tipo_via, sonda_vesical, sonda_nasogastrica, observaciones=""):
        self.nombre_completo = nombre_completo
        self.fecha_ingreso = fecha_ingreso
        self.habitacion_cama = habitacion_cama
        self.frecuencia_respiratoria = frecuencia_respiratoria
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self.presion_arterial = presion_arterial
        self.temperatura = temperatura
        self.saturacion_oxigeno = saturacion_oxigeno
        self.tipo_via = tipo_via
        self.sonda_vesical = sonda_vesical
        self.sonda_nasogastrica = sonda_nasogastrica
        self.observaciones = observaciones

    def mostrar_informacion(self):
        return f"""
        Nombre Completo: {self.nombre_completo}
        Fecha de Ingreso: {self.fecha_ingreso}
        Habitación y Cama: {self.habitacion_cama}
        Frecuencia Respiratoria: {self.frecuencia_respiratoria} rpm
        Frecuencia Cardiaca: {self.frecuencia_cardiaca} bpm
        Presión Arterial: {self.presion_arterial} mmHg
        Temperatura: {self.temperatura} °C
        Saturación de Oxígeno: {self.saturacion_oxigeno} %
        Tipo de Vía: {self.tipo_via}
        Sonda Vesical: {"Sí" if self.sonda_vesical else "No"}
        Sonda Nasogástrica: {"Sí" if self.sonda_nasogastrica else "No"}
        Observaciones: {self.observaciones}
        """

# Interfaz con Streamlit
st.title("Registro de Enfermería")
st.subheader("Complete la Información del Paciente")

nombre_completo = st.text_input("Nombre y Apellido")
fecha_ingreso = st.date_input("Fecha de Ingreso")
habitacion_cama = st.text_input("Habitación y Cama")
frecuencia_respiratoria = st.number_input("Frecuencia Respiratoria (rpm)", min_value=0, step=1)
frecuencia_cardiaca = st.number_input("Frecuencia Cardiaca (bpm)", min_value=0, step=1)
presion_arterial = st.text_input("Presión Arterial (mmHg)")
temperatura = st.number_input("Temperatura (°C)", min_value=0.0, step=0.1)
saturacion_oxigeno = st.number_input("Saturación de Oxígeno (%)", min_value=0, max_value=100, step=1)
tipo_via = st.text_input("Tipo de Vía")
sonda_vesical = st.radio("Sonda Vesical", ["Sí", "No"]) == "Sí"
sonda_nasogastrica = st.radio("Sonda Nasogástrica", ["Sí", "No"]) == "Sí"
observaciones = st.text_area("Observaciones")

if st.button("Guardar Información"):
    paciente = Paciente(
        nombre_completo=nombre_completo,
        fecha_ingreso=fecha_ingreso,
        habitacion_cama=habitacion_cama,
        frecuencia_respiratoria=frecuencia_respiratoria,
        frecuencia_cardiaca=frecuencia_cardiaca,
        presion_arterial=presion_arterial,
        temperatura=temperatura,
        saturacion_oxigeno=saturacion_oxigeno,
        tipo_via=tipo_via,
        sonda_vesical=sonda_vesical,
        sonda_nasogastrica=sonda_nasogastrica,
        observaciones=observaciones
    )
    st.success("Información guardada con éxito.")
    st.subheader("Información del Paciente")
    st.text(paciente.mostrar_informacion())
