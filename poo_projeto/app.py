from fastapi import FastAPI, HTTPException
from classe.TipousuarioClass import TipoUsuario

app = FastAPI()

@app.get("/tipousuario", response_model=list)
async def tipousuario():
    tipo_usuario = TipoUsuario()
    tipos_usuario = tipo_usuario.get_tiposusuario()
    return tipos_usuario

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)