import React,{useState,useEffect} from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import NavigationButton from './NavigationButton';
import SpecificPatient from './SpecificPatient';


export default function Patient(props) {
    const navigate = useNavigate();
    const {state} = useLocation();
    const[patientData, setPatientData] = useState(null);
    const [locationData, setLocationData] = useState(null);
    useEffect(() => {
        if(JSON.stringify(state.isPatient)===0){
          fetch('/patients?token='+state.token)
          .then((response)=>response.json())
          .then((availableData)=>{
          setPatientData(availableData);
          })
        }
      },[]);
      function handleClick(patient){
        navigate('/specificPatient',{state:{ID: state.ID, isPatient: state.isPatient,token:state.token,patient_id:patient.patient_id, patient_firstName: patient.first_name, patient_lastName: patient.last_name }})
      }
      const patientDetails = []
      if(patientData!==null){
        for(let i =0;i<patientData.length;i++){
            patientDetails.push(patientData[i]);
        }
        
      }
      let provider = false;
      if(JSON.stringify(state.isPatient)==="0"){
        provider = true;
      }
      if (provider === false){
        console.log("Reached here");
        navigate('/specificPatient',{state:{ID:state.ID, token:state.token, isPatient:state.isPatient}})
      }
      
  return (
    <div>
        {//Line 22 is the left side nav bar.
        <></>}
        
         <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID}/>
        
        {//Lines 43-51 are if a provider accesses patients details.
        }
        {provider && <div>
            <h1>Patient Details</h1>
                <ul>
                        {patientDetails.map((patient)=>(
                            <li onClick = {()=>handleClick(patient)}>Summary of Patient {patient.first_name}</li>
                        ))
                        }
                </ul>
        </div>}
           
    </div>
  )
}
