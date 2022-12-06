

import logo from './logo.svg';
import CodecareIcon from './Codecare.png';
import './App.css';
import MapIcon from './map.JPG';
import MessagesIcon from './messages.JPG';
import NotificationIcon from './notifications.JPG';
import OverviewIcon from './overview.JPG';
import PatientsIcon from './patients.JPG';
import SettingsIcon from './settings.JPG';
import React, {useState, useEffect, useRef} from 'react';
import Notification from './Notification';
import {Routes,Route,useNavigate} from 'react-router-dom';
import Details from './Details';
import Login from './Login';
import Register from './Register';
import Patient from './Patient';
import SpecificPatient from './SpecificPatient';

function App() {
  const [newData, setData] = useState(null);
  const notInitialRender = useRef(false);
  const navigate = useNavigate();
  return (
    <div>
      <Routes>
        <Route path = "/" element = {<Login/>}/>
        <Route  path="/details" element = {<Details/>} />
        <Route path ="/register" element={<Register/>}/>
        <Route path ="/patients" element={<Patient/>}/>
        <Route path ="/notification" element = {<Notification/>}/>
        <Route path ="/specificPatient" element={<SpecificPatient/>}/>
      </Routes>
    </div>
  );
}

export default App;
