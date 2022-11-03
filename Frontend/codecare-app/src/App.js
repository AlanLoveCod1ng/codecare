import CodecareIcon from './Codecare.png';
import './App.css';

function App() {
  return (
    <div className = "Notifications">
      <div className="App-logo">
            <img src={CodecareIcon} width="200" height="80" alt = "logo"/>
      </div>
      <div className = "lowerContainer">
        <div className= "leftInnerContainer">
          <div className = "navButs">
            <button>
              <img src = "navButImg/overview.JPG" alt = "overview"/>
              Overview
            </button>
            <button>
              <img src = "navButImg/notifications.JPG" alt = "notifications"/>
              Notifications
            </button>
            <button>
              <img src = "navButImg/messages.JPG" alt = "messages"/>
              Messages
            </button>
            <button>
              <img src = "navButImg/map.JPG" alt = "map"/>
              Map
            </button>
            <button>
              <img src = "navButImg/patients.JPG" alt = "patients"/>
              Patients
            </button>
            <button>
              <img src = "navButImg/settings.JPG" alt = "settings"/>
              Settings
            </button>
          </div>
        </div>
        <div className="App-box2">
          <h2> Box2</h2>
        </div>
        <div className="App-box3">
          <h2> Box3</h2>
        </div>
      </div>
    </div>
  );
}

export default App;
