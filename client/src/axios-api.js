import axios from 'axios'

let baseURL;

if (process.env.NODE_ENV === 'development') {
    baseURL = process.env.VUE_APP_API_MAIN_URL_DEV;
} else {
    baseURL = process.env.VUE_APP_API_MAIN_URL_PROD;
}

const getAPI = axios.create({
    baseURL: baseURL,
    timeout: 3000,
})

export { getAPI }