import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    /**
     * * baseURL: 'https://danielmaestre.es/api', En remoto, configurar esta dirección
     */
    timeout: 3000,
})

export { getAPI }