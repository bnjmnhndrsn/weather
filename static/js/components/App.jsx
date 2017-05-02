import React, { Component } from 'react';

import LocationPicker from './LocationPicker';
import Temperatures from './Temperatures';
import API from '../api';

export default class App extends Component {
    constructor(){
        super();
        this.state = {
            selected: null,
            detailData: {}
        };

        this.onSelect = this.onSelect.bind(this);
    }

    onSelect(item){
        this.setState({selected: item});
        this.fetchDetail(item);
    }

    fetchDetail(item){
        API.fetchDetail(item.id).then(resp => {
            this.setState({
                detailData: Object.assign({}, this.state.detailData, {[item.id]: resp.data})
            });
        });
    }

    render(){
        const selectedData = this.state.selected && this.state.detailData[this.state.selected.id];

        return (
            <div>
                <LocationPicker selected={this.state.selected} onSelect={this.onSelect} />
                {
                    selectedData &&
                    <Temperatures {...selectedData} />
                }
            </div>
        );
    }
}
