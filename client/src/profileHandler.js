import React, { Component } from 'react';
import * as Constants from './constants';


class ProfileHandler extends Component {
    
    state = {
        email: ""
    }

    getUserProfile = () => {
        alert("Get user profile");

        const getUserProfileUrl = `${Constants.BASE_URL}/profile`;
        fetch(getUserProfileUrl, {
            method: 'GET',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
            },
            credentials: "include"
        })
        .then(response => response.json())
        .then((data) => {
            this.setState({
                email: data.profile.email
            });
            console.log("get user profile data: ", data);
        })
        .catch((err) => console.log(err))
    }
    
    render() {
        const { email } = this.state;

        return(
            <div>
                <h3>Profile Handler</h3>
                 <p>{email}</p>
                <button onClick={this.getUserProfile}>Get Profile</button>
            </div>
        )
    }
}

export default ProfileHandler;