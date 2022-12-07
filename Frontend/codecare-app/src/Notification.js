import React,{useState,useEffect} from 'react';
import NavigationButton from './NavigationButton';
import { useLocation,useNavigate } from 'react-router-dom';
import './Notification.css';
import HandleClick from './HandleClick';
function Notification (props) {
  const{state} = useLocation();
  const navigate = useNavigate();
  const[data,setData] = useState(state.numberNotification);
  const[apiAccept,setApiAccept] = useState(null);
  const[apiDecline,setApiDecline] = useState(null);
  useEffect(() => {
    if(apiAccept!==null){
      fetch('/send/'+apiAccept+'?token='+state.token)
      .then(()=>{
        navigate('/details',{state:{token:state.token, isPatient:state.isPatient, ID:state.ID}})
      })
    }
  }, [apiAccept]);
  useEffect(() => {
    if(apiDecline!==null){
      fetch('/send/'+apiDecline+'?token='+state.token)
      .then(()=>{
        navigate('/details',{state:{token:state.token, isPatient:state.isPatient, ID:state.ID}})
      })
    }
  }, [apiDecline]);
  
  let provider = false;
  if (JSON.stringify(state.isPatient) === '0'){
    console.log("Found a provider");
    provider = true;
  }
  //console.log(state.entireData);
  return (
    <div>
      {
         <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID}/>
      }
      {// Lines 18-34 are middle part of the notification. 
      }
      <div className='Notification'>
          <div className='Box1'>
              <h1>Summary and Title of the Selected Notification {data+1} </h1>
              <br></br>
              <h2>Placeholder Data</h2>
          </div>
          <div className='Box2'>
              {provider && <h1>Preview of the message to be sent</h1>}
              {provider===false && <h1>Notification Received</h1>}
              <br></br>
              <p>{JSON.stringify(state.entireData[data].content)}</p>
              {provider && <div>
                <button onClick={()=>setApiAccept(state.entireData[data].notification_id)} type='button'>Send Notification</button>
                <button onClick={()=>setApiDecline(state.entireData[data].notification_id)} type='button'>Reject Notification</button>
              </div>}
          </div>
          {provider && <div className='Box3'>
              <h1>Susceptible Patients</h1>
              <br></br>
              <h2>Placeholder Data</h2>
          </div>}
      </div>
      {// Lines 37-39 are the right portion of the notification tab.
      }
      <div>
        <HandleClick updateNumber = {setData} number = {state.entireData.length}/>
      </div>
    </div>
  )
};
export default Notification;
