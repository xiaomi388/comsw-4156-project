

import React, { Component } from 'react';
import * as Constants from './constants';


class RatingHandler extends Component {

    state = {
        fid: '',
        rating: 0,
    }

    rate = () => {
        const { fid, rating } = this.state;
        const rateFurnitureUrl = `${Constants.BASE_URL}/furnitures/${fid}/rate?rating=${rating}`;
        console.log("rateFurnitureUrl: ", rateFurnitureUrl);
        // fetch()
        fetch(rateFurnitureUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify({}),
            credentials: "include"
        })
        .then(response => response)
        .then((data) => {
            console.log("data: ", data);
            if (data.status === 200 || data.status === 201) {
                alert('date furniture!');
            } else {
                alert('fail to rate furniture, status=', data.status);
            }
        })
        .catch((err) => console.log(err))
    }

    render() {
        return(
            <div>
                <h3>
                    This is Rating Handler
                </h3>

                <input placeholder="fid" onChange={(e) => this.setState({ fid: e.target.value })} ></input>
                <input placeholder="rating in [0, 5]" onChange={(e) => this.setState({ rating: parseInt(e.target.value) })} ></input>
                <button onClick={this.rate}>Rate</button>
            
            </div>
        )
    }
}

export default RatingHandler;
