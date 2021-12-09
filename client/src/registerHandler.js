import React, { Component } from 'react';

class RegisterHandler extends Component {

    state = {
        username: '',
        password: ''
    }

    register = () => {
        const { username, password } = this.state;
        alert(`register! username:${username}, password:${password}`);
        
        // Send post request
        const registerUrl = 'http://localhost:5000/register';

        fetch(registerUrl, {
            method: 'POST',
            mode: 'no-cors',
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
            console.log("data: ", data);
        })
        .catch((err) => alert(`ERROR: Invalid username=${username}, err=${err}.`));

    }

    render() {
        return(
            <div>
                <h3>
                    Register Handler
                </h3>
                <input placeholder="username" onChange={(e) => this.setState({ username: e.target.value })}></input>
                <input placeholder="password" onChange={(e) => this.setState({ password: e.target.value})}></input>
                <button onClick={this.register}>Register</button>
                
            </div>
        )
    }
}

export default RegisterHandler;
