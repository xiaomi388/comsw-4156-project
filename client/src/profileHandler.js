import React, { Component } from 'react';
import * as Constants from './constants';


class ProfileHandler extends Component {
    
    getUserProfile = () => {
        alert("Get user profile");

        const getUserProfileUrl = `${Constants.BASE_URL}/profile`;
        fetch(getUserProfileUrl, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
            },
        })
        .then(response => response)
        .then((data) => {
            console.log("get user profile data: ", data);
        })
        .catch((err) => console.log(err))
    }
    
    render() {
        return(
            <div>
                <h3>Profile Handler</h3> <p>(Cannot get profile without login)</p>
                <button onClick={this.getUserProfile}>Get Profile</button>
            </div>
        )
    }
}

export default ProfileHandler;