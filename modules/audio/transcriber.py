from faster_whisper import WhisperModel
from api.logger import get_logger

logger = get_logger("transcriber")

def transcrever(caminho_audio):
    logger.info(f"Iniciando transcrição: {caminho_audio}")
    try:
        model = WhisperModel("small", device="cpu", compute_type="default")
        segments, info = model.transcribe(str(caminho_audio), beam_size=5)

        resultado = []
        for segment in segments:
            dado = {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            }
            resultado.append(dado)

        logger.info(f"Transcrição concluída: {len(resultado)} segmentos")
        return resultado
    except Exception as e:
        logger.error(f"Erro ao chamar a Transcrição {e}")
        raise
    
