import React from 'react'

function HandleClick (props) {
    const clickedOn = (numberVar) =>{
        props.updateNumber(numberVar);
    };
    const newArr = [];
    for (let i =0; i<props.number;i++){
        newArr.push(i);
    }
    return (
        <div>
            <h1> Current Notifications </h1>
            <ul>
                {
                    newArr.map((individualData)=>(
                        <li onClick = {()=>clickedOn(individualData)}>Summary of Notification {individualData+1}</li>
                    ))
                }
            </ul>
        </div>
    );
};
export default HandleClick;