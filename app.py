import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(key):
    try:
        return st.secrets[key]
    except:
        return os.getenv(key, "")

# ── Assets ────────────────────────────────────────────────────────────────────
LOGO_URL = "https://maive.es/wp-content/uploads/2024/11/cropped-clinica-estetica-lanzarote-maive-logo.png"

TRATAMIENTOS_SIDEBAR = [
    {
        "cat": "✦ Medicina Estética",
        "items": [
            {"n": "Full Face", "img": "https://maive.es/wp-content/uploads/2024/12/full-face-lanzarote-maive.png",
             "desc": "Protocolo de rejuvenecimiento facial integral que combina neuromoduladores, ácido hialurónico y bioestimuladores adaptados a cada paciente. Resultados naturales y armoniosos en una sola sesión planificada por nuestros médicos."},
            {"n": "HydraFacial", "img": "https://maive.es/wp-content/uploads/2024/12/hydrafacial-lanzarote-maive.png",
             "desc": "Tratamiento multiacción que en 3 pasos limpia, exfolia, extrae impurezas e hidrata la piel en profundidad mediante un sistema de vortex patentado. Sin dolor ni tiempo de recuperación. Resultados visibles desde la primera sesión."},
            {"n": "Neuromoduladores (Bótox)", "img": "https://maive.es/wp-content/uploads/2024/12/infiltracion-antiarrugas-lanzarote-maive.png",
             "desc": "Toxina botulínica que relaja los músculos responsables de las arrugas de expresión (frente, entrecejo, patas de gallo). Efecto natural visible en 3-7 días. Duración aproximada de 4-6 meses. Procedimiento rápido y mínimamente invasivo."},
            {"n": "Hilos Tensores", "img": "https://maive.es/wp-content/uploads/2024/11/hilos-tensores-lanzarote-maive.png",
             "desc": "Hilos biodegradables que tensan y reposicionan los tejidos faciales ofreciendo un efecto lifting inmediato sin cirugía. Estimulan además la producción de colágeno de forma progresiva. Duración de 12 a 18 meses."},
            {"n": "Harmonyca · Lifting sin cirugía", "img": "https://maive.es/wp-content/uploads/2024/02/lifting-sin-cirugia-maive-blog.png",
             "desc": "Combina ácido hialurónico con hidroxiapatita cálcica en un único producto. Efecto lifting inmediato más estimulación de colágeno a largo plazo. Ideal para restaurar volúmenes perdidos con resultados naturales y duraderos."},
            {"n": "LPG Endermologie Facial", "img": "https://maive.es/wp-content/uploads/2024/12/lpg-lanzarote-maive.png",
             "desc": "Masaje mecánico con cabezal de rodillos y succión que activa las células de la piel de forma no invasiva. Reafirma el óvalo facial, reduce la papada, mejora la textura cutánea y estimula el drenaje linfático."},
        ],
    },
    {
        "cat": "✦ Tratamientos Corporales",
        "items": [
            {"n": "Indiba Corporal", "img": "https://maive.es/wp-content/uploads/2024/11/corporal-lanzarote-maive.png",
             "desc": "Radiofrecuencia profunda que genera calor controlado en los tejidos internos. Reduce medidas, reafirma la piel, combate la celulitis y mejora la circulación. Protocolo habitual de 6 a 10 sesiones, 1-2 veces por semana."},
            {"n": "Embody Esculpt (EMS)", "img": "https://maive.es/wp-content/uploads/2025/01/embody-lanzarote.webp",
             "desc": "Tecnología de electroestimulación muscular (EMS) que tonifica músculos y elimina grasa de forma simultánea. Equivale a miles de contracciones en una sola sesión de 30 minutos. Sin esfuerzo, sin recuperación."},
            {"n": "Maderoterapia", "img": "https://maive.es/wp-content/uploads/2018/09/foto-maderoterapia.jpg",
             "desc": "Técnica de masaje con utensilios de madera que rompe los nódulos de grasa, activa la circulación linfática y remodela la silueta. Reduce la celulitis, mejora la textura de la piel y aporta un efecto drenante muy visible."},
        ],
    },
    {
        "cat": "✦ Cirugía Estética",
        "items": [
            {"n": "Blefaroplastia", "img": "https://maive.es/wp-content/uploads/2024/11/blefaroplastia-lanzarote-maive-cirugia.png",
             "desc": "Intervención quirúrgica que elimina el exceso de piel y grasa de los párpados superiores y/o inferiores. Mejora el aspecto (mirada más joven y descansada) y, en casos de ptosis severa, también la funcionalidad visual. Realizada por el Dr. Aaron Zapata, oftalmólogo especialista."},
        ],
    },
    {
        "cat": "✦ Rituales Yonka",
        "items": [
            {"n": "Viaje a la Polinesia", "img": "https://maive.es/wp-content/uploads/2025/01/ritual-viaje-polinesia-lanzarote-maive.png",
             "desc": "Ritual relajante con aceites esenciales exóticos y movimientos fluidos inspirados en la Polinesia. Libera tensiones profundas y transporta los sentidos a un estado de paz absoluta. 90 min · €90."},
            {"n": "Delicias Corsas Vitalité", "img": "https://maive.es/wp-content/uploads/2025/01/ritual-delicias-corsas-lanzarote-maive.png",
             "desc": "Ritual energizante con fragancias mediterráneas. Masaje estimulante que activa la circulación, tonifica los tejidos y recarga las pilas. Ideal para combatir el cansancio acumulado. 90 min · €90."},
            {"n": "Paseo por el Bosque", "img": "https://maive.es/wp-content/uploads/2025/01/ritual-paseo-por-el-bosque-lanzarote-maive.png",
             "desc": "Ritual de desconexión total con texturas, aromas y movimientos que evocan la naturaleza. Relajación mental y física profunda para olvidarse del mundo exterior. 90 min · €90."},
            {"n": "Escapada Provenzal Detox", "img": "https://maive.es/wp-content/uploads/2025/01/ritual-escapada-provenzal-lanzarote-maive.png",
             "desc": "Ritual iluminador con ingredientes de la Provenza francesa. Exfoliación y masaje que purifican, iluminan y desintoxican la piel dejándola radiante y suave. 90 min · €90."},
        ],
    },
]

