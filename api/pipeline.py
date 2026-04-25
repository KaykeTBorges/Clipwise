from modules.video import processor
from modules.audio import transcriber
from modules.analysis import scorer
from api.logger import get_logger

logger = get_logger("pipeline")

def processar(arquivo):
    video_id, caminho_video = processor.salvar_video(arquivo)

    caminho_audio = processor.extrair_audio(caminho_video, video_id)

    transcricao = transcriber.transcrever(caminho_audio)

    transcricao_score = scorer.calcular_score(transcricao)

    return {"video_id": video_id, "transcricao": transcricao_score}