from src.model.enum.Status import Status
from src.repository.ocr_cupom_repository import OcrCupomRepository


class OcrCupomService:

    def __init__(self, event):
        self.event = event
        self.repository = OcrCupomRepository()

    def obter_cupons_processados(self):
        return self.repository.find_by_status(Status.VALIDO.value)

    def obter_cupons_nao_processados(self):
        return self.repository.find_by_status(Status.INVALIDO.value)

