from fastapi import FastAPI, UploadFile, File, HTTPException
from api import pipeline
from api.logger import get_logger

logger = get_logger("api")

app = FastAPI()

@app.get("/health")
def health_check():
    dict = {"status" : "ok"}
    return dict

@app.post("/upload")
def upload_video(arquivo: UploadFile = File(...)):
    logger.info(f"Recebendo upload: {arquivo.filename}")
    try:
        conteudo = arquivo.file.read()
        resultado = pipeline.processar(conteudo)
        logger.info(f"Processamento concluído do {resultado['video_id']}")
        return resultado
    except Exception as e:
        logger.error(f"Erro no processamento {e}")
        raise HTTPException(status_code=500, detail=str(e))