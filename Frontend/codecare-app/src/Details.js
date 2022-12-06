import './App.css';
import React, {useState, useEffect} from 'react';
import Notification from './Notification';
import {useLocation,useNavigate,Redirect} from 'react-router-dom';
import HandleClick from './HandleClick';
import NavigationButton from './NavigationButton';

function Details() {
    const {state} = useLocation();
    const navigate = useNavigate();
    const[applicableData, setApplicableData] = useState(null);
    const[data , setData] = useState(null);
    const filter = "waiting";
    const first = "12"; 
    useEffect(() => {
        fetch('/notification?filter='+filter+"&first="+first+"&token="+state)
     .then((response)=>response.json())
     .then((apiData)=>{
      setApplicableData(apiData);
     })
    }, []);
    let trueNotification = null;
    let newVar = null;
    const dataPrinted = [];
    if (applicableData!==null){
      for (let i=0;i<applicableData.length;i++){
        dataPrinted.push(i);
      }
    }
    if (data !==null && applicableData!==null) {
        navigate('/notification',{state:{numberNotification:data,entireData:applicableData, token:state}})
    }

    
    return (
      
      <div className="App">
        {// following code is the left section line 62
          <div></div>
        }
        
        <NavigationButton state = {state}/>
         
        
        {// following code is the middle section lines 68 - 74
        }
        <div>
          {applicableData!==null && data === null && <div className="App-box2">
            
            <HandleClick updateNumber = {setData} number = {applicableData.length}/>
          </div>
          }
        </div>
        {// following code is the right section lines 76 - 82 
        }
      </div>
    );
  }
  
  export default Details;