import React, { Component } from 'react';
import * as Constants from './constants';


class BuyerHandler extends Component {

    state = {
        fid: ''
    }

    buy = () => {
        const { fid } = this.state;
        const buyFurnitureUrl = `${Constants.BASE_URL}/furnitures/${fid}/buy`;
        // fetch()
        fetch(buyFurnitureUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                fid: fid
            }),
            credentials: "include"
        })
        .then(response => response)
        .then((data) => {
            console.log("buyer buy: ", data);
        })
        .catch((err) => console.log(err))
    }

    render() {
        return(
            <div>
                <h3>
                    Buyer handler

                </h3>
                    <input placeholder="fid" onChange={(e) => this.setState({ fid: e.target.value })} ></input>
                    <button onClick={this.buy}>Buy</button>
            </div>
        )
    }
}

export default BuyerHandler;
