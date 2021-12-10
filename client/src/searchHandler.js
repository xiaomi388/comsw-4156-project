

import React, { Component } from 'react';
import * as Constants from './constants';


class SearchHandler extends Component {

    state = {
        keyword: '',
        searchResult: ''
    }
    
    search = () => {
        // alert('search')

        const { keyword } = this.state;
        const getUserProfileUrl = `${Constants.BASE_URL}/furniture?keyword=${keyword}`;
        fetch(getUserProfileUrl)
        .then(response => response)
        .then((data) => {
            console.log("data: ", data);
            if (data.status === 200) {
                alert('Find some furniture!');
            } else {
                alert('No furniture found.');
            }
        })
        .catch((err) => console.log(err))
    }
    
    render() {
        return(
            <div>
                <h3>Search Handler</h3>
                <input placeholder="Enter keyword" onChange={(e) => this.setState({keyword: e.target.value})}></input>
                <button onClick={this.search}>Search Furniture</button>
            </div>
        )
    }
}

export default SearchHandler;