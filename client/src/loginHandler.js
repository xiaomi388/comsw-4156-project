import React, { Component } from 'react';
import * as Constants from './constants';


class LoginHandler extends Component {

    state = {
        email: '',
        password: ''
    }

    login = () => {
        const { email, password } = this.state;
        const loginUrl = `${Constants.BASE_URL}/user/login?email=${email}&password=${password}`;

        // Send get request
        fetch(loginUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST']
            },
            body: new URLSearchParams({
                email: email,
                password: password
            }),
            credentials: "include"
        })
        .then((res) => res)
        .then((data) => {
            console.log(data);
            console.log(data.status)
            if (data.status === 400) {
                alert(`ERROR: Fail to login, email=${email}.`);
            } else if (data.status == 200) {
                alert(`Yeah! Login in successfully with email=${email}`);
            } else {
                alert('ERROR: Invalid Credentials.');
            }
        })
        .catch((err) => alert(`ERROR: Fail to login, email=${email}, err=${err}.`));
    }

    logout = () => {
        const logoutUrl = `${Constants.BASE_URL}/user/logout`;
        fetch(logoutUrl)
        .then((res) => res) 
        .then((data) => {
            alert('Logout!');
        })
    }

    render() {
        return(

            <div>
                <h3>
                    Login Handler
                </h3>
                <input placeholder="email" onChange={(e) => this.setState({ email: e.target.value })}></input>
                <input placeholder="password" onChange={(e) => this.setState({ password: e.target.value})}></input>
                <button onClick={this.login}>Log In</button>
                <button onClick={this.logout}>Log Out</button>
            </div>
        )
    }
}

export default LoginHandler;
