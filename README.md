🏗️ Automatización de Formularios MINVU
Prototipo de integración entre ERP de arquitectura y formularios oficiales

Este repositorio contiene un prototipo experimental de frontend cuyo objetivo es automatizar el llenado de formularios utilizados en trámites del Ministerio de Vivienda y Urbanismo (MINVU) de Chile.

La idea central del proyecto es conectar un sistema tipo ERP de arquitectura con plantillas de formularios oficiales, permitiendo generar documentos prellenados a partir de información ya almacenada en el sistema.

🎯 Problema que intenta resolver

En la práctica profesional de arquitectura y gestión de vivienda en Chile, los expedientes requieren completar múltiples formularios manualmente.

Esto genera problemas como:

repetición constante de datos

errores en el ingreso de información

pérdida de tiempo administrativo

duplicación de trabajo entre sistemas

Este proyecto intenta explorar una solución donde:

Base de datos del proyecto
        │
        ▼
ERP / sistema de gestión
        │
        ▼
Frontend de formulario
        │
        ▼
Plantilla MINVU prellenada

De esta forma el profesional ingresa los datos una sola vez.

🧠 Idea del sistema

El sistema propuesto se basa en tres componentes:

1️⃣ ERP o base de datos de proyectos

Contiene información como:

datos del propietario

datos del inmueble

superficie

rol de avalúo

ubicación

antecedentes técnicos

2️⃣ Interfaz de formulario

El frontend permite:

visualizar los datos

editar información

mapear campos hacia formularios oficiales

3️⃣ Generación automática de formularios

El objetivo final era generar documentos como:

formularios MINVU

fichas técnicas

documentos de postulación

completados automáticamente.

📂 Estructura del repositorio

El repositorio contiene archivos de prueba y documentación relacionados con el intento de integración.

Ejemplo de estructura general:

proyecto_educativo
│
├── docs/
│   ├── estudios y notas
│   └── pruebas de formularios
│
├── markdown/
│   ├── ejercicios
│   └── documentación técnica
│
└── recursos del proyecto

El repositorio se utilizó principalmente como espacio de experimentación y documentación.

⚙️ Tecnologías exploradas

El proyecto considera o explora el uso de:

Python

Django

HTML / CSS

generación automática de formularios

plantillas PDF

La idea era integrarlo con una aplicación existente desarrollada en otro repositorio.

🚧 Estado del proyecto

⚠️ Prototipo experimental

Este repositorio representa un intento inicial de:

incrustar una aplicación existente

conectar un frontend con formularios

automatizar el llenado de documentos

La integración completa no fue finalizada, pero el proyecto sirve como base conceptual para futuros desarrollos.

💡 Posible evolución del proyecto

A futuro el sistema podría evolucionar hacia:

un ERP especializado para arquitectura

automatización de formularios MINVU

generación automática de expedientes de regularización

integración con sistemas de subsidios habitacionales

Esto sería especialmente útil para profesionales que trabajan con:

permisos de edificación

regularización de viviendas

subsidios habitacionales

expedientes técnicos

👤 Autor

Loreto Salazar Salina
Arquitecta | Desarrollo de herramientas digitales para gestión de proyectos habitacionales
