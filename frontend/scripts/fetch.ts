import { useQuery } from "react-query";
import axios from "axios";

export const useFetch = (API_Parameters: string, PDF_ID: string) =>
{
    const Get_Request = async () =>
    {
        const {data} = await axios.get(`http://10.0.2.2:8000/${API_Parameters}/${PDF_ID}`)
        return await data
    }

    const {data, status} = useQuery(API_Parameters, () => Get_Request())

    return status != "success" ? [[]] : data
}