import React, { Component } from 'react';
import * as Constants from './constants';


class SellerConfirmHandler extends Component {

    state = {
        fid: ''
    }

    confirm = () => {
        const { fid } = this.state;
        // POST /furniture/<fID>/confirm?confirm=True/False
        const confirmUrl = `${Constants.BASE_URL}/furnitures/${fid}/confirm?confirm=True`;
        fetch(confirmUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify({
            //     fid: fid
            // }),
            credentials: "include"
        })
        .then(response => response)
        .then((data) => {
            console.log("seller confirm: ", data);
        })
        .catch((err) => console.log(err))
    }

    notConfirm = () => {
        const { fid } = this.state;
        // POST /furniture/<fID>/confirm?confirm=True/False
        const notConfirmUrl = `${Constants.BASE_URL}/furnitures/${fid}/confirm?confirm=False`;
        fetch(notConfirmUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify({
            //     fid: fid
            // }),
            credentials: "include"
        })
        .then(response => response)
        .then((data) => {
            console.log("seller not confirm: ", data);
        })
        .catch((err) => console.log(err))
    }

    render() {
        return(
            <div>
                <h3>SellerConfirmHandler</h3>
                <input placeholder="fid" onChange={(e) => this.setState({ fid: e.target.value })}></input>
                <button onClick={this.confirm}> Confirm</button>
                <button onClick={this.notConfirm}>Not Confirm</button>
            </div>
        )
    }
}

export default SellerConfirmHandler;
