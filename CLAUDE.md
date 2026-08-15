# maive-chatbot — CONGELADO

Chatbot original de **Maive Centro Médico Estético**: un `app.py` de ~777 líneas
en Streamlit con Claude, con el catálogo de tratamientos escrito en el propio fichero.

**Estado: congelado. Último commit 31/05/2026.**
**Sucesor: `maive-cumplimiento`** — mismo cliente, con dashboard, scheduler,
persistencia con Alembic y toda la capa de cumplimiento RGPD.

## No trabajes aquí

Si te han pedido algo de Maive, el repo es `../maive-cumplimiento`. Éste se conserva
como respaldo del chatbot inicial.

Ojo con la confusión de nombres: el `README.md` de `maive-cumplimiento` todavía
describe su árbol bajo el nombre "maive-chatbot/". Eso es herencia, no una referencia
a este repositorio.

## Si aun así hay que tocarlo

```bash
pip install -r requirements.txt   # streamlit, anthropic, python-dotenv
streamlit run app.py
```

Sin tests, sin base de datos: el estado vivía en la sesión de Streamlit.

## Lo único que sigue siendo útil

El bloque `TRATAMIENTOS_SIDEBAR` de `app.py` tiene el catálogo de tratamientos de la
clínica redactado y categorizado. Si hace falta ese contenido, sale de aquí.
