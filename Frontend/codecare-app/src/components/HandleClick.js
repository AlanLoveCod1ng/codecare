import React from 'react'
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import ListGroup from 'react-bootstrap/ListGroup';

function HandleClick (props) {
    const newArr = [];

    const clickedOn = (numberVar) =>{
        props.updateNumber(numberVar);
    };
    
    for (let i =0; i<props.number;i++){
        newArr.push(i);
    }

    return (
        <div>
                <ListGroup>
                    {
                        newArr.map((individualData) => (
                            <ListGroup.Item action onClick={()=>clickedOn(individualData)}>Notification {individualData + 1}</ListGroup.Item>
                        ))
                    }
                </ListGroup>
        </div>
    );
};
export default HandleClick;