def Analytics_Serializer(Analytic):
    return {
            "PDF_ID": Analytic["PDF_ID"],
            "Activity_Period": Analytic["Activity_Period"],
            "Mean": Analytic["Mean"]
            }

def Analytics_Deserializer(Analytics):
    return  [Analytics_Serializer(Analytic) for Analytic in Analytics]