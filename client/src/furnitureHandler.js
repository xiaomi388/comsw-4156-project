import React, { Component } from 'react';

class FurnitureHandler extends Component {

    uploadFurniture = () => {
        alert("Upload furniture!");

        const postFurnitureUrl = 'http://localhost:5000/furnitures';
        const requestOptions = {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(
                {
                    "title": "test title",
                    "labels": "test labels",
                    "image_url": "test image url",
                    "description": "description"
                }
            )
        };
        fetch(postFurnitureUrl, requestOptions)
            .then(response => response.json())
            .then((data) => {
                console.log("post Furniture Data: ", data);
            })
            .catch((err) => console.log(err))

    }

    render() {
        return (
            <div>
                <h3>FurnitureHandler</h3>
                <input placeholder="title"></input>
                <input placeholder="labels"></input>
                <input placeholder="image_url"></input>
                <input placeholder="description"></input>
                <button onClick={this.uploadFurniture}>Upload Furniture</button>
            </div>
        )
    }
}

export default FurnitureHandler;



