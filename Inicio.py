import streamlit as st
from PIL import Image
from pages import Consulta_Pacientes_IREN

favicon = "images/ucsp.ico"
st.set_page_config(layout="wide",
    page_title="Multipage App",
    page_icon=favicon,
)


st.title(':green[Proyecto de Desarrollo Tecnológico]')
st.header('Construcción de un prototipo electromagnético capaz de medir propiedades dieléctricas de tejidos biológicos no homogéneos en ambiente controlado, basado en una sonda coaxial de circuito abierto')
st.sidebar.success("Selecciona una página")

image = Image.open('images/logo.png')
st.sidebar.image(image)
st.sidebar.markdown("***")

consult = st.button("Consulta de Pacientes IREN")
if consult:
    Consulta_Pacientes_IREN.page_content()

website_url = "https://ucsp.edu.pe/video-mabis-brasier-ayudara-masificar-deteccion-temprana-cancer-de-mama/"	
col1, col2 = st.columns(2)

with col1:

	
	st.markdown("***")

	":green[Este proyecto tiene como objetivo ayudar en la construcción de un prototipo electromagnético capaz de analizar las propiedades dieléctricas de los tejidos humanos (Enfoque tejidos mamarios), se integran diferentes líneas de investigación( Radiofrecuencia, control y automatización, telemática y procesamiento de señales).]"

	":green[Inicialmente el proyecto necesita de apoyo en los siguientes puntos:]"
	":green[- Medición de propiedades dieléctricas de tejidos biológicos In vivo, Ex-vivo(Cirugía).]"
	":green[- Medición de propiedades dieléctricas de tejidos biológicos In vivo(Quimioterapia). ]"
	":green[- Medición de propiedades dieléctricas de tejidos biológicos In vivo(Radiología).]"
	":green[- Desarrollo de programación  frontend, página web.]"
	":green[- Programación de App en MIT app inventor. ]"
	":green[- Apoyo en sistema y circuito de control de mesa automatizada. ]"
	":green[- Apoyo en diseños mamarios anatómicos realistas en 3D.]"




	st.markdown("***")
	


with col2:
	st.markdown("***")
	
	st.write(':blue[Figura 1: Instituto Regional de Enfermedades Neoplasicas del Sur (IREN)]')
	image = Image.open('images/iren.jpg')
	st.image(image)
	
	st.write(':blue[Figure 2: Model Outputs and Inputs]')
	image = Image.open('apply.jpg')
	st.image(image)

with col1:
	
	":green[Instituto Regional de Enfermedades Neoplasicas del Sur (IREN)]"

	"Este proyecto se realiza en alianza con el Instituto Regional de Enfermedades Neoplásicas del Sur al igual que el proyecto MABIS."


	"IREN Sur desarrolla actividades del Sector Salud, para la atención especializada del cáncer y hospitalización, en el ámbito macrorregional, fue creado mediante la Ordenanza Regional Nº 057-2008-AREQUIPA de fecha 17 de Junio del 2008, incorporándolo a la estructura orgánica del Gobierno Regional de Arequipa."

	
	st.markdown("[Ver más sobre MABIS](https://ucsp.edu.pe/video-mabis-brasier-ayudara-masificar-deteccion-temprana-cancer-de-mama/)")
	st.markdown("***")
	":green[Sensor usado para las mediciones]"

	"Other scenarios can also be investigated in the model."

	"For example, the mean lengths-of-stay of different surgical types, and the number of ring-fenced beds available to patients can be changed to understand \
	effects on surgical throughput."
	
	"Additionally, the mean number of days delayed can be changed.  This represents a proportion of patients whose ward length-of-stay\
	is delayed for various reasons, such as awaiting a community package of care. The proportion of these patients can also be changed."



