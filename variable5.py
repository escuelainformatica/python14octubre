# los flotantes, no son numeros exactos.
# los flotantes los maneja la FPU (Floating), por lo tanto son operaciones rapidas.
# los flotantes pueden dar datos inexactos

import decimal

flotante1=1.01
flotante2=1.02
print(flotante1+flotante2)  # 2.0300000000000002  = 2.03

dec1=decimal.Decimal("1.01")  # Decimal
dec2=decimal.Decimal("1.02")  # Decimal
print(dec1+dec2)  # 2.030000000000000026645352591
