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
    }

    render() {
        return(
            <div>
                <h3>
                    This is Buyer handler
                    <input placeholder="fid" onChange={(e) => this.setState({ fid: e.target.value })} ></input>
                    <button onClick={this.buy}></button>
                </h3>
            </div>
        )
    }
}

export default BuyerHandler;
