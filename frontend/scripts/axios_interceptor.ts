import axios from 'axios'

const Base_Url = 'http://127.0.0.1:8000/'
export const AxiosInstance = axios.create({
    baseURL: Base_Url, 
    timeout: 30000, 
    headers:    {
                    "Content-Type": "application/json", 
                    accept: "application/json"
                }
})
