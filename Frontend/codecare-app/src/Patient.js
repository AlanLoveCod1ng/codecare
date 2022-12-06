import React,{useState,useEffect} from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import NavigationButton from './NavigationButton';
import SpecificPatient from './SpecificPatient';


export default function Patient(props) {
    const navigate = useNavigate();
    const {state} = useLocation();
    const[patientData, setPatientData] = useState(null);
    useEffect(() => {
        fetch('/patients?token='+state)
        .then((response)=>response.json())
        .then((availableData)=>{
          setPatientData(availableData);
        })
      },[]);
      function handleClick(patient){
        navigate('/specificPatient',{state:{token:state,patient_id:patient.patient_id, patient_firstName: patient.first_name, patient_lastName: patient.last_name }})
      }
      const patientDetails = []
      if(patientData!==null){
        for(let i =0;i<patientData.length;i++){
            patientDetails.push(patientData[i]);
        }
        
      }
  return (
    <div>
        {//Line 22 is the left side nav bar.
        <></>}
        
         <NavigationButton state = {state}/>
        
        
        <div>
            <h1>Patient Details</h1>
                <ul>
                        {patientDetails.map((patient)=>(
                            <li onClick = {()=>handleClick(patient)}>Summary of Patient {patient.first_name}</li>
                        ))
                        }
                </ul>
        </div>    
    </div>
  )
}
