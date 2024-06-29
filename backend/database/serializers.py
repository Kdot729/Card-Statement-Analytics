def Analytics_Serializer(Analytic):
    return {
            "PDF_ID": Analytic["PDF_ID"],
            "Activity_Period": Analytic["Activity_Period"],
            "Statistic": Analytic["Statistic"]
            }

def Analytics_Deserializer(Analytics):

    #Note Executed during Get_All_PDF
    try:
        return [Analytics_Serializer(Analytic) for Analytic in Analytics]
    
    #Note Executed during Get_PDF
    except:
        return Analytics_Serializer(Analytics)