import CodecareIcon from './Codecare.png';
import './App.css';
import MapIcon from './map.JPG';
import MessagesIcon from './messages.JPG';
import NotificationIcon from './notifications.JPG';
import OverviewIcon from './overview.JPG';
import PatientsIcon from './patients.JPG';
import SettingsIcon from './settings.JPG';
import React, {useState, useEffect} from 'react';
import Notification from './Notification';



function App() {

  const[Box3,setBox3] = useState(false);
  const[Box2, setBox2] = useState(true);
  let[data, setData] = useState(null);
  const handleClick = (newData,Box2,Box3) => {
    setBox2(Box2 = false)
    setBox3(Box3 = true)
    setData(data = newData)
  }

  return (
    
    <div className="App">
      <div className="App-box1">
        <img src={CodecareIcon} width="200" height="80"/>
        <div className = "lowerContainer">
        <div className= "leftInnerContainer">
          <div className = "navButs">
            <button>
              <img src = {OverviewIcon} alt = "overview"/>
              Overview
            </button>
            <button>
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
            <button>
              <img src = {PatientsIcon} alt = "patients"/>
              Patients
            </button>
            <button>
              <img src = {SettingsIcon} alt = "settings"/>
              Settings
            </button>
          </div>
        </div>
      </div>
      </div>
        {Box2 && <div className="App-box2">
          <h1> Current Notifications</h1>
          <br></br>
          <ul>
            <li onClick = {()=>handleClick(1,Box3,Box2)}>Summary of the Notification 1</li>
            <br></br>
            <li onClick = {()=>handleClick(2,Box3,Box2)}>Summary of the Notification 2</li>
            <br></br>
            <li onClick = {()=>handleClick(3,Box3,Box2)}>Summary of the Notification 3</li>
            <br></br>
            <li onClick = {()=>handleClick(4,Box3,Box2)}>Summary of the Notification 4</li>
            <br></br>
            <li onClick = {()=>handleClick(5,Box3,Box2)}>Summary of the Notification 5</li>
            <br></br>
            <li onClick = {()=>handleClick(6,Box3,Box2)}>Summary of the Notification 6</li>
            <br></br>
            <li onClick = {()=>handleClick(7,Box3,Box2)}>Summary of the Notification 7</li>
            <br></br>
            <li onClick = {()=>handleClick(8,Box3,Box2)}>Summary of the Notification 8</li>
            <br></br>
            <li onClick = {()=>handleClick(9,Box3,Box2)}>Summary of the Notification 9</li>
            <br></br>
            <li onClick = {()=>handleClick(10,Box3,Box2)}>Summary of the Notification 10</li>
            <br></br>
            <li onClick = {()=>handleClick(11,Box3,Box2)}>Summary of the Notification 11</li>
            <br></br>
            <li onClick = {()=>handleClick(12,Box3,Box2)}>Summary of the Notification 12</li>
            <br></br>
          </ul>
        </div>
      }
      {!Box2 && <Notification data = {data}/> }
      {Box3 &&<div className="App-box3">
            <h1> Current Notifications</h1>
            <ul>
            <li onClick = {()=>handleClick(1,Box3,Box2)}>Summary of the Notification 1</li>
            <br></br>
            <li onClick = {()=>handleClick(2,Box3,Box2)}>Summary of the Notification 2</li>
            <br></br>
            <li onClick = {()=>handleClick(3,Box3,Box2)}>Summary of the Notification 3</li>
            <br></br>
            <li onClick = {()=>handleClick(4,Box3,Box2)}>Summary of the Notification 4</li>
            <br></br>
            <li onClick = {()=>handleClick(5,Box3,Box2)}>Summary of the Notification 5</li>
            <br></br>
            <li onClick = {()=>handleClick(6,Box3,Box2)}>Summary of the Notification 6</li>
            <br></br>
            <li onClick = {()=>handleClick(7,Box3,Box2)}>Summary of the Notification 7</li>
            <br></br>
            <li onClick = {()=>handleClick(8,Box3,Box2)}>Summary of the Notification 8</li>
            <br></br>
            <li onClick = {()=>handleClick(9,Box3,Box2)}>Summary of the Notification 9</li>
            <br></br>
            <li onClick = {()=>handleClick(10,Box3,Box2)}>Summary of the Notification 10</li>
            <br></br>
            <li onClick = {()=>handleClick(11,Box3,Box2)}>Summary of the Notification 11</li>
            <br></br>
            <li onClick = {()=>handleClick(12,Box3,Box2)}>Summary of the Notification 12</li>
            <br></br>
          </ul>
        </div>
      }
    </div>
  );
}

export default App;
