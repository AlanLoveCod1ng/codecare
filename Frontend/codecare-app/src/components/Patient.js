import React,{useState,useEffect} from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import NavigationButton from './NavigationButton';
import SpecificPatient from './SpecificPatient';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import ListGroupItem from 'react-bootstrap/esm/ListGroupItem';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

export default function Patient(props) {
    const navigate = useNavigate();
    const {state} = useLocation();
    const[patientData, setPatientData] = useState(null);
    const [locationData, setLocationData] = useState(null);
    useEffect(() => {
        if(JSON.stringify(state.isPatient)==='0'){
          fetch('/patients?token='+state.token)
          .then((response)=>{
            if(response.status === 403){
              navigate('/');
            }
            return response.json()})
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
      console.log(patientData)
  return (
    <div className='row gap-2'>
      <div className='col-2 bg-light vh-100'>
        {//Line 22 is the left side nav bar.
        <></>}
        
         <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID} firstName = {state.first_name} lastName = {state.last_name}/>
         </div>

         <div className='col-8 bg-light'>
        {//Lines 43-51 are if a provider accesses patients details.
        }
        {provider && <div>
            <h1>Patient Details</h1>
                  <Row xs={1} md={3} className="gap-2">
                        {patientDetails.map((patient)=>(
                            <Card onClick = {()=>handleClick(patient)}>
                              <Card.Img variant="top" src="https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png" />
                              <Card.Title>Summary of {patient.first_name} {patient.last_name}</Card.Title>
                              <Card.Text>
                                Email: {patient.email} <br></br>
                                Phone Number: {patient.phone}
                              </Card.Text>
                            </Card>
                        ))
                        }
                  </Row>
        </div>}
        </div>
           
    </div>
  )
}
