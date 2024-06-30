import { useQuery } from "react-query";
import axios from "axios";

export const useFetch = (PDF_ID) =>
{
    const Get_Request = async () =>
    {
    
        const Domain_Name = window.location.hostname
        const {data} = await axios.get(`http://${Domain_Name}:8000/get/PDF/${PDF_ID}`)
    
        return await data
    
    }

    const {data, status} = useQuery("Fetch", () => Get_Request(PDF_ID))

    return status != "success" ? [[]] : data
}
