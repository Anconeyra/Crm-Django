# CRM de Clientes Django

Este es un sistema básico de Gestión de Relaciones con Clientes (CRM) desarrollado con Django, diseñado para gestionar clientes y sus interacciones.
![image](https://github.com/user-attachments/assets/ac279f5f-b688-4b56-b162-5164ac34afc5)
![image](https://github.com/user-attachments/assets/d6e5abfa-cc58-40bf-8f7a-475dcb045d14)
![image](https://github.com/user-attachments/assets/45be95ff-e0ba-458c-b11f-dd3c43df1d1c)
![image](https://github.com/user-attachments/assets/94ae6a4e-8218-4a97-a728-c76bc3070e51)
![image](https://github.com/user-attachments/assets/c622a099-522e-46a8-9366-aae1b4975810)
![image](https://github.com/user-attachments/assets/1bea871d-6714-41f1-88c4-85311e0a7694)
![image](https://github.com/user-attachments/assets/0375f1c7-7b5b-42e6-836c-a155d30d997b)



## Tabla de Contenidos

1.  [Requisitos Previos](#1-requisitos-previos)
2.  [Configuración del Entorno](#2-configuración-del-entorno)
3.  [Configuración de la Base de Datos (MySQL)](#3-configuración-de-la-base-de-datos-mysql)
4.  [Instalación de Dependencias](#4-instalación-de-dependencias)
5.  [Migraciones de Base de Datos](#5-migraciones-de-base-de-datos)
6.  [Creación de Superusuario](#6-creación-de-superusuario)
7.  [Poblar Datos de Ejemplo](#7-poblar-datos-de-ejemplo)
8.  [Ejecutar el Proyecto](#8-ejecutar-el-proyecto)
9.  [Acceso a Vistas](#9-acceso-a-vistas)
10. [Características Principales](#10-características-principales)

---

## 1. Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

* **Python 3.10** (o una versión compatible con Django 5.0.7, se recomienda 3.10+).
* **pip** (el gestor de paquetes de Python, usualmente viene con Python).
* **Git** (para clonar el repositorio).
* **MySQL Server** (si planeas usar MySQL como base de datos) o **SQLite** (Django usa SQLite por defecto, no requiere instalación adicional de servidor).

---

## 2. Configuración del Entorno

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto.

1.  **Clonar el Repositorio:**

    ```bash
    git clone [https://github.com/Anconeyra/Crm.git](https://github.com/Anconeyra/Crm.git)
    cd Crm # O el nombre de tu carpeta de proyecto, por ejemplo prueba_tecnica
    ```

2.  **Crear y Activar un Entorno Virtual:**

    ```bash
    python -m venv venv
    ```

    * **En Windows (CMD/PowerShell):**

        ```bash
        .\venv\Scripts\activate
        ```

    * **En Linux/macOS (Bash/Zsh):**

        ```bash
        source venv/bin/activate
        ```

    Una vez activado, verás `(venv)` al principio de tu línea de comandos.

---

## 3. Configuración de la Base de Datos (MySQL)

Este proyecto está configurado por defecto para usar SQLite, pero puedes cambiarlo a MySQL.

### Opción A: Usar SQLite (Recomendado para desarrollo rápido)

Si no deseas configurar MySQL, el proyecto usará la base de datos SQLite por defecto. No necesitas hacer nada aquí.

### Opción B: Configurar MySQL

1.  **Instalar el conector MySQL para Python:**

    ```bash
    pip install mysqlclient
    ```

2.  **Crear una base de datos en MySQL:**
    Accede a tu servidor MySQL (por ejemplo, vía phpMyAdmin, MySQL Workbench o la línea de comandos) y crea una nueva base de datos.

    ```sql
    CREATE DATABASE crm_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'crm_user'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON crm_db.* TO 'crm_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

    *Reemplaza `crm_db`, `crm_user` y `your_password` con tus propios valores.*

3.  **Configurar `settings.py`:**
    Abre `prueba_tecnica/settings.py` y modifica la sección `DATABASES` para que apunte a tu base de datos MySQL:

    ```python
    # prueba_tecnica/settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'crm_db',
            'USER': 'crm_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
    ```

---

## 4. Instalación de Dependencias

Con tu entorno virtual activado, instala todas las dependencias del proyecto.

```bash
pip install Django==5.0.7 django-jazzmin
```
---

## 5. Migraciones de Base de Datos

Aplica las migraciones para crear las tablas necesarias en tu base de datos.

```bash
python manage.py makemigrations generacion
python manage.py migrate
```
## 6. Creación de Superusuario

Crea un superusuario para acceder al panel de administración de Django.

```bash
python manage.py createsuperuser
```
---
7. Poblar Datos
   Antes de ello tenemos que lanzar los datos
   ## Instalar la dependencia Faker

Asegúrate de tener tu entorno virtual activado, luego instala la librería Faker:

```bash
pip install Faker
```
## Ejecutar el comando de generación de datos

Una vez que hayas configurado tu base de datos y ejecutado las migraciones (`python manage.py migrate`), puedes poblar la base de datos con el siguiente comando:

```bash
python manage.py generate_fake_data
```
Puedes añadir Compañías, Representantes de Ventas, Clientes e Interacciones manualmente
a través del panel de administración de Django una vez que el servidor esté funcionando.

---

## 8. Ejecutar el Proyecto

Inicia el servidor de desarrollo de Django.

```bash
python manage.py runserver
```
## 9. Acceso a Vistas

Una vez que el servidor esté en funcionamiento:

- **Vista Principal (Home):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Lista de Clientes:** [http://127.0.0.1:8000/clientes/](http://127.0.0.1:8000/clientes/)
- **Panel de Administración (Django Jazzmin):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

> Usa las credenciales del superusuario que creaste previamente.

## 10. Características Principales

- Gestión de Clientes.
- Registro de Interacciones.
- Búsqueda y filtrado de clientes.
- Paginación para la lista de clientes.
- Panel de administración moderno y personalizable con Django Jazzmin.
