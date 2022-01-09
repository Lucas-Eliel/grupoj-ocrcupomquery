from src.model.enum.Status import Status
from src.repository.ocr_cupom_redis import OcrCupomRedis
from src.repository.ocr_cupom_repository import OcrCupomRepository
from src.utils.decimal_encoder import DecimalEncoder
import json
import ast


class OcrCupomService:

    def __init__(self, event):
        self.event = event
        self.repository = OcrCupomRepository()
        self.redis = OcrCupomRedis()

    def obter_cupons_validos(self):

        dados_redis = self.redis.get(Status.VALIDO.name)

        if dados_redis is not None:
            return ast.literal_eval(dados_redis.decode("utf-8"))
        else:
            response = self.repository.find_by_status(Status.VALIDO.value)
            self.redis.save(Status.VALIDO.name, str(json.dumps(response, cls=DecimalEncoder)))
            return response

    def obter_cupons_invalidos(self):

        dados_redis = self.redis.get(Status.INVALIDO.name)

        if dados_redis is not None:
            return ast.literal_eval(dados_redis.decode("utf-8"))
        else:
            response = self.repository.find_by_status(Status.INVALIDO.value)
            self.redis.save(Status.INVALIDO.name, str(json.dumps(response, cls=DecimalEncoder)))
            return response
