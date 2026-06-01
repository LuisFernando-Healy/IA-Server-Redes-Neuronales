![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO_Model-FF6F00?style=for-the-badge&logo=yolo&logoColor=white)
![AI & Computer Vision](https://img.shields.io/badge/AI_&_CV-Machine_Learning-blue?style=for-the-badge)

> **Aplicación móvil multiplataforma impulsada por IA para la detección e identificación de objetos en tiempo real.**

Este repositorio contiene el código fuente de una aplicación móvil desarrollada en **Flutter** que integra un modelo de Deep Learning (**YOLO - You Only Look Once**) para el análisis de imágenes y reconocimiento de objetos a través de la cámara del dispositivo. 

## Arquitectura y Tecnologías

El proyecto demuestra la capacidad de integrar modelos complejos de Inteligencia Artificial en interfaces de usuario fluidas y responsivas.

* **Frontend / UI:** Flutter & Dart.
* **Motor de Inferencia (IA):** Modelo YOLO (You Only Look Once) optimizado para detección rápida.
* **Integración de Hardware:** Uso nativo de la cámara del dispositivo para captura de frames.
* **Gestión de Estado:** [Menciona aquí si usaste Provider, Riverpod, Bloc, o solo setState, ej: *Provider para la gestión del flujo de datos de la cámara*].

## Características Principales (Features)

**Análisis en Tiempo Real:** Captura de imágenes directamente desde la cámara del dispositivo móvil para su procesamiento inmediato.
**Detección de Alta Precisión:** Identificación de múltiples objetos simultáneos en un solo frame utilizando la arquitectura YOLO.
**Bounding Boxes Dinámicos:** Dibujo algorítmico de cajas delimitadoras (bounding boxes) y etiquetas con el porcentaje de confianza sobre la imagen original.
**UI Fluida y Reactiva:** Interfaz de usuario diseñada en Flutter que mantiene los 60 FPS sin bloquear el hilo principal durante la inferencia del modelo.