EQUIPO = [
    {
        "nombre": "Dra. Naida Rodríguez",
        "rol": "Directora Médica · Médico Estético",
        "img": "https://maive.es/wp-content/uploads/2025/03/clinica-estetica-lanzarote-maive-Naida-768x1092.jpg",
        "especialidades": ["Medicina Estética", "Rejuvenecimiento Facial", "Tratamientos Inyectables", "Terapias Regenerativas"],
        "bio": """Fundadora y Directora Médica de Maive Centro Médico Estético. Especialista en medicina estética con amplia formación en rejuvenecimiento facial, tratamientos inyectables avanzados y terapias bioestimuladoras.

Lidera el equipo con una visión centrada en la naturalidad y el bienestar integral del paciente. Su filosofía se basa en realzar la belleza de cada persona respetando sus rasgos y personalidad únicos.

Con más de una década de experiencia en medicina estética, Naida es referente en Lanzarote por su rigor médico y su capacidad para diseñar tratamientos completamente personalizados.""",
    },
    {
        "nombre": "Dr. Manuel Fuciños",
        "rol": "Médico Estético",
        "img": "https://maive.es/wp-content/uploads/2026/05/Sin-titulo-1366-x-2048-px-8-683x1024.png",
        "especialidades": ["Medicina Estética", "Neuromoduladores", "Ácido Hialurónico", "Bioestimuladores"],
        "bio": """Médico estético especializado en técnicas de rejuvenecimiento facial y corporal. Experto en neuromoduladores (bótox), ácido hialurónico y los últimos protocolos de bioestimulación.

Combina rigor médico con sensibilidad artística para conseguir resultados naturales que armonizan con los rasgos de cada paciente. Su enfoque minimalista e individualizado garantiza una evolución progresiva y elegante.

Formación continuada en congresos nacionales e internacionales de medicina estética.""",
    },
    {
        "nombre": "Dr. Aaron Zapata",
        "rol": "Oftalmólogo · Especialista en Blefaroplastia",
        "img": "https://maive.es/wp-content/uploads/2024/05/oftalmologo-aaron--e1715073790661.jpeg",
        "especialidades": ["Oftalmología", "Blefaroplastia", "Cirugía Párpados", "Cirugía Facial"],
        "bio": """Oftalmólogo especializado en cirugía estética y funcional de párpados (blefaroplastia). Su doble formación — médica y quirúrgica — le permite abordar tanto la mejora estética como la funcionalidad visual con máxima precisión.

Referente en Lanzarote para la corrección de párpados caídos (ptosis), bolsas bajo los ojos y el exceso de piel que interfiere en la visión. Cada intervención es planificada con detalle para garantizar resultados duraderos y de aspecto natural.

Formado en centros de excelencia oftalmológica, aúna técnica quirúrgica avanzada con una visión artística del rejuvenecimiento facial.""",
    },
    {
        "nombre": "Dra. Iona Barrera",
        "rol": "Médica Estética",
        "img": "https://maive.es/wp-content/uploads/2026/05/Sin-titulo-1366-x-2048-px-3-683x1024.png",
        "especialidades": ["Medicina Estética", "Tratamientos Faciales", "Mesoterapia", "Antiaging"],
        "bio": """Médica estética con enfoque integral en el cuidado de la piel y el bienestar. Especialista en tratamientos faciales avanzados, mesoterapia, protocolos de hidratación profunda y tratamientos antiaging.

Su vocación por la medicina estética se traduce en una atención cercana y detallada que pone al paciente siempre en el centro. Trabaja con los protocolos más actualizados para proporcionar resultados visibles y duraderos.

Comprometida con la formación continua y la excelencia en cada procedimiento.""",
    },
    {
        "nombre": "Rocío Guzmán",
        "rol": "Técnico Superior en Estética",
        "img": "https://maive.es/wp-content/uploads/2026/05/b315a65e-cf81-449e-8b08-1ac10d7a042c-725x1024.png",
        "especialidades": ["LPG Endermologie", "Indiba", "Embody Esculpt", "Tratamientos Corporales"],
        "bio": """Técnico superior en estética especializada en aparatología avanzada. Experta en LPG Endermologie, Indiba y Embody Esculpt, acompaña a cada cliente con dedicación y profesionalidad en su proceso de mejora corporal y facial.

Su formación técnica combinada con una atención personalizada garantiza la máxima eficacia y comodidad en cada sesión. Apasionada por el bienestar y la estética, su objetivo es que cada cliente se sienta y se vea en su mejor versión.""",
    },
    {
        "nombre": "Dahiana Montoya",
        "rol": "Técnico en Estética",
        "img": "https://maive.es/wp-content/uploads/2026/05/Sin-titulo-1366-x-2048-px-7-683x1024.png",
        "especialidades": ["Tratamientos Faciales", "Tratamientos Corporales", "Higiene Facial", "Masajes"],
        "bio": """Técnico en estética y belleza con amplia experiencia en tratamientos faciales y corporales. Su atención meticulosa y pasión genuina por el sector se traducen en sesiones donde el cliente se siente cuidado y escuchado desde el primer momento.

Especializada en tratamientos de higiene facial, masajes terapéuticos y protocolos de cuidado corporal. Su trato cercano y profesional hace que cada visita a Maive sea una experiencia memorable.""",
    },
    {
        "nombre": "Cristina Sánchez",
        "rol": "Nutricionista Clínica",
        "img": "https://maive.es/wp-content/uploads/2024/06/nutricionista-lanzarote-maive-cristina-scaled.jpg",
        "especialidades": ["Nutrición Deportiva", "Pérdida de Peso", "Nutrición Clínica", "Educación Nutricional"],
        "bio": """Graduada en Nutrición y Dietética con Máster en Nutrición Clínica. Su misión es ayudar a las personas a mejorar su alimentación a través de un cambio de hábitos real y sostenible, adaptándose a la actividad física, patologías y gustos de cada paciente.

La primera consulta incluye valoración de hábitos diarios, historia médica y dietética, planificación del entrenamiento y definición de objetivos personalizados.

**Especialidades:** Nutrición deportiva · Pérdida de peso y educación nutricional · Nutrición clínica (cardiovascular, digestiva, diabetes) · Planificación dietética personalizada.""",
    },
]

