"""Calculo de boleta de venta."""

from dataclasses import dataclass

IGV = 0.18
DESCUENTO = 0.10

@dataclass
class Boleta:
subtotal: float
cliente_frecuente: bool = False

def calcular(boleta: Boleta) -> float:
total = boleta.subtotal

if boleta.cliente_frecuente and total >= 100:
    total -= total * DESCUENTO

if total >= 200:
    total += total * IGV
else:
    total += total * (IGV - 0.03)

return round(total, 2)
