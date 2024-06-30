import axios from 'axios'

//Note Mobile URL is http://10.0.2.2:8000/'
//Note Web URL is 'http://10.0.2.2:8000/'

const Base_Url = 'http://10.0.2.2:8000/'
// const Base_Url = 'http://127.0.0.1:8000/'

export const AxiosInstance = axios.create({
    baseURL: Base_Url, 
    timeout: 30000, 
    headers:    {
                    "Content-Type": "application/json", 
                    accept: "application/json"
                }
})
