import React, { Component } from 'react';
import * as Constants from './constants';


class RegisterHandler extends Component {

    state = {
        username: '',
        password: ''
    }

    register = () => {
        const { username, password } = this.state;
        
        // Send post request
        const registerUrl = `${Constants.BASE_URL}/register`;

        fetch(registerUrl, {
            method: 'POST',
            // mode: 'no-cors',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
            },
            body: new URLSearchParams({
                'email': username,
                'password': password,
                'name': 'testtestuser',
                'mobile_phone': 8148888477,
                'zipcode': 10026
            })
        })
        .then((res) => res)
        .then((data) => {
            if (data.status === 400) {
                alert(`ERROR: Somehow you cant register with email=${username}.`);
            } else if (data.status == 201) {
                alert(`Congrats! Successfully register with email=${username}.`);
            } else {
                alert('ERROR: Other(Invalid format).');
            }
        })
        .catch((err) => alert(`ERROR: Invalid username=${username}, err=${err}.`));

    }

    render() {
        return(
            <div>
                <h3>
                    Register Handler
                </h3>
                <input placeholder="email" onChange={(e) => this.setState({ username: e.target.value })}></input>
                <input placeholder="password(at least 8 characters)" onChange={(e) => this.setState({ password: e.target.value})}></input>
                <button onClick={this.register}>Register</button>
                
            </div>
        )
    }
}

export default RegisterHandler;
