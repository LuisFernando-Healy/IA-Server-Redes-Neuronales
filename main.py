from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np

# 1. Inicializamos la API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# 2. Cargamos el modelo de YOLO 
model = YOLO("yolov8n.pt") 

@app.post("/detectar")
async def procesar_imagen(file: UploadFile = File(...)):
    try:
        # 3. Leer la imagen enviada por el celular (desde la memoria, sin guardarla en disco para ser veloces)
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return {"error": "No se pudo leer la imagen"}

        resultados = model(img)

        detecciones = []
        
        # 5. Analizar lo que vio la IA 
        for r in resultados:
            for box in r.boxes:
                clase_id = int(box.cls[0])
                nombre_objeto = model.names[clase_id] # Ej: 'cell phone', 'bottle', 'person'
                confianza = float(box.conf[0])
                
                
                # Matemáticas de proporciones (área de la caja vs área total de la imagen)
                x1, y1, x2, y2 = box.xyxy[0]
                area_caja = (x2 - x1) * (y2 - y1)
                area_total = img.shape[0] * img.shape[1]
                proporcion = area_caja / area_total
                
                # Lógica para determinar el tamaño/distancia
                if proporcion > 0.5:
                    tamano = "bastante grande o muy cerca de la cámara"
                elif proporcion > 0.15:
                    tamano = "de tamaño mediano"
                else:
                    tamano = "pequeño o a lo lejos"

                # Construcción de la respuesta final
                descripcion_inteligente = f"He detectado un {nombre_objeto} {tamano}. Estoy seguro al {int(confianza * 100)} por ciento."

                detecciones.append({
                    "objeto": nombre_objeto,
                    "descripcion": descripcion_inteligente,
                    "confianza": confianza
                        
                })

        # 6. Responder al celular con el objeto más seguro que detectó
        if detecciones:
            mejor_deteccion = max(detecciones, key=lambda x: x["confianza"])
            return mejor_deteccion
        else:
            return {
                "objeto": "desconocido", 
                "descripcion": "No veo nada con claridad en esta imagen. Intenta enfocar de nuevo."
            }
            
    except Exception as e:
        return {"error": str(e)}
    

    # comando para ejecutar la app
    #           |
    #           |
    #           v
    #  main:app --host 0.0.0.0 --port 8000

    