import React from 'react'
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';

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
                <Row xs={1} md={1} className = "gap-1">
                    {
                        newArr.map((individualData)=>(
                                <Button onClick = {()=>clickedOn(individualData)}>Notification {individualData+1}</Button>
                        ))
                    }
                </Row>
        </div>
    );
};
export default HandleClick;