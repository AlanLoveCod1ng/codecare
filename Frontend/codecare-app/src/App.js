import logo from './static/logo.svg';
import CodecareIcon from './static/Codecare.png';
import MapIcon from './static/map.JPG';
import MessagesIcon from './static/messages.JPG';
import NotificationIcon from './static/notifications.JPG';
import OverviewIcon from './static/overview.JPG';
import PatientsIcon from './static/patients.JPG';
import SettingsIcon from './static/settings.JPG';
import React, {useState, useEffect, useRef} from 'react';
import Notification from './components/Notification';
import {Routes,Route,useNavigate} from 'react-router-dom';
import Details from './components/Details';
import Login from './components/Login';
import Register from './components/Register';
import Patient from './components/Patient';
import SpecificPatient from './components/SpecificPatient';

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
