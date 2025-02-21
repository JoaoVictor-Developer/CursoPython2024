O = 184590.506540 #Orçamento
G = 7945.96549 #Gasto
L = O - G #Lucro
print("Faturamento: ",O)
print("Gasto: ",int(G))
print("Lucro: ",round(L,1))

TempoDeContrato = 190 #messes
TempoEmDias = 190 * 30
TempoEmAnos = 1990 / 12 #Anos
TempoEmAnosSobra = 190 % 12 #Anos(messes)
print("TEMPODECONTRATO:")
print("Dias: ",TempoEmDias)
print("Mêses: ",TempoDeContrato)
print("Anos: ",int(TempoEmAnos),"E ",TempoEmAnosSobra," Mêses")