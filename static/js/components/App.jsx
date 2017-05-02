import React, { Component } from 'react';

import LocationPicker from './LocationPicker';
import Temperatures from './Temperatures';
import API from '../api';

export default class App extends Component {
    constructor(){
        super();
        this.state = {
            selected1: null,
            selected2: null,
            detailData: {}
        };

        this.onSelect1 = this.onSelect1.bind(this);
        this.onSelect2 = this.onSelect2.bind(this);

    }

    onSelect1(item){
        this.setState({selected1: item});
        this.fetchDetail(item);
    }

    onSelect2(item){
        this.setState({selected2: item});
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
        const selectedData1 = this.state.selected1 && this.state.detailData[this.state.selected1.id];
        const selectedData2 = this.state.selected2 && this.state.detailData[this.state.selected2.id];

        return (
            <div>
                <div>
                    <h1>
                        Select Location
                    </h1>
                    <LocationPicker selected={this.state.selected1} onSelect={this.onSelect1} />
                </div>
                <div>
                    <h1>
                        Select Another
                    </h1>
                    <LocationPicker selected={this.state.selected2} onSelect={this.onSelect2} />
                </div>

                {
                    (selectedData1 || selectedData2) &&
                    <Temperatures selected1={selectedData1} selected2={selectedData2} />
                }
            </div>
        );
    }
}
