import { useQuery } from "react-query";
import axios from "axios";

export const useFetch = (PDF_ID: string) =>
{
    const Get_Request = async () =>
    {
        const {data} = await axios.get(`http://10.0.2.2:8000/get/PDF/${PDF_ID}`)
        return await data
    }

    const {data, status} = useQuery("Fetch", () => Get_Request())

    return status != "success" ? [[]] : data
}
