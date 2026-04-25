import uuid
from pathlib import Path
import subprocess

from api.logger import get_logger

logger = get_logger("processor")

VIDEOS_DIR = Path("storage/videos")
AUDIO_DIR = Path("storage/audio")

def salvar_video(arquivo):
    video_id = str(uuid.uuid4())
    caminho_video = VIDEOS_DIR / f"{video_id}.mp4"
    
    logger.info(f"Iniciando processamento do vídeo: {video_id}")

    try:
        with open(caminho_video, "wb") as f:
            f.write(arquivo)
        logger.info(f"Vídeo salvo com sucesso: {caminho_video}")
    except Exception as e:
        logger.error(f"Erro ao salvar vídeo na memória: {e}")
        raise
    
    return video_id, caminho_video

def extrair_audio(caminho_video, video_id):
    caminho_audio = AUDIO_DIR / f"{video_id}.wav"

    logger.info(f"Extraindo áudio de: {caminho_video}")
    resultado = subprocess.run([
        "ffmpeg", "-i", str(caminho_video),
        "-q:a", "0", "-map", "a",
        str(caminho_audio)
    ], stdin=subprocess.DEVNULL, capture_output=True, text=True)

    if resultado.returncode != 0:
        logger.error(f"ffmpeg falhou: {resultado.stderr}")
        raise Exception(f"Erro ao extrair áudio: {resultado.stderr}")

    logger.info(f"Áudio extraído com sucesso: {caminho_audio}")
    return caminho_audio