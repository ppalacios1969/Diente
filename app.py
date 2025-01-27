import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie




image=Image.open("imagenes/CliDent a.png")
st.image(image, use_container_width=True)


url="https://lottie.host/ecb38580-bf7f-409a-b0be-8ba012215819/8OOHhJLKfw.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()
lottie=load_lottie(url)

#intro
with st.container():
    st.title("Hola somos CliDent 👋")
    st.subheader("Somos un grupo de odontólogos, enfocados en ayudarte a recuperar o mantener tu salud bucodental")
    

#sobre nosotros
with st.container():
    st.write("- - -")
    animation_column,text_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🔍")
        st.write(
            """
            Lo primero que debes de saber es que en una primer visita no hay pinchazos no tratamientos dolorosos
            de ningun tipo. El odontólogo se limita a estudiar y evaluar el estado general de tu salud bucodental, 
            antes de proponer tratamientos concretos si son necesarios ¿ Qué se hace en una primera visita?:

            -✅Historia Clinica
             Antes de examinar tus dientes tu odontólogo querrá saber cómo es el estado de tu salud en general. Para 
             ello se realizará un cuestionario que refleje toda la información relevante sobre tu salud.

            -✅Exploración y Revisiones
             Exploración bucodental: Después,en el sillón, tu dentista estudiará el estado de tus dientes y tu boca
             ayudándose del pequeño espejo circular con el que todos estamos familiarizados.

            -✅Diagnóstico y Tratamiento
             Después de haber efectuado toda la exploración , tu dentista te hará un diagnóstico personalizado y te 
             propondrá los tratamientos más adecuados para resolver los problemas que ha detectado.

            ***Una vez que se ha asegurado que has entendido todo, el respaldo del sillón se enderezará y la primera
            consulta habrá concluido.😁***
            """
        )

        with animation_column:
           st_lottie(lottie, height=850,width=450)
    
  
 # Servicios
with st.container():
    st.write("- - -")
    st.header("Servicios 🩺")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column: 
        image=Image.open("imagenes/dentista.png")
        st.image(image,use_container_width=True)  
    with text_column:
        st.title("Servicio general del dentista")
        st.subheader("¡Manten tu sonrisa Siempre! 😁")

        st.subheader("Nuestro servicio incluye:")
        st.write("""
        - ✅ **Blancamiento de dientes**: Evaluamos tu caso para ofrecerte el mejor tratamiento.
        - ✅ **Resinas**: Realizamos la colocación de resinas con precisión.
        - ✅ **Limpieza dental**: Prevenir enfermedades de las encías y elimina la placa y sarro.
        - ✅ **Extracciones**: Evaluamos tu caso para ofrecerte la mejor opción.
        - ✅ **Cirugias de muelas del juicio**: Evaluamos tu caso para ofrecerte el mejor tratamiento.                  
        """)

        st.markdown("---")  # Línea divisoria para separar secciones
        st.write("[¡Agenda tu cita hoy y Manten tu sonrisa!](https://calendar.app.google/ANDRWRo7zEB2mumRA")
       # image=Image.open("imagenes/Dr Patricia.png")
       # st.image(image,caption="imagen centrada", width=200)
        

    image_column, text_column = st.columns((1,2))    
    with image_column: 
        image=Image.open("imagenes/endodontic.png")
        st.image(image,use_container_width=True)  
    with text_column:
        st.write("---")
        st.title("Servicio de Endodoncia")
        st.subheader("¡Salva tu sonrisa con elegir la Endodoncia! 😁")

        st.subheader("Nuestro servicio incluye:")
        st.write("""
        - ✅ **Alivio del dolor**: el tratamiento elimina la infección y el dolor, permitiéndote 
        volver a disfrutar de tus actividades diarias sin preocupación.
        - ✅ **Salva tu diente**: Mantén tus dientes naturales y evita extracciones innecesarias. 
        cada diente cuenta y merece ser salvado.         
        - ✅ **Procedimiento seguro y efectivo**: Nuestros profesionales están altamente capacitados
        y utilizan tecnología avanzada para garantizar un tratamiento seguro y exitoso.
        - ✅ **Recuperación rápida**: La mayoría de los paciente pueden retomar sus actividades 
        casi de inmediato. ¡ Sin dolor!.
          
        """)

        st.markdown("---")  # Línea divisoria para separar secciones

        st.write("[¡Agenda tu cita hoy y transforma tu sonrisa!]https://calendar.app.google/5pomPkE3PRJ5Zv8S9")
      #  image=Image.open("imagenes/Dr Jessica.png")
      #  st.image(image,caption="imagen centrada", width=200)
        st.write("---")
        st.markdown("---")  # Línea divisoria para separar secciones

    image_column, text_column = st.columns((1,2))    
    with image_column: 
        image=Image.open("imagenes/bracket.png")
        st.image(image,use_container_width=True)
    with text_column:
        st.write("---")
        st.title("Servicio de Brackets")
        st.subheader("¡Renueva tu sonrisa con brackets! 😁")

        st.subheader("Nuestro servicio incluye:")
        st.write("""
        - ✅ **Valoración inicial**: Evaluamos tu caso para ofrecerte el mejor tratamiento.
        - ✅ **Instalación de brackets**: Realizamos la colocación de brackets con precisión.
        - ✅ **Tratamiento personalizado**: Diseñamos un plan exclusivo para ti.
        """)

        st.markdown("---")  # Línea divisoria para separar secciones
        st.write("[¡Agenda tu cita hoy y transforma tu sonrisa!]https://calendar.app.google/DJVcVjC9zSFKGj127")
       # image=Image.open("imagenes/Dr Karina.png")
       # st.image(image,caption="imagen centrada", width=200)
                  
        imagenj=Image.open("imagenes/carita feliz.jpeg")
        st.image(imagenj,caption="imagen centrada",width=200)
    
       