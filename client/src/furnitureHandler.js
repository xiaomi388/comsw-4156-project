import React, { Component } from 'react';
import * as Constants from './constants';


class FurnitureHandler extends Component {

    state = {
        title: '',
        labels: '',
        image_url: '',
        description: ''
    }

    uploadFurniture = () => {
        const { title, labels, image_url, description } = this.state;
        const postFurnitureUrl = `${Constants.BASE_URL}/furnitures`;

        fetch(postFurnitureUrl, {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': ['GET', 'POST'],
            },
            body: JSON.stringify({
                title: title,
                labels: labels,
                image_url: image_url,
                description: description
            })
        })
        .then(response => response)
        .then((data) => {
            console.log("post Furniture Data: ", data);
        })
        .catch((err) => console.log(err))
    }

    render() {
        return (
            <div>
                <h3>FurnitureHandler</h3> <p>(Cannot upload without login)</p>
                <input placeholder="title" onChange={(e) => this.setState({ title: e.target.value })}></input>
                <input placeholder="labels" onChange={(e) => this.setState({ labels: e.target.value })}></input>
                <input placeholder="image_url" onChange={(e) => this.setState({ image_url: e.target.value })}></input>
                <input placeholder="description" onChange={(e) => this.setState({ description: e.target.value })}></input>
                <button onClick={this.uploadFurniture}>Upload Furniture</button>
            </div>
        )
    }
}

export default FurnitureHandler;



