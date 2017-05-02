import React, { Component } from 'react';
import API from '../api';

const Location = (props) => {
    return <span>{ `${props.place_name}, ${props.subnational_entity}` }</span>;
}

export default class LocationPicker extends Component {
    constructor(){
        super();
        this.state = {
            isEditing: false,
            query: '',
            choices: null
        };

        this.updateQuery = this.updateQuery.bind(this);
        this.onSelect = this.onSelect.bind(this);
    }

    updateQuery(e){
        const newVal = e.target.value;
        this.setState({query: newVal});
        if (newVal.length > 2) {
            this.searchLocations(newVal);
        } else {
            this.setState({choices: null});
        }
    }

    searchLocations(query){
        // TODO debounce
        API.searchLocations(query).then((resp) => {
            this.setState({
                choices: resp.data
            });
        });
    }

    onSelect(item){
        this.props.onSelect(item);
        this.setState({isEditing: false, choices: null, query: ''});
    }

    renderChoices(){
        let choices;
        if (!this.state.choices) {
            choices = <li>Please type more than 2 characters</li>
        } else if (this.state.choices.length) {
            choices = this.state.choices.map(item => (
                <li key={item.id} onClick={() => this.onSelect(item)}>
                    <Location {...item} />
                </li>
            ));
        } else {
            choices = <li>No Results Found</li>
        }

        return <ul>{ choices }</ul>;
    }

    render() {
        if (this.state.isEditing) {
            return (
                <div>
                    <div>
                        <input type="text" value={this.state.query} onChange={this.updateQuery} />
                    </div>
                    <div>
                        { this.renderChoices() }
                    </div>
                </div>
            );
        } else {
            return (
                <div>
                    <div>
                        <span>
                            {
                                this.props.selected ?
                                <Location {...this.props.selected} /> :
                                'Nowhere selected'
                            }
                        </span>
                        {' '}
                        <button type="button" onClick={() => this.setState({isEditing: true})}>
                            Edit
                        </button>
                    </div>
                </div>
            );
        }
    }
}
