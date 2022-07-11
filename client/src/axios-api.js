import axios from 'axios'

const getAPI = axios.create({
    /**
     * * baseURL: 'http://127.0.0.1:8000', En local, configurar esta dirección
     */
    baseURL: 'https://danielmaestre.es/api',
    timeout: 3000,
})

export { getAPI }