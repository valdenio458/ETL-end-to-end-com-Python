from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class AnuncioData(BaseModel):
    Organizador: int = Field(..., description="ID do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês no formato YYYY-MM")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio")   
    Tipo_Dia: str = Field(..., description="Tipo de dia")
    Objetivo: str = Field(..., description="Objetivo do anúncio")
    Date: date = Field(..., description="Data do anúncio")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(..., description="Valor gasto")
    Link_clicks: Optional[int] = Field(..., description="Cliques no link")
    Impressions: Optional[int] = Field(..., description="Impressões")
    Conversions: Optional[int] = Field(..., description="Conversões")
    Segmentação: str = Field(..., description="Segmentação do anúncio")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase da campanha")


user = AnuncioData()
print(user)
