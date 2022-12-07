import React,{useState,useEffect} from 'react';
import { useLocation } from 'react-router-dom';
import NavigationButton from './NavigationButton';

export default function SpecificPatient(props) {
    const {state} = useLocation();
    const [patientData, setPatientData] = useState(null);
    let provider = false;
    if(JSON.stringify(state.isPatient)==="0"){
        provider = true;
    }
    useEffect(() => {
        if(provider){
            fetch('/record/'+state.patient_id+"?token="+state.token)
            .then((response)=>response.json())
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
  return (
    <div>
        
        <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID} />
        
        {
            // Lines 31 till 34 are the top div only contaning the name of the patient.
        }
        {provider && state.ispatientData!== null &&<div>
            <h1>{state.patient_firstName} {state.patient_lastName}</h1>

        </div>}
        {
            // Lines 38 till 46 are the bottom div containing the city name and the state name of the visited cities.
        }
        <div>
            <h1>Location History</h1>
            <ul>
                {newData.map((location)=>(
                                <li>Visited City- {location.city} State - {location.state_id}</li>
                            ))
                }
            </ul>
        </div>
    </div>
  )
}
