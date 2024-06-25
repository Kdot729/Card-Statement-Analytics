def Analytics_Serializer(Analytic):
    return {
            "URI_ID": Analytic["URI_ID"],
            "Avg": Analytic["Avg"]
            }

def Analytics_Deserializer(Analytics):
    return  [Analytics_Serializer(Analytic) for Analytic in Analytics]