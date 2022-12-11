import React,{useState,useEffect} from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import NavigationButton from './NavigationButton';




export default function SpecificPatient(props) {
    const navigate = useNavigate();
    const {state} = useLocation();
    const [patientData, setPatientData] = useState(null);
    
    let provider = false;
    if(JSON.stringify(state.isPatient)==="0"){
        provider = true;
    }
    useEffect(() => {
        if(provider){
            fetch('/record/'+state.patient_id+"?token="+state.token)
            .then((response)=>{
                if(response.status===403){
                    navigate('/');
                }
                return response.json()})
            .then((availableData)=>{
              setPatientData(availableData);
            })
        } else{
            fetch('/record/'+state.ID+"?token="+state.token)
            .then((response)=>response.json())
            .then((availableData)=>{
                setPatientData(availableData);
                console.log(availableData);
            })
        }
      },[]);
      const newData = []
      if (patientData!==null){
        for(let i =0;i<patientData.length;i++){
            newData.push(patientData[i]);
        }
      }
      const [mapMarker, setMapMarker] = useState(null)
      const [called , setCalled] = useState(0)
      useEffect(()=>{
        if(newData.length!==0 && called === 0){
            setMapMarker(newData[0])
            setCalled(1)
        }
      })
    function onClickHandle(location){
        setMapMarker(location)
    }
  return (
    <div className='row'>
        <div className='col-2 bg-light vh-100'>
        <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID} firstName = {state.first_name} lastName = {state.last_name}/>
        </div>
        {
            // Lines 31 till 34 are the top div only contaning the name of the patient.
        }
        <div className='col-6'>
            {provider && state.ispatientData!== null &&<div>
                <h1>{state.patient_firstName} {state.patient_lastName}</h1>

            </div>}
            
            {
                // Lines 38 till 46 are the bottom div containing the city name and the state name of the visited cities.
            }
            <div>
                <h1>Location History</h1>
                <div className='row gy-3'>
                {newData.map((location)=>(
                                <div className='col-lg-6 col-sm-12 gap-0'>
                                    <div className="card" style={{width: '9 rem'}}>
                                        <div className="card-body">
                                            <h5 className="card-title">Location Record</h5>
                                        </div>
                                        <ul className="list-group list-group-flush">
                                            <li className="list-group-item">City: {location.city}</li>
                                            <li className="list-group-item">State: {location.state_id}</li>
                                            <li className="list-group-item">Time: {location.datetime}</li>
                                            <li className="list-group-item">Latitude: {location.latitude}</li>
                                            <li className="list-group-item">Latitude: {location.longitude}</li>
                                        </ul>
                                        <div className='card-body'>
                                            <button onClick={()=>onClickHandle(location)} className="btn btn-primary">Show on Map</button>
                                        </div>
                                    </div>
                                </div>
                            ))
                }
                </div>
                
            </div>
        </div>
        <div className='col-4'>
            {mapMarker!==null&&<GetMap mapMarker = {mapMarker} setMapMarker = {setMapMarker} default = {newData[0]}/>}
        </div>
    </div>
  )
}



function GetMap(props){
    console.log(props)
    let mapSrc = "https://www.google.com/maps/embed/v1/place?key=AIzaSyA1yZohw-dUXrCAZ4VMcyO0zlpYx_7Pw6Q&q="+props.mapMarker.latitude+","+props.mapMarker.longitude
    return (
        <iframe
            width="450"
            height="80%"
            // frameborder="0" style="border:0"
            // referrerpolicy="no-referrer-when-downgrade"
            src={mapSrc}
            allowFullScreen>
        </iframe>
    )
    
}