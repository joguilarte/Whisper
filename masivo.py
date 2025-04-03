import whisper
from docx import Document
import os

# Cargar el modelo de Whisper (usar un modelo más preciso)
model = whisper.load_model("base")  # O prueba con "large"

# Ruta a la carpeta con los archivos de audio
audio_folder = "C:/Users/guilarte.j510/Desktop/Reuniones/audios"

# Obtener la lista de archivos de audio en la carpeta
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]

# Transcribir cada archivo de audio
for audio_file in audio_files:
    audio_path = os.path.join(audio_folder, audio_file)
    
    # Transcribir el archivo de audio forzando español
    result = model.transcribe(audio_path, language="es", task="transcribe")
    
    # Crear un nuevo documento de Word
    doc = Document()
    
    # Añadir la transcripción al documento de Word
    doc.add_paragraph(result["text"])
    
    # Guardar el documento de Word con el mismo nombre que el archivo de audio
    doc_name = os.path.splitext(audio_file)[0] + ".docx"
    doc_path = os.path.join(audio_folder, doc_name)
    doc.save(doc_path)
    
    print(f"Transcripción completada y guardada en {doc_path}")
