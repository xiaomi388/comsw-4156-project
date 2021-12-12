import React, { Component } from 'react';
import * as Constants from './constants';


class BuyerHandler extends Component {

    state = {
        fid: ''
    }

    buy = () => {
        
    }

    render() {
        return(
            <div>
                <h3>
                    This is Buyer handler
                    <button onClick={this.buy}></button>
                </h3>
            </div>
        )
    }
}

export default BuyerHandler;
