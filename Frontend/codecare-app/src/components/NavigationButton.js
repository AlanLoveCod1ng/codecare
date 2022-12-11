import CodecareIcon from '../static/Codecare.png';
import React from 'react'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome"
import { faHouse, faMap, faEnvelope, faGear, faMessage, faUser} from '@fortawesome/free-solid-svg-icons'
import { useLocation, useNavigate } from 'react-router-dom';
import {useState,useEffect} from 'react';

export default function NavigationButton(props) {
    const[userData, setUserData] = useState(0);
    const navigate=useNavigate();
    const {state} = useLocation();
    let url = null;
    if (JSON.stringify(props.isPatient)==='0'){
        url = '/patients'
    } else {
        url = '/specificPatient'
    }

    useEffect(() => {
        fetch('/account?token='+state.token)
        .then((response)=>{
            if(response.status === 403){
                navigate('/');
            }
            return response.json()})
            .then((availableData)=>{
                setUserData(availableData);
        })
        }, [props, state]);

  return (
    <div className="App-box1 vh-100 fixed-left">
        <div className='container'>
            <div className="row justify-content-center">
                <div className='col text-center'>
                    <img src={CodecareIcon} width="200" height="80"/>
                </div>
            </div>
        </div>
        
        <div className = "flex-column align-middle d-flex justify-content-center h-75 bg-light gap-4">

        <div className = "text-center">Welcome, {userData.first_name} {userData.last_name}!</div>

            <div className='row justify-content-center'>

                <button className="col-sm-7 btn border-0 btn-outline-success btn-md me-2 text-start" disabled>
                    <FontAwesomeIcon icon={faHouse} />
                    <span> Overview</span>
                </button>
            </div>
            <div className='row justify-content-center'>
                <button className= "col-sm-7 btn btn-outline-success me-2 border-0 btn-md text-start" onClick={()=>{navigate('/details',{state:{token:props.token, isPatient:props.isPatient, ID:props.ID}})}}>
                    <FontAwesomeIcon icon={faEnvelope} />  
                    <span> Notifications</span>
                </button>
            </div>
            
            <div className='row justify-content-center'>
                <button className= "col-sm-7 btn btn-outline-success me-2 border-0 btn-md text-start" disabled>
                    <FontAwesomeIcon icon={faMessage} />  
                    <span> Messages</span>
                </button>
            </div>
            
            <div className='row justify-content-center'>
                <button className= "col-sm-7 border-0 btn-md btn btn-outline-success me-2 text-start" disabled>
                    <FontAwesomeIcon icon={faMap} />
                    <span> Map</span>
                </button>
            </div>
            
            <div className='row justify-content-center'>
                <button className= "col-sm-7 border-0 btn-md btn btn-outline-success me-2 text-start" onClick={()=>{navigate(url,{state:{token:props.token, isPatient:props.isPatient, ID:props.ID}})}}>
                    <FontAwesomeIcon icon={faUser} />
                    <span> Patients</span>
                </button>
            </div>
            
            <div className='row justify-content-center'>
                <button className= "col-sm-7 border-0 btn-md btn btn-outline-success me-2 text-start" disabled>
                    <FontAwesomeIcon icon={faGear} />
                    <span> Settings</span>
                </button>
            </div>
            
        </div>
        
    </div>
  )
}