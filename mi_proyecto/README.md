# 🎸 Proyecto Rock Nacional - Catálogo Interactivo

Este proyecto es una aplicación web desarrollada en **Django** que permite administrar un catálogo de artistas, bandas y canciones del rock nacional. Incluye funciones CRUD completas, un sistema de búsqueda y autenticación de usuarios.

---

## 🛠️ Tecnologías Utilizadas
* **Python** 🐍
* **Django** 📦
* **SQLite** 🗄️ (Base de datos por defecto)

---

## 📂 Estructura Principal de Funcionalidades

El proyecto está organizado de la siguiente manera dentro de la aplicación principal (`mi_app`):

* **Inicio (Home):** Vista basada en `TemplateView` que presenta la información general del proyecto y la sección "Acerca de".
* **Modelos (CRUDs):** Secciones independientes para gestionar la base de datos:
  * 👤 **Artistas:** `Persona` (Nombre, Apellido, Instrumento, Edad).
  * 👥 **Bandas:** `Banda` (Nombre, Género, Año de formación).
  * 🎵 **Canciones:** `Cancion` (Título, Álbum, Año de lanzamiento).
* **Autenticación:** Sistema de usuarios ubicado en la carpeta de plantillas `registration/` (Registro, Login y Logout).

---

## 🚀 Orden Sugerido para Probar el Sitio

Para verificar que todo el sistema funciona correctamente, se recomienda seguir este orden de prueba en el navegador:

### 1. Portada e Información (`/`)
* Al ingresar a la URL principal, se cargará el **Home** con la bienvenida, la descripción del proyecto y la barra de navegación global.

### 2. Registro de Usuario (`/register/`)
* Ve a la sección **Registrarse** en la barra de navegación.
* Crea una cuenta nueva completando el formulario. Al finalizar, el sistema te redirigirá automáticamente al Login.

### 3. Inicio de Sesión (`/login/`)
* Inicia sesión con las credenciales que acabas de crear.
* Verifica que la barra de navegación cambie dinámicamente: ahora mostrará un mensaje de bienvenida con tu nombre de usuario y el enlace para **Cerrar Sesión**.

### 4. Pruebas del CRUD (Artistas, Bandas y Canciones)
* Navega a cualquiera de las tres secciones desde el menú (por ejemplo, **Canciones**).
* **Crear:** Haz clic en el botón para agregar un nuevo registro y completa el formulario.
* **Leer y Buscar:** Verifica que el nuevo registro aparezca en la lista general. Usa la barra de búsqueda superior para filtrar por nombre o título.
* **Editar:** Haz clic en modificar para cambiar algún dato y asegurar que se guarde.
* **Borrar:** Prueba eliminar un registro y confirma la acción.

### 5. Cierre de Sesión (`/logout/`)
* Haz clic en **Cerrar Sesión**. La barra de navegación volverá a mostrar las opciones de *Iniciar Sesión* y *Registrarse*.