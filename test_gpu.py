import torch

print("=====================================")
# 1. Verifica si CUDA (el motor de tu gráfica) está disponible
cuda_disponible = torch.cuda.is_available()
print(f"¿CUDA está disponible?: {cuda_disponible}")

if cuda_disponible:
    # 2. Imprime el nombre exacto de la tarjeta de video
    nombre_gpu = torch.cuda.get_device_name(0)
    print(f"Tarjeta gráfica detectada: {nombre_gpu}")
    print("¡El entorno está listo para volar! 🚀")
else:
    print("Algo salió mal. PyTorch está usando el procesador (CPU).")
print("=====================================")