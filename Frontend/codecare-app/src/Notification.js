import React from 'react'
import './Notification.css';
const Notification = (props) => {
  console.log("Hi nishit"+props.data);
  return (
    <div className='Notification'>
        <div className='Box1'>
            <h1>Summary and Title of the Selected Notification {props.data.data}</h1>
            <br></br>
            <h2>Placeholder Data</h2>
        </div>
        <div className='Box2'>
            <h1>Preview of the message to be sent</h1>
            <br></br>
            <p>{props.newVar}</p>
        </div>
        <div className='Box3'>
            <h1>Susceptible Patients</h1>
            <br></br>
            <h2>Placeholder Data</h2>
        </div>
    </div>
  )
};
export default Notification;
