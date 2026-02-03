# PlayHub/middleware.py
import time
import logging

logger = logging.getLogger(__name__)  # usamos el logger de Django

class RegistroRequestMiddleware:
    """
    Middleware que registra: ruta, método, usuario y tiempo de ejecución
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # guardamos el tiempo de inicio

        response = self.get_response(request)  # ejecutamos la vista

        # calculamos tiempo de ejecución
        duration = time.time() - start_time

        # usuario
        if request.user.is_authenticated:
            usuario = request.user.username
        else:
            usuario = "Anonimo"

        # logueamos la info
        logger.info(
            f"[Middleware] Ruta: {request.path}, Método: {request.method}, "
            f"Usuario: {usuario}, Tiempo: {duration:.4f} segundos"
        )

        return response
