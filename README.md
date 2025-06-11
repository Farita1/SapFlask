# 🧑‍💼 SAP - Sistema de Administración de Personas

Este es un sistema básico de administración de personas (SAP) desarrollado con **Flask**, que permite realizar operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar) usando una base de datos **PostgreSQL**.

## 🚀 Tecnologías usadas

- Python 🐍
- Flask 🌶️
- SQLAlchemy 🧬
- PostgreSQL 🐘
- Flask-WTF (formularios) 📄
- Flask-Migrate (migraciones) 🛠️
- HTML (para las vistas)

## 📸 Capturas
INDEX:

![image](https://github.com/user-attachments/assets/f113df95-1fb0-430e-b128-2118ee44ba4f)

AGREGAR:

![image](https://github.com/user-attachments/assets/9022fdeb-1482-4e4f-8a7a-12cf148fee5a)

EDITAR:

![image](https://github.com/user-attachments/assets/576ce7f6-9eb2-4f54-b386-f824742e42c3)


## 🛠️ Funcionalidades

✅ Listar personas registradas  
✅ Ver detalle de una persona  
✅ Agregar una nueva persona  
✅ Editar los datos de una persona  
✅ Eliminar persona  
✅ Validaciones de formulario con Flask-WTF  
✅ Migraciones con Flask-Migrate  

## ⚙️ Requisitos

- Python 3.10+
- PostgreSQL instalado
- pip

## 🧰 Instalación y ejecución

1. **Clonar el repositorio**
2. **Crear el entorno virtual**
Ejecutar comandos en la terminal:
python -m venv venv
cd .\entorno\Scripts\
.\Activate.ps1
3. Instalar las dependencias
pip install -r requirements.txt
4. Configurar base de datos:
USER_DB = 'tu_usuario'
PASS_DB = 'tu_password'
URL_DB = 'localhost'
NAME_DB = 'nombre_de_tu_base_de_datos'
5. Inicializar la base de datos:
flask db init
flask db migrate -m "Inicial"
flask db upgrade
6. Ejecutar: flask run

Hecho Por: Farita1
