import CodecareIcon from '../static/Codecare.png';
import React from 'react'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome"
import { faHouse, faMap, faEnvelope, faGear, faMessage, faUser} from '@fortawesome/free-solid-svg-icons'
import { useNavigate } from 'react-router-dom';

export default function NavigationButton(props) {
    const navigate=useNavigate();
    let url = null;
    console.log(props.isPatient);
    if (JSON.stringify(props.isPatient)==='0'){
        url = '/patients'
    } else {
        url = '/specificPatient'
    }
  return (
    <div className="App-box1 col-3">
        <div className='container'>
            <div className="row justify-content-center">
                <div className='col text-center'>
                    <img src={CodecareIcon} width="200" height="80"/>
                </div>
            </div>
        </div>
        
        
        <div className = "flex-column align-middle d-flex justify-content-center h-75 gap-4">
            <div className='row justify-content-center'>
                <a className="col-sm-6 btn btn-outline-success me-2">
                    <FontAwesomeIcon icon={faHouse} />
                    <span> Overview</span>
                </a>
            </div>
            <div className='row justify-content-center'>
                <a className= "col-sm-6 btn btn-outline-success me-2" onClick={()=>{navigate('/details',{state:{token:props.token, isPatient:props.isPatient, ID:props.ID}})}}>
                    <FontAwesomeIcon icon={faEnvelope} />  
                    <span> Notifications</span>
                </a>
            </div>
            
            <div className='row justify-content-center'>
                <a className= "col-sm-6 btn btn-outline-success me-2">
                    <FontAwesomeIcon icon={faMessage} />  
                    <span> Messages</span>
                </a>
            </div>
            
            <div className='row justify-content-center'>
                <a className= "col-sm-6 btn btn-outline-success me-2">
                    <FontAwesomeIcon icon={faMap} />
                    <span> Map</span>
                </a>
            </div>
            
            <div className='row justify-content-center'>
                <a className= "col-sm-6 btn btn-outline-success me-2" onClick={()=>{navigate(url,{state:{token:props.token, isPatient:props.isPatient, ID:props.ID}})}}>
                    <FontAwesomeIcon icon={faUser} />
                    <span> Patients</span>
                </a>
            </div>
            
            <div className='row justify-content-center'>
                <a className= "col-sm-6 btn btn-outline-success me-2">
                    <FontAwesomeIcon icon={faGear} />
                    <span> Settings</span>
                </a>
            </div>
            
        </div>
        
    </div>
  )
}
