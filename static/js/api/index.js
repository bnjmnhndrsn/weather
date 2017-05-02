import axios from 'axios';

function searchLocations(query){
    return axios({
        method: 'GET',
        url: '/json/search/',
        params: {
            query
        }
    });
}

const API = {
    searchLocations
};

export default API;
