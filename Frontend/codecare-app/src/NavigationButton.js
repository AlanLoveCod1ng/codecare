import MapIcon from './map.JPG';
import MessagesIcon from './messages.JPG';
import NotificationIcon from './notifications.JPG';
import OverviewIcon from './overview.JPG';
import PatientsIcon from './patients.JPG';
import SettingsIcon from './settings.JPG';
import CodecareIcon from './Codecare.png';
import './App.css'
import React from 'react'
import { useNavigate } from 'react-router-dom';

export default function NavigationButton(props) {
    const navigate=useNavigate();
  return (
    <div className="App-box1">
        <img src={CodecareIcon} width="200" height="80"/>
        <div className = "navButs">
        <button>
            <img src = {OverviewIcon} alt = "overview"/>
            Overview
        </button>
        <button onClick={()=>{navigate('/details',{state:props.state})}}>
            <img src = {NotificationIcon} alt = "notifications"/>
            Notifications
        </button>
        <button>
            <img src = {MessagesIcon} alt = "messages"/>
            Messages
        </button>
        <button>
            <img src = {MapIcon} alt = "map"/>
            Map
        </button>
        <button onClick={()=>{navigate('/patients',{state:props.state})}}>
            <img src = {PatientsIcon} alt = "patients"/>
            Patients
        </button>
        <button>
            <img src = {SettingsIcon} alt = "settings"/>
            Settings
        </button>
        </div>
            
          
    </div>
  )
}