SUGGESTIONS = [
    "¿Qué es el HydraFacial?",
    "¿Cuánto dura el bótox?",
    "Quiero reservar una cita",
    "¿Cuáles son los horarios?",
]

SYSTEM_PROMPT = """Eres el asistente virtual de Maive Centro Médico Estético, una clínica premium ubicada en Arrecife, Lanzarote. Número de registro sanitario: SCS/7776.

IDENTIDAD Y TONO:
- Nombre: Asistente virtual de Maive
- Tono: profesional, cálido, cercano y empático. Usa siempre "tú" para dirigirte al cliente.
- Responde de forma clara, concisa y elegante. No uses lenguaje técnico innecesario.
- Siempre prioriza la experiencia del cliente y su bienestar.
- Tagline de la clínica: "La salud de tu belleza en buenas manos"

TRATAMIENTOS FACIALES:
- Full Face (rejuvenecimiento facial integral)
- HydraFacial
- Neuromoduladores (bótox / Dysport) — toxina botulínica para arrugas
- Hilos Tensores — lifting no quirúrgico
- Harmonyca — lifting sin cirugía, biestimulación
- Indiba Facial — radiofrecuencia profunda facial
- LPG Endermologie Facial
- Peeling Facial
- Mesoterapia Facial
- Exosomas Faciales
- Bioestimulación (hidroxiapatita cálcica)
- Inductores de Colágeno
- SkinPen (microneedling)
- Carbon Peel Láser
- Liftera (HIFU)
- Rinomodelación sin cirugía
- Terapia Fotodinámica
- Kinesiolifting
- Tratamiento acné
- Tratamiento manchas / Luz Pulsada IPL
- ZO Skin Health
- Bioestimulación capilar
- Higiene Facial · Masajes Faciales · Exfoliación

TRATAMIENTOS CORPORALES:
- Indiba Corporal — radiofrecuencia profunda reductora y reafirmante
- Embody Esculpt (EMS) — escultura muscular y eliminación de grasa
- Depilación Láser (diodo)
- LPG Endermologie Corporal
- Maderoterapia
- Presoterapia
- Ondas de Choque
- Mesoterapia Corporal
- Carboxiterapia Corporal
- Body Contouring
- Láser CO2 · Láser borrar tatuajes · Esclerolaser
- Masajes Corporales
- Sueroterapia Antienvejecimiento

CIRUGÍA ESTÉTICA (Dr. Aaron Zapata & Dr. Manuel Fuciños):
- Blefaroplastia (cirugía de párpados superiores e inferiores)
- Lifting Facial · Rinoplastia · Otoplastia
- Liposucción de cuello / general · Nanofat
- Mastoplastia de aumento / reducción / Mastopexia
- Abdominoplastia · Gluteoplastia · Implante Pectoral · Ginecomastia

GINECOESTÉTICA:
- Láser Vaginal · Radiofrecuencia Genital · Bioregeneración Genital
- Exosomas Genitales · Antiaging Íntimo · Blanqueamiento Genital

RITUALES BIENESTAR — Yonka (€90 cada uno):
- Viaje a la Polinesia (relajante)
- Delicias Corsas Vitalité (energizante)
- Un Paseo por el Bosque (desconexión)
- Escapada Provenzal Detox (iluminador)
- También: Osteopatía · Hormonas Bioidenticas · Tratamiento Menopausia

NUTRICIÓN (Cristina Sánchez — Nutricionista, Máster en Nutrición Clínica):
- Nutrición deportiva
- Pérdida de peso y educación nutricional
- Nutrición clínica: cardiovascular, digestiva, diabetes

EQUIPO MÉDICO:
- Dra. Naida Rodríguez — Directora médica y médico estético
- Dr. Manuel Fuciños — Médico estético
- Dr. Aaron Zapata — Oftalmólogo, especialista en blefaroplastia
- Dra. Iona Barrera — Médica estética
- Rocío Guzmán — Técnico superior en estética
- Dahiana Montoya — Técnico en estética
- Cristina Sánchez — Nutricionista clínica

INFORMACIÓN DE CONTACTO:
- Teléfono / WhatsApp principal: 638 128 452
- Teléfono secundario: 828 902 864
- Email: info@maive.es
- Dirección: C/ Parranda de Los Buches 16-18, Local 2, 35500 Arrecife, Lanzarote
- Web: maive.es
- Instagram: @maivelanzarote · Facebook: MaiveLanzarote · TikTok: @maivelanzarote

HORARIO:
- Lunes a Viernes: 9:00 a 19:00
- Sábados: 10:00 a 14:00 (solo con cita previa)
- Domingos y festivos: cerrado

PREGUNTAS FRECUENTES:

¿Es doloroso el bótox?
El bótox se aplica con agujas muy finas y la molestia es mínima, similar a un pequeño pinchazo. La mayoría de pacientes lo describen como muy tolerable. No requiere anestesia en la mayoría de los casos.

¿Cuánto dura el efecto del ácido hialurónico?
Depende de la zona y el producto: labios 6-12 meses, surcos nasogenianos 12-18 meses, hidratación intradérmica 6-9 meses.

¿Qué es la blefaroplastia?
Intervención quirúrgica que corrige el exceso de piel y la caída de párpados superiores y/o inferiores. Mejora estética y funcionalidad visual. Realizada por el Dr. Aaron Zapata, oftalmólogo especialista.

¿Cuántas sesiones necesito?
Depende del tratamiento: LPG Endermologie 10-15 sesiones, Indiba 6-10 sesiones, tratamientos faciales pueden verse resultados desde la primera sesión.

¿Cuáles son los precios?
Los precios varían según el tratamiento y las necesidades específicas. Realizamos una valoración personalizada gratuita. Los rituales Yonka tienen un precio fijo de €90.

¿Qué es el Full Face?
Tratamiento integral de rejuvenecimiento facial que combina técnicas según las necesidades de cada paciente: ácido hialurónico, bioestimuladores, neuromoduladores y más, para un resultado natural y armonioso.

¿Qué es el HydraFacial?
Tratamiento multiacción que limpia, exfolia, extrae impurezas e hidrata la piel en profundidad mediante un sistema de vortex. Resultados visibles desde la primera sesión, sin tiempo de recuperación.

FLUJO DE RESERVA DE CITA:
Cuando un cliente quiera reservar una cita, recoge la información en este orden exacto, una pregunta a la vez:
1. Nombre completo
2. Tratamiento de interés
3. Fecha y hora preferida
4. Número de teléfono de contacto
5. Pregunta: "¿Prefieres recibir la confirmación y los recordatorios por WhatsApp o por email?"
   - Si elige WhatsApp: ya tienes el teléfono, no hace falta más datos.
   - Si elige email: pregunta su dirección de email.

Una vez tengas todos los datos, usa el mensaje correspondiente:

Si eligió WhatsApp (sustituye [nombre] y [teléfono]):
"¡Perfecto, [nombre]! 🎉 Hemos recibido tu solicitud de cita. Te enviaremos la confirmación por WhatsApp al [teléfono] y recibirás un recordatorio automático 24h antes y otro 2h antes para que no se te olvide. ¡Hasta pronto! ✨"

Si eligió email (sustituye [nombre] y [email]):
"¡Perfecto, [nombre]! 🎉 Hemos recibido tu solicitud de cita. Te enviaremos la confirmación a [email] y recibirás un recordatorio automático 24h antes y otro 2h antes para que no se te olvide. ¡Hasta pronto! ✨"

INSTRUCCIONES IMPORTANTES:
- Si el cliente pregunta por algo que no conoces con certeza, indícale que contacte directamente con la clínica.
- Para preguntas médicas específicas, recomienda siempre una consulta presencial.
- Nunca inventes precios exactos salvo los rituales Yonka (€90).
- Sé siempre positivo, empático y orientado a ayudar al cliente."""

