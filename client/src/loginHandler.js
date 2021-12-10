import React, { Component } from 'react';

class LoginHandler extends Component {

    state = {
        username: '',
        password: ''
    }

    login = () => {
        const { username, password } = this.state;
        alert(`log in! username:${username}, password:${password}`);
        
        // Send get request
        const loginUrl = 'http://localhost:5000/login';
        const requestOptions = {
            method: 'GET',
            mode: 'no-cors',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
            },
        };


        fetch(loginUrl, requestOptions)
            // method: 'GET',
            // mode: 'no-cors',
            // headers: {
            //     'Access-Control-Allow-Origin': '*',
            //     'Access-Control-Allow-Methods': ['GET', 'POST'],
            // },
            // body: new URLSearchParams({
            //     'email': username,
            //     'password': password
            //     // 'name': 'testtestuser',
            //     // 'mobile_phone': 8148888477,
            //     // 'zipcode': 10026
            // })

        .then((req) => req.json())
        .then((data) => {
            console.log("data: ", data);
        })
        .catch((err) => alert(`ERROR: Invalid username=${username}, err=${err}.`));

    }

    render() {
        return(

            <div>
                <h3>
                    Login Handler
                </h3>
                <input placeholder="username" onChange={(e) => this.setState({ username: e.target.value })}></input>
                <input placeholder="password" onChange={(e) => this.setState({ password: e.target.value})}></input>
                <button onClick={this.login}>Log In</button>
                
            </div>
        )
    }
}

export default LoginHandler;
