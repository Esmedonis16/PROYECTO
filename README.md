# 🎓 Sistema de Gestión Académica CUNOC / USAC

Aplicación web desarrollada con **Python y Django**, orientada a la gestión de estudiantes, docentes, cursos y calificaciones del **Centro Universitario de Occidente**.

El proyecto reúne herramientas de administración académica y un flujo experimental de autenticación mediante reconocimiento facial.

> **Estado del proyecto:** implementación académica en desarrollo. Algunas funciones requieren ajustes y pruebas antes de utilizarse en producción.

## 📋 Contenido

- [Descripción](#-descripción)
- [Funcionalidades](#-funcionalidades)
- [Tecnologías](#-tecnologías)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Modelo de datos](#-modelo-de-datos)
- [Funcionamiento general](#-funcionamiento-general)
- [Instalación](#-instalación)
- [Docker](#-docker)
- [Estado y pendientes](#-estado-y-pendientes)
- [Recursos de terceros](#-recursos-de-terceros)

## 📖 Descripción

El sistema busca centralizar procesos académicos en una plataforma web:

- Registro de estudiantes y docentes.
- Acceso de usuarios mediante credenciales.
- Administración de la oferta de cursos.
- Asignación y desasignación de estudiantes.
- Registro de notas.
- Exportación de calificaciones a Excel.
- Notificaciones por correo electrónico.
- Recuperación de contraseñas.
- Identificación facial mediante fotografías de perfil.

El repositorio contiene dos implementaciones relacionadas: **CUNOC** y **USAC**. La carpeta `CUNOC` incorpora el conjunto más amplio de funcionalidades descritas en este documento.

## ⚙️ Funcionalidades

### Estudiantes

- Registro con nombre de usuario, nombres, apellidos, correo, CUI y fotografía.
- Validación de correos ya registrados.
- Inicio y cierre de sesión.
- Consulta del portal estudiantil.
- Visualización de cursos con cupo disponible.
- Asignación y desasignación de cursos.
- Consulta de cursos asignados.

### Docentes y administración

- Registro de docentes y asociación con cuentas de usuario.
- Organización de usuarios mediante grupos.
- Administración de cursos, horarios, costos, cupos y portadas.
- Consulta de cursos vinculados al docente.
- Registro de notas y comentarios.
- Exportación de notas seleccionadas a un archivo `.xlsx`.

### Autenticación y recuperación

- Acceso estudiantil mediante usuario y contraseña.
- Validadores de contraseña para mayúsculas, dígitos y símbolos.
- Configuración de control de intentos fallidos mediante Django Axes.
- Recuperación de contraseña mediante correo electrónico.

### Reconocimiento facial

Se implementó un flujo que:

1. Solicita acceso a la cámara del navegador.
2. Captura una fotografía.
3. Envía la imagen al servidor.
4. Compara el rostro con fotografías de perfiles registrados.
5. Intenta iniciar sesión cuando identifica una coincidencia.

Esta función es experimental y requiere pruebas de precisión, permisos y manejo de errores.

### Correos y reportes

- Preparación de correos de confirmación de asignación y desasignación.
- Plantillas para recuperación de contraseña.
- Generación de reportes Excel con profesor, curso, estudiante, nota y comentario.

> La existencia de estas funciones en el código no implica que todos sus flujos hayan sido verificados en ejecución.

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Desarrollo del servidor |
| Django | Framework web, ORM y autenticación |
| PostgreSQL | Base de datos configurada |
| psycopg2 | Conexión con PostgreSQL |
| Django Jazzmin | Personalización del panel administrativo de CUNOC |
| Django Axes | Control de intentos de acceso |
| Django Crispy Forms | Presentación de formularios |
| Bootstrap | Diseño de interfaces |
| JavaScript y jQuery | Interacción y captura de fotografías |
| face-recognition y dlib | Procesamiento y comparación facial |
| NumPy y Pillow | Procesamiento de imágenes |
| openpyxl | Generación de archivos Excel |
| Docker | Preparación del entorno de desarrollo |

Las dependencias principales están declaradas en:

```text
CUNOC/requirements.txt
```

## 📁 Estructura del repositorio

```text
PROYECTO/
├── CUNOC/
│   ├── CUNOC/                  # Configuración general y rutas
│   ├── ESTUDIANTES/            # Registro, portal y cursos del estudiante
│   ├── Admin_y_Docentes/       # Docentes, cursos, asignaciones y notas
│   ├── contraseña_olvidada/    # Plantillas de recuperación y correos
│   ├── profiles/               # Perfiles y fotografías
│   ├── logs/                   # Registros de intentos de acceso facial
│   ├── media/                  # Archivos cargados por usuarios
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── USAC/
│   ├── Ejemplo/                # Configuración de la implementación USAC
│   ├── Isaac/                  # Funciones estudiantiles
│   ├── Admin_y_Docentes/       # Administración académica
│   ├── loginout/               # Vistas generales y cierre de sesión
│   ├── Templates/
│   └── manage.py
│
├── Examen_Final/               # Entorno virtual incluido en el repositorio
├── Paquetes.txt               # Lista de dependencias
├── excel.txt                  # Lista ampliada de dependencias
└── README.md
```

La carpeta `Examen_Final` contiene bibliotecas y archivos de un entorno virtual; no representa un módulo académico del sistema.

## 🗃️ Modelo de datos

| Modelo | Descripción |
|---|---|
| `User` | Cuenta de autenticación de Django |
| `allusuarios` | Información del estudiante |
| `inges` | Información del docente |
| `cursos` | Cursos, horarios, costos, cupos y docente |
| `EstudianteCurso` | Relación de asignación entre estudiante y curso |
| `Notas` | Calificación y comentario por estudiante y curso |
| `Profile` | Perfil y fotografía utilizados en el acceso facial |
| `Log` | Fotografía y registro de un intento de identificación |
| `Registros` | Entrada administrativa al formulario de registro docente |

Los modelos `EstudianteCurso`, `Profile` y `Log` forman parte de la implementación CUNOC.

## 🔄 Funcionamiento general

### Registro estudiantil

El usuario completa el formulario con sus datos y fotografía. El sistema crea la cuenta, guarda la información académica y la vincula al grupo `Estudiantes`.

### Asignación de cursos

El estudiante consulta cursos con cupo disponible. Al solicitar una asignación, el sistema registra la relación con el curso, disminuye el cupo e intenta enviar un correo de confirmación.

La desasignación elimina la relación y devuelve el cupo correspondiente.

> El indicador denominado “Asignado y Pagado” se activa en la inscripción. No se identificó una integración que verifique pagos.

### Administración de notas

El docente utiliza el panel administrativo para gestionar las notas de sus cursos. La implementación CUNOC permite exportar las notas seleccionadas a Excel.

### Acceso facial

El servidor compara una fotografía capturada con las imágenes de perfiles registrados. Cuando obtiene una coincidencia, intenta autenticar al usuario asociado.