WELCOME_MESSAGE = "¡Hola! Soy el asistente virtual de Maive ✨ ¿En qué puedo ayudarte hoy? Puedo informarte sobre nuestros tratamientos, resolver tus dudas o ayudarte a reservar tu cita."

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MAIVE — Asistente Virtual",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8F6F2; }
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] { background-color: #1A1A1A; border-right: none; }
    [data-testid="stSidebar"] * { color: #E8E0D4 !important; }
    [data-testid="stSidebar"] h3 {
        color: #C9A96E !important;
        font-size: 0.68rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        font-weight: 600;
        margin: 1.2rem 0 0.5rem 0;
        padding-top: 0.8rem;
        border-top: 1px solid #2A2A2A;
    }
    [data-testid="stSidebar"] h3:first-of-type { border-top: none; margin-top: 0.2rem; }
    [data-testid="stSidebarUserContent"] { padding-top: 1.2rem; }

    .sidebar-logo { display:flex; justify-content:center; margin-bottom:1rem; }
    .sidebar-logo img { max-width:130px; filter: brightness(0) invert(1); }

    .sidebar-contact {
        background: #222;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 0.75rem;
        line-height: 1.9;
    }
    .sidebar-contact a { color: #C9A96E !important; text-decoration: none; }

    .trat-card {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.3rem 0;
        font-size: 0.76rem;
        border-bottom: 1px solid #252525;
    }
    .trat-card img {
        width: 34px; height: 34px;
        object-fit: cover; border-radius: 6px; flex-shrink: 0;
    }
    .trat-dot {
        width: 34px; height: 34px;
        background: #2A2A2A; border-radius: 6px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center; font-size: 0.9rem;
    }

    /* Team cards */
    .team-card {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.4rem 0 0.2rem 0;
    }
    .team-card img {
        width: 46px; height: 46px;
        object-fit: cover; object-position: top;
        border-radius: 50%; flex-shrink: 0;
        border: 2px solid #C9A96E;
    }
    .team-avatar-circle {
        width: 46px; height: 46px;
        background: linear-gradient(135deg, #C9A96E, #8B6914);
        border-radius: 50%; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.85rem; font-weight: 700; color: white !important;
    }
    .team-info .t-name { font-size: 0.8rem; font-weight: 600; color: #E8E0D4 !important; }
    .team-info .t-rol { font-size: 0.68rem; color: #888 !important; }

    /* Botones sidebar — "Ver ficha" y "ℹ" */
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid #333 !important;
        color: #C9A96E !important;
        font-size: 0.68rem !important;
        padding: 0.15rem 0.6rem !important;
        border-radius: 20px !important;
        margin-bottom: 0.3rem !important;
        width: auto !important;
        letter-spacing: 0.05em;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        border-color: #C9A96E !important;
        background: #221f1a !important;
    }
    /* Botón ℹ — pequeño, cuadrado, alineado al centro vertical */
    [data-testid="stSidebar"] .stButton > button[title] {
        border-radius: 50% !important;
        padding: 0 !important;
        width: 20px !important;
        height: 20px !important;
        min-width: 20px !important;
        font-size: 0.7rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-top: 6px !important;
    }

    /* ── Dialog fondo ── */
    [data-testid="stModal"] > div, div[role="dialog"] {
        background-color: #FAFAF8 !important;
    }

    /* Botón primario (Reservar) */
    [data-testid="stModal"] [data-testid="stBaseButton-primary"],
    div[role="dialog"] [data-testid="stBaseButton-primary"] {
        background-color: #1A1A1A !important;
        border: none !important;
        border-radius: 10px !important;
    }
    [data-testid="stModal"] [data-testid="stBaseButton-primary"]:hover,
    div[role="dialog"] [data-testid="stBaseButton-primary"]:hover {
        background-color: #C9A96E !important;
    }
    [data-testid="stModal"] [data-testid="stBaseButton-primary"] p,
    [data-testid="stModal"] [data-testid="stBaseButton-primary"] span,
    div[role="dialog"] [data-testid="stBaseButton-primary"] p,
    div[role="dialog"] [data-testid="stBaseButton-primary"] span {
        color: #FFFFFF !important;
    }

    /* Botón X nativo — aria-label es más estable que data-testid */
    button[aria-label="Close"] {
        background-color: #EDEAE5 !important;
        border: 1px solid #B0A898 !important;
        border-radius: 5px !important;
        width: 22px !important;
        height: 22px !important;
        min-width: 22px !important;
        min-height: 22px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    button[aria-label="Close"]:hover {
        background-color: #C9A96E !important;
        border-color: #C9A96E !important;
    }
    button[aria-label="Close"] svg,
    button[aria-label="Close"] svg path {
        fill: #555555 !important;
        stroke: #555555 !important;
        color: #555555 !important;
        width: 10px !important;
        height: 10px !important;
    }
    button[aria-label="Close"]:hover svg,
    button[aria-label="Close"]:hover svg path {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }

    /* ── Dialog / Modal ── */
    [data-testid="stModal"],
    [data-testid="stModal"] > div,
    div[role="dialog"],
    div[role="dialog"] > div {
        background-color: #FAFAF8 !important;
        font-family: 'Inter', sans-serif !important;
    }
    div[role="dialog"] p,
    div[role="dialog"] span,
    div[role="dialog"] div,
    div[role="dialog"] li {
        color: #2A2A2A !important;
    }

    .bio-header { margin-bottom: 0.5rem; }
    .bio-name { font-size: 1.4rem !important; font-weight: 700 !important; color: #1A1A1A !important; margin: 0 !important; }
    .bio-rol { font-size: 0.8rem !important; color: #C9A96E !important; font-weight: 500 !important; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.8rem !important; }
    .bio-esp { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; }
    .bio-tag {
        background: #F0EDE8 !important; border-radius: 20px;
        padding: 0.2rem 0.7rem; font-size: 0.72rem !important; color: #555 !important;
    }
    .bio-text {
        font-size: 0.86rem !important;
        line-height: 1.7 !important;
        color: #444 !important;
        max-height: 140px;
        overflow-y: auto;
        padding-right: 4px;
    }

    /* ── Main chat area ── */
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; max-width: 780px; }

    .maive-header {
        text-align: center;
        padding: 0.4rem 0 1.4rem 0;
        border-bottom: 1px solid #EAE6E0;
        margin-bottom: 1.4rem;
    }
    .maive-header img { max-height: 68px; margin-bottom: 0.3rem; }
    .maive-subtitle {
        font-size: 0.74rem; font-weight: 400;
        letter-spacing: 0.14em; color: #999; text-transform: uppercase;
    }
    .maive-tagline { font-size: 0.78rem; color: #C9A96E; font-style: italic; margin-top: 0.15rem; }

    .suggestions-row {
        display: flex; flex-wrap: wrap; gap: 0.45rem;
        margin-bottom: 1.4rem; justify-content: center;
    }
    .chip {
        background: #fff; border: 1.5px solid #E0D8CE; border-radius: 20px;
        padding: 0.3rem 0.85rem; font-size: 0.76rem; color: #555;
    }

    .chat-bubble-assistant {
        background: #fff; border-left: 3px solid #C9A96E;
        border-radius: 0 12px 12px 0; padding: 0.9rem 1.1rem;
        margin: 0.35rem 0; font-size: 0.89rem; line-height: 1.65; color: #2A2A2A;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .chat-bubble-user {
        background: #1A1A1A; border-radius: 12px 12px 0 12px;
        padding: 0.9rem 1.1rem; margin: 0.35rem 0;
        font-size: 0.89rem; line-height: 1.65; color: #fff; text-align: right;
    }
    .chat-label-assistant {
        font-size: 0.67rem; font-weight: 600; letter-spacing: 0.1em;
        color: #C9A96E; text-transform: uppercase; margin-bottom: 0.12rem;
    }
    .chat-label-user {
        font-size: 0.67rem; font-weight: 600; letter-spacing: 0.1em;
        color: #888; text-transform: uppercase; margin-bottom: 0.12rem; text-align: right;
    }

    /* Chat input */
    [data-testid="stChatInput"] textarea {
        border: 1.5px solid #E0D8CE !important;
        border-radius: 12px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        background-color: #fff !important;
        color: #1A1A1A !important;
        caret-color: #1A1A1A !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border-color: #C9A96E !important;
        box-shadow: 0 0 0 2px rgba(201,169,110,0.15) !important;
        color: #1A1A1A !important;
    }
    [data-testid="stChatInput"] textarea::placeholder { color: #AAAAAA !important; }

    .info-footer {
        text-align: center; font-size: 0.71rem; color: #BBBBBB;
        margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #EAE6E0;
    }
</style>
""", unsafe_allow_html=True)

# ── Dialog modal (bio) ────────────────────────────────────────────────────────
@st.dialog("Sobre este tratamiento", width="large")
def mostrar_tratamiento(trat):
    col_close, _ = st.columns([1, 6])
    with col_close:
        if st.button("✕ cerrar", key="btn_cerrar_trat"):
            st.rerun()

    col_img, col_info = st.columns([1, 2], gap="large")
    with col_img:
        if trat["img"]:
            st.image(trat["img"], width=180)
    with col_info:
        st.markdown(f"""
        <p class="bio-name">{trat['n']}</p>
        <div class="bio-text" style="max-height:none;">{trat['desc']}</div>
        """, unsafe_allow_html=True)

    st.divider()
    if st.button("📅 Reservar este tratamiento", use_container_width=True, key="btn_reservar_trat", type="primary"):
        st.session_state.messages.append({
            "role": "user",
            "content": f"Quiero reservar una cita para {trat['n']}"
        })
        st.session_state.pending_response = True
        st.rerun()


@st.dialog("Ficha del Profesional", width="large")
def mostrar_bio(miembro):
    col_foto, col_info = st.columns([1, 2], gap="large")
    with col_foto:
        st.image(miembro["img"], width=180)
    with col_info:
        st.markdown(f"""
        <div class="bio-header">
            <p class="bio-name">{miembro['nombre']}</p>
            <p class="bio-rol">{miembro['rol']}</p>
        </div>
        <div class="bio-esp">
            {"".join(f'<span class="bio-tag">{e}</span>' for e in miembro['especialidades'])}
        </div>
        <div class="bio-text">{miembro['bio'].replace(chr(10), '<br>')}</div>
        """, unsafe_allow_html=True)
    st.divider()
    if st.button("📅 Reservar cita con este profesional", use_container_width=True, key="btn_reservar", type="primary"):
        st.session_state.messages.append({
            "role": "user",
            "content": f"Quiero reservar una cita con {miembro['nombre']}"
        })
        st.session_state.pending_response = True
        st.rerun()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "open_bio" not in st.session_state:
    st.session_state.open_bio = None
if "open_trat" not in st.session_state:
    st.session_state.open_trat = None
if "pending_response" not in st.session_state:
    st.session_state.pending_response = False

# Abrir modales si hay uno pendiente
if st.session_state.open_bio is not None:
    mostrar_bio(st.session_state.open_bio)
    st.session_state.open_bio = None
if st.session_state.open_trat is not None:
    mostrar_tratamiento(st.session_state.open_trat)
    st.session_state.open_trat = None

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f'<div class="sidebar-logo"><img src="{LOGO_URL}" alt="Maive"></div>', unsafe_allow_html=True)

    st.markdown("### Contacto")
    st.markdown("""
    <div class="sidebar-contact">
        📍 C/ Parranda de Los Buches 16-18, Local 2<br>
        35500 Arrecife, Lanzarote<br>
        📞 <a href="tel:+34638128452">638 128 452</a> &nbsp;|&nbsp; <a href="tel:+34828902864">828 902 864</a><br>
        ✉️ <a href="mailto:info@maive.es">info@maive.es</a><br>
        🕐 L–V 9:00–19:00 · S 10:00–14:00
    </div>
    """, unsafe_allow_html=True)

    # Tratamientos
    for categoria in TRATAMIENTOS_SIDEBAR:
        st.markdown(f"### {categoria['cat']}")
        for t in categoria["items"]:
            col_card, col_btn = st.columns([5, 1])
            with col_card:
                if t["img"]:
                    st.markdown(f"""
                    <div class="trat-card">
                        <img src="{t['img']}" alt="{t['n']}">
                        <span>{t['n']}</span>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="trat-card">
                        <div class="trat-dot">✦</div>
                        <span>{t['n']}</span>
                    </div>""", unsafe_allow_html=True)
            with col_btn:
                if st.button("ℹ", key=f"trat_{t['n']}", help=f"Ver más sobre {t['n']}"):
                    st.session_state.open_trat = t
                    st.rerun()

    # Equipo
    st.markdown("### ✦ Equipo Médico")
    for p in EQUIPO:
        initials = "".join(w[0] for w in p["nombre"].replace("Dra.", "").replace("Dr.", "").strip().split()[:2])
        st.markdown(f"""
        <div class="team-card">
            <img src="{p['img']}" alt="{p['nombre']}">
            <div class="team-info">
                <div class="t-name">{p['nombre']}</div>
                <div class="t-rol">{p['rol']}</div>
            </div>
        </div>""", unsafe_allow_html=True)

        if st.button(f"Ver ficha →", key=f"bio_{p['nombre']}"):
            st.session_state.open_bio = p
            st.rerun()

    st.markdown("""
    <div style="text-align:center;font-size:0.67rem;color:#444;padding:0.8rem 0;">
        Reg. Sanitario SCS/7776<br>
        <a href="https://maive.es" target="_blank" style="color:#C9A96E;">maive.es</a> ·
        <a href="https://instagram.com/maivelanzarote" target="_blank" style="color:#C9A96E;">@maivelanzarote</a>
    </div>""", unsafe_allow_html=True)

# ── Main chat area ────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="maive-header">
    <img src="{LOGO_URL}" alt="Maive Centro Médico Estético">
    <div class="maive-subtitle">Centro Médico Estético · Arrecife, Lanzarote</div>
    <div class="maive-tagline">La salud de tu belleza en buenas manos</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="suggestions-row">' +
    "".join(f'<span class="chip">{s}</span>' for s in SUGGESTIONS) +
    '</div>',
    unsafe_allow_html=True
)

# ── Historial ─────────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown('<div class="chat-label-assistant">Maive</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bubble-assistant">{WELCOME_MESSAGE}</div>', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.markdown('<div class="chat-label-assistant">Maive</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble-assistant">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="chat-label-user">Tú</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Escribe tu consulta...")

# Determinar qué mensaje procesar: del chat o del botón de reserva del diálogo
msg_to_process = None

if user_input and user_input.strip():
    msg_to_process = user_input.strip()
    st.session_state.messages.append({"role": "user", "content": msg_to_process})
    st.markdown('<div class="chat-label-user">Tú</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bubble-user">{msg_to_process}</div>', unsafe_allow_html=True)
elif st.session_state.pending_response and st.session_state.messages:
    st.session_state.pending_response = False
    msg_to_process = st.session_state.messages[-1]["content"]

if msg_to_process:
    api_key = get_secret("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("API key no configurada.")
        st.stop()

    client = anthropic.Anthropic(api_key=api_key)
    st.markdown('<div class="chat-label-assistant">Maive</div>', unsafe_allow_html=True)
    placeholder = st.empty()
    full_response = ""

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=st.session_state.messages,
    ) as stream:
        for chunk in stream.text_stream:
            full_response += chunk
            placeholder.markdown(
                f'<div class="chat-bubble-assistant">{full_response}▌</div>',
                unsafe_allow_html=True
            )

    placeholder.markdown(
        f'<div class="chat-bubble-assistant">{full_response}</div>',
        unsafe_allow_html=True
    )
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="info-footer">
    Maive Centro Médico Estético · C/ Parranda de Los Buches 16-18, Local 2, Arrecife · 638 128 452 · maive.es
</div>
""", unsafe_allow_html=True)
