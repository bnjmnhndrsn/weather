import React, { Component } from 'react';
import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';

// const data = [
//       {name: 'Page A', uv: [100, 4000], pv: 2400, amt: 2400},
//       {name: 'Page B', uv: 3000, pv: 1398, amt: 2210},
//       {name: 'Page C', uv: 2000, pv: 9800, amt: 2290},
//       {name: 'Page D', uv: 2780, pv: 3908, amt: 2000},
//       {name: 'Page E', uv: 1890, pv: 4800, amt: 2181},
//       {name: 'Page F', uv: 2390, pv: 3800, amt: 2500},
//       {name: 'Page G', uv: 3490, pv: 4300, amt: 2100},
// ];

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December'];

export default class Temperatures extends Component {
    mapData () {
        const { selected1, selected2 } = this.props;

        return MONTHS.map((month, i) => {
            const datum = {name: month};
            if (selected1) {
                Object.assign(datum, {[selected1.place_name]: [+selected1.min_data[i].temperature, +selected1.max_data[i].temperature]});
            }

            if (selected2) {
                Object.assign(datum, {[selected2.place_name]: [+selected2.min_data[i].temperature, +selected2.max_data[i].temperature]});
            }

            return datum;
        });
    }

    render () {
        const data = this.mapData();
        console.log(data);
      	return (
            <BarChart width={600} height={300} data={data}
                margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                <XAxis dataKey="name"/>
                <YAxis/>
                <CartesianGrid strokeDasharray="3 3"/>
                <Legend />
                {
                    this.props.selected1 &&
                    <Bar dataKey={this.props.selected1.place_name} fill="#82ca9d" />
                }
                {
                    this.props.selected2 &&
                    <Bar dataKey={this.props.selected2.place_name} fill="#9c27b0" />
                }
            </BarChart>
        );
    }
}
