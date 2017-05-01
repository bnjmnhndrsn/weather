import React, { Component } from 'react';

export default class App extends Component {
    render(){
        return <div onClick={() => console.log('hi')}>Hello and welcome to my app</div>;
    }
}
