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

function fetchDetail(id){
    return axios({
        method: 'GET',
        url: `/json/locations/${id}/`
    });
}

const API = {
    searchLocations,
    fetchDetail
};

export default API;
