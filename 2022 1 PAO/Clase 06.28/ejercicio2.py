resultado = "Resultado de Laboratorio 'Su Salud' Nombre del paciente: José Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma médico responsable Dr. Juan Pozo"
resultado=resultado.split(' ')#lista
print("INFORME DE LABORATORIO\n**********************")
recomendacion=''
for i in range(len(resultado)):
    if resultado[i].isupper():
        print("{:5s} {:<10.2f} {:>10s}".format(resultado[i],float(resultado[i+1]),resultado[i+2]))
        if resultado[i]=='HGB' and float(resultado[i+1])<14:
            recomendacion='**Su nivel de hemoglobina es bajo, se recomienda ir al hematólogo.'
    if resultado[i]=='Dr.' or resultado[i]=='Dra.':
        medico=' '.join(resultado[i+1:])

print("\nMedico: {}".format(medico))
if len(recomendacion)!=0:
    print(recomendacion)
