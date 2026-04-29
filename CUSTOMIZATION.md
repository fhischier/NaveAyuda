# 🎨 Guía de Personalización - Fácil y Sencillo

## 📋 Índice
1. [Cambiar Colores](#cambiar-colores)
2. [Modificar Preguntas](#modificar-preguntas)
3. [Agregar Más Preguntas](#agregar-más-preguntas)

---

## 🎨 Cambiar Colores

### 📍 Dónde editar: `src/config/settings.py`

Busca esta sección y cambia los códigos de color:

```python
class Theme:
    """Color scheme and styling constants."""
    BACKGROUND = "#1a1a2e"        # Color de fondo (oscuro)
    SURFACE = "#16213e"          # Color de tarjetas
    PRIMARY = "#0f4c75"          # Color principal (botones)
    PRIMARY_HOVER = "#3282b8"    # Color al pasar mouse
    PRIMARY_LIGHT = "#bbe1fa"    # Color claro
    SUCCESS = "#22c55e"          # Verde para respuestas correctas
    ERROR = "#ef4444"            # Rojo para respuestas incorrectas
    TEXT = "#ffffff"             # Color del texto
    TEXT_MUTED = "#94a3b8"       # Color de texto secundario
```

### 🎨 Colores Populares para Copiar y Pegar:

**Tema Azul (actual):**
```python
BACKGROUND = "#1a1a2e"
PRIMARY = "#0f4c75"
SUCCESS = "#22c55e"
ERROR = "#ef4444"
```

**Tema Morado:**
```python
BACKGROUND = "#2d1b69"
PRIMARY = "#6b46c1"
SUCCESS = "#10b981"
ERROR = "#ef4444"
```

**Tema Verde:**
```python
BACKGROUND = "#14532d"
PRIMARY = "#16a34a"
SUCCESS = "#22c55e"
ERROR = "#ef4444"
```

**Tema Rojo:**
```python
BACKGROUND = "#7f1d1d"
PRIMARY = "#dc2626"
SUCCESS = "#16a34a"
ERROR = "#f59e0b"
```

---

## ❓ Modificar Preguntas

### 📍 Dónde editar: `src/data/questions.py`

Busca esta función y modifica las preguntas:

```python
def create_sample_survey() -> Survey:
    """Create a sample survey with questions."""
    questions = [
        Question(
            text="¿QUIÉN ES EL DUEÑO DE CLAMERS?",           # ← CAMBIA LA PREGUNTA AQUÍ
            options=["German", "Ioio", "Nari"],               # ← CAMBIA LAS OPCIONES AQUÍ
            correct_index=0                                   # ← ÍNDICE DE LA RESPUESTA CORRECTA (0=primera, 1=segunda, 2=tercera)
        ),
        Question(
            text="¿CUÁNTO PAGA CLAMERS?",                    # ← SEGUNDA PREGUNTA
            options=["Bien", "Poco", "Mucho"],
            correct_index=1                                   # ← La correcta es "Poco" (índice 1)
        ),
        Question(
            text="¿QUIÉN ES EL MÁS GORDO?",                  # ← TERCERA PREGUNTA
            options=["German", "Ioio", "Nari"],
            correct_index=0                                   # ← La correcta es "German" (índice 0)
        )
    ]
    
    return Survey(questions)
```

### 🔥 Ejemplo Práctico:

**Si quieres cambiar la primera pregunta:**

```python
# ANTES:
Question(
    text="¿QUIÉN ES EL DUEÑO DE CLAMERS?",
    options=["German", "Ioio", "Nari"],
    correct_index=0
)

# DESPUÉS (ejemplo con pregunta de programación):
Question(
    text="¿QUÉ LENGUAJE USAMOS EN ESTE PROYECTO?",
    options=["Python", "JavaScript", "Java"],
    correct_index=0  # Python es la correcta
)
```

---

## ➕ Agregar Más Preguntas

### 📍 Dónde editar: `src/data/questions.py`

Simplemente copia y pega más preguntas en la lista:

```python
def create_sample_survey() -> Survey:
    """Create a sample survey with questions."""
    questions = [
        # Pregunta 1
        Question(
            text="¿QUIÉN ES EL DUEÑO DE CLAMERS?",
            options=["German", "Ioio", "Nari"],
            correct_index=0
        ),
        
        # Pregunta 2
        Question(
            text="¿CUÁNTO PAGA CLAMERS?",
            options=["Bien", "Poco", "Mucho"],
            correct_index=1
        ),
        
        # Pregunta 3
        Question(
            text="¿QUIÉN ES EL MÁS GORDO?",
            options=["German", "Ioio", "Nari"],
            correct_index=0
        ),
        
        # 🆕 PREGUNTA 4 (AGREGA ESTA):
        Question(
            text="¿CUÁL ES EL MEJOR LENGUAJE?",
            options=["Python", "JavaScript", "C++"],
            correct_index=0
        ),
        
        # 🆕 PREGUNTA 5 (Y ESTA):
        Question(
            text="¿QUÉ FRAMEWORK USAMOS?",
            options=["PyQt", "Tkinter", "PySide6"],
            correct_index=2
        ),
        
        # 🆕 PREGUNTA 6 (Y CUANTAS QUIERAS):
        Question(
            text="¿QUÉ COLOR TE GUSTA MÁS?",
            options=["Azul", "Rojo", "Verde"],
            correct_index=0
        )
    ]
    
    return Survey(questions)
```

---

## 🔥 Tips Rápidos

### ✨ Importante Recordar:
- **`correct_index=0`** = Primera opción es correcta
- **`correct_index=1`** = Segunda opción es correcta  
- **`correct_index=2`** = Tercera opción es correcta
- **Puedes agregar 2, 3, 4 o más opciones** si quieres

### ⚡ Atajos:
1. **Copia y pega** una pregunta existente
2. **Cambia solo el texto** y las opciones
3. **Ajusta el `correct_index`**
4. **Guarda el archivo** y ejecuta `python3 main.py`

### 🎯 Para Preguntas con 4 Opciones:
```python
Question(
    text="¿CUÁLES SON LOS COLORES PRIMARIOS?",
    options=["Rojo", "Verde", "Azul", "Amarillo"],
    correct_index=3  # Amarillo sería la correcta
)
```

---

## 🚀 Cómo Probar los Cambios

1. **Edita el archivo** (`src/config/settings.py` o `src/data/questions.py`)
2. **Guarda los cambios** (Ctrl+S)
3. **Cierra la aplicación** si está abierta
4. **Ejecuta nuevamente**: `python3 main.py`
5. **¡Listo!** Verás tus cambios inmediatamente

---

## 🆘 Problemas Comunes

**❌ "No se guardan los cambios":**
- Asegúrate de guardar el archivo con Ctrl+S
- Cierra y vuelve a abrir la aplicación

**❌ "La respuesta correcta no funciona":**
- Revisa que el `correct_index` coincida con la opción correcta
- Recuerda: 0=primera, 1=segunda, 2=tercera

**❌ "Los colores no cambian":**
- Verifica que los códigos de color tengan # al inicio
- Reinicia la aplicación después de cambiar los colores

---

