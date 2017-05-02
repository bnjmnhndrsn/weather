import React, { Component } from 'react';

import LocationPicker from './LocationPicker';

export default class App extends Component {
    constructor(){
        super();
        this.state = {
            selected: null
        };

        this.onSelect = this.onSelect.bind(this);
    }

    onSelect(item){
        this.setState({selected: item});

    }

    render(){
        return (
            <div>
                <LocationPicker selected={this.state.selected} onSelect={this.onSelect} />
            </div>
        );
    }
}
