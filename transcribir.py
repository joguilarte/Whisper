import whisper
from docx import Document

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Ruta al archivo de audio que deseas transcribir
audio_path = "C:/Users/guilarte.j510/Desktop/Reuniones/audios/fran.wav"

# Transcribir el archivo de audio
result = model.transcribe(audio_path)

# Crear un nuevo documento de Word
doc = Document()

# Añadir la transcripción al documento de Word
doc.add_paragraph(result["text"])

# Guardar el documento de Word
doc_path = "C:/Users/guilarte.j510/Desktop/transcripcion.docx"
doc.save(doc_path)

print(f"Transcripción completada y guardada en {doc_path}")
