import React, { Component } from 'react';

class ProfileHandler extends Component {
    
    getUserProfile = () => {
        alert("Get user profile");

        const getUserProfileUrl = 'http://localhost:5000/profile';
        const requestOptions = {
            method: 'GET',
            mode: 'no-cors',
            headers: { 
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'cookie': "test0@columbia.edu"
            },
        };
        fetch(getUserProfileUrl, requestOptions)
            .then(response => response.json())
            .then((data) => {
                console.log("get user profile data: ", data);
            })
            .catch((err) => console.log(err))
    }
    
    render() {
        document.cookie = "email='test0@columbia.edu'";
        return(
            <div>
                <h3>Profile Handler</h3>

                <button onClick={this.getUserProfile}>Get Profile</button>
            </div>
        )
    }
}

export default ProfileHandler;