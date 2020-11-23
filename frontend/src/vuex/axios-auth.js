import axios from 'axios';
const instance = axios.create({
    baseURL: 'https://digital-library-iu.herokuapp.com'
});
export default instance;