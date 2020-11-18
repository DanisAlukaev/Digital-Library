import axios from 'axios';
const instance = axios.create({
    baseURL: ''//todo change url
});
export default instance;