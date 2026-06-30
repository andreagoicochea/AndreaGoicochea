# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu(None,['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['1-circle-fill','2-circle-fill', '3-circle-fill'], menu_icon=None, default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
#selected = option_menu(
 #   menu_title="Selecciona una sección: ", 
 #   options=['Inicio', 'Experiencia', 'Gráficos'], 
 #   icons=['person-heart', 'globe-americas', 'pencil-square'], 
  #  menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Andrearama</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("andreafotobw.jpeg", caption='Andrea', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
   ¡Hola, mi nombre es Andrea Goicochea! Soy una persona curiosa, responsable y con muchas ganas de aprender cosas nuevas. Soy de Lima y actualmente estudio periodismo. Elegí esta carrera porque me encantan las oportunidades que te brinda la carrera para el desarrollo personal, permitiendo a uno desenvolverse desde la fotografía hasta la escritura, oratoria, etc.

Lo que más me gusta de mi carrera es la posibilidad de conocer distintas realidades y contar historias que pueden generar un impacto en las personas. Asimismo, me motiva no solo desarrollar habilidades de comunicación, sino poder investigar a profundidad y aprender a transmitir información de manera clara y responsable.

Aunque aún tengo dudas sobre en qué rama especializarme, tengo opciones como el fotoperiodismo o el periodismo de investigación. Siempre me han gustado temas relacionados con política y coyuntura nacional y considero que desde estos enfoques puedo impactar periodísticamente a la sociedad. 

En mi tiempo libre disfruto fotografiar, escuchar música, ver películas y leer. Me considero una cinéfila en su totalidad y me apasiona descubrir nuevas películas y cine de arte. Del mismo modo, últimamente he retomado mi hobby de la lectura de manera frecuente y siempre me gusta acompañarlo de un café bien cargado. 

Me gusta pensar que hay infinitas cosas y personas por descubrir siempre. 
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'> Video informativo 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Video realizado como parte de una entrega asincrónica (PC1) sobre operadores boleanos, especificamente, operadores de pertenencia y lógicos. 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://www.youtube.com/watch?v=vG2zsCXrz3w")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta una explicación de los conceptos fundamentales de ambos tipos de operadores, su funcionamiento y la forma en que se utilizan mediante ejemplos prácticos, con el propósito de comprender su aplicación en la programación. "
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    # st.subheader("🎥 Video 1 - Google Drive")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    #st.link_button(
            #"Ver video",
            #"https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link"
       # )
    # Agrega una breve descripción del video.
    #st.caption(
    #    "En este video se presenta ...., "
   # )

elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'> Gráficos 📊</h2>", unsafe_allow_html=True)

    graficos = ['Nube de palabras','Gráfico 1', 'Gráfico 2','Gráfico 3', 'Mapa']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
  
    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Nube de palabras':
        # Título de la sección
        st.subheader("☁️ Nube de palabras: A dónde va el viento")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
Se creó una nube de palabras haciendo uso de un diccionario obtenido previamente. A partir de este diccionario, se generó una representación visual en la que el tamaño de cada palabra refleja su frecuencia de aparición, facilitando la identificación de los términos más relevantes del texto analizado, es decir, la letra de una canción de Julieta Venegas.            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "nubedepalabras.png",
                width=800
            )
    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico 1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Rendimiento de Barcelona como participante")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Aquí debe ir una breve interpretación de tu gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "graficopastel.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico 2':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Promedio de tarjetas rojas por cada equipo como local")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "graficohistograma.png",
                width=800
            )
    elif grafico_seleccionado == 'Gráfico 3':
        # Título de la sección
        st.subheader("📊 Gráfico 3: Análisis de goles del Barcelona:Temporada 2025-2026")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "graficobarras.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa':
        # Título de la sección
        st.subheader("🗺️ Mapa: Mapa Interactivo")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapadepeliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
