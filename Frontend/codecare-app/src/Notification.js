import React from 'react'
import './Notification.css';
export default function Notification(props) {
  return (
    <div className='Notification'>
        <div className='Box1'>
            <h1>Summary and Title of the Selected Notification {props.data}</h1>
            <br></br>
            <h2>Placeholder Data</h2>
        </div>
        <div className='Box2'>
            <h1>Preview of the message to be sent</h1>
            <br></br>
            <h2>Placeholder Data</h2>
        </div>
        <div className='Box3'>
            <h1>Susceptible Patients</h1>
            <br></br>
            <h2>Placeholder Data</h2>
        </div>
    </div>
  )
}
