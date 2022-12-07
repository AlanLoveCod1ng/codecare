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
    const [latitude,setLatitude] = useState(null);
    const [longitude,setLongitude] = useState(null);
    const filter = "waiting";
    const first = "12"; 
    console.log("Patient is "+state.isPatient);
    

    useEffect(() => {
        fetch('/notification?filter='+filter+"&first="+first+"&token="+state.token)
     .then((response)=>{
        if(response.status===403){
          navigate('/');
        }
        return response.json()
      })
     .then((apiData)=>{
      setApplicableData(apiData);
     })
    }, []);
    useEffect(()=>{
      if (JSON.stringify(state.isPatient)==="1"){
        navigator.geolocation.getCurrentPosition((position)=>{
          setLatitude(position.coords.latitude);
          setLongitude(position.coords.longitude);
        })
    
        console.log("New Date is "+newDate);
        console.log("New Time is "+timePrint);
      }
    });
    const today = new Date();
    let monthPrint,datePrint;
    const month = today.getMonth()+1;
    const year = today.getFullYear();
    const date = today.getDate();
    if(month < 10){
      monthPrint = "0"+month;
    } else{
      monthPrint = ""+month;
    }
    if(date < 10){
      datePrint = "0"+date;
    } else{
      datePrint = ""+date;
    }
    const yearPrint = ""+year;
    const newDate = yearPrint+"-"+monthPrint+"-"+datePrint;
    const hours = today.getHours();
    const minutes = today.getMinutes();
    const seconds = today.getSeconds();
    let hourPrint,minutePrint,secondPrint;
    if(hours<10){
      hourPrint = "0"+hours;
    } else {
      hourPrint = ""+hours;
    }
    if(minutes <10){
      minutePrint = "0"+minutes;
    } else{
      minutePrint = ""+minutes;
    }
    if(seconds <10){
      secondPrint = "0"+minutes;
    } else{
      secondPrint = ""+minutes;
    }
    const timePrint = hourPrint+":"+minutePrint+":"+secondPrint;
   
    useEffect (()=>{
      if (latitude!==null && longitude!==null){
          fetch('/new_record?lat='+latitude+'&lon='+longitude+'&datetime='+newDate+'+'+timePrint+"?token="+state.token)
          .then((response)=>{
            if(response.status===403){
              navigate('/');
            }
          })
        }
    },[latitude,longitude])
    let trueNotification = null;
    let newVar = null;
    const dataPrinted = [];
    if (applicableData!==null){
      for (let i=0;i<applicableData.length;i++){
        dataPrinted.push(i);
      }
    }
    if (data !==null && applicableData!==null) {
        navigate('/notification',{state:{numberNotification:data,entireData:applicableData, token:state.token, isPatient:state.isPatient, ID:state.ID}})
    }

    
    return (
      
      <div className="App">
        <div className='container-fluid'>
          <div className='row'>
            {// following code is the left section line 62
            <div></div>
            }
            
            <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID}/>
            
            
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
        </div>
        
      </div>
    );
  }
  
  export default Details;