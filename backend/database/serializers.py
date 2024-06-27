def Analytics_Serializer(Analytic):
    return {
            "PDF_ID": Analytic["PDF_ID"],
            "Avg": Analytic["Avg"]
            }

def Analytics_Deserializer(Analytics):
    return  [Analytics_Serializer(Analytic) for Analytic in Analytics]