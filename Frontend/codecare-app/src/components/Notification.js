import React,{useState,useEffect} from 'react';
import NavigationButton from './NavigationButton';
import { useLocation,useNavigate } from 'react-router-dom';
import HandleClick from './HandleClick';
import Accordion from 'react-bootstrap/Accordion';
import AccordionBody from 'react-bootstrap/esm/AccordionBody';

function Notification (props) {
  const{state} = useLocation();
  const navigate = useNavigate();
  const[data,setData] = useState(state.numberNotification);
  const[apiAccept,setApiAccept] = useState(null);
  const[apiDecline,setApiDecline] = useState(null);

  useEffect(() => {
    if(apiAccept!==null){
      fetch('/send/'+apiAccept+'?token='+state.token)
      .then((response)=>{
        if(response.status===201){
          alert("Notification Sent Successfully");
        }
        
        if(response.status===403){
          navigate('/');
        }
        navigate('/details',{state:{token:state.token, isPatient:state.isPatient, ID:state.ID}})
      })
    }
  }, [apiAccept]);
  useEffect(() => {
    if(apiDecline!==null){
      fetch('/send/'+apiDecline+'?token='+state.token)
      .then((response)=>{
        if(response.status===201){
          alert("Notification Denied Successfully");
        }
        if(response.status===403){
          navigate('/');
        }
        navigate('/details',{state:{token:state.token, isPatient:state.isPatient, ID:state.ID}})
      })
    }
  }, [apiDecline]);

  let provider = false;
  if (JSON.stringify(state.isPatient) === '0'){
    console.log("Found a provider");
    provider = true;
  }
  return (
    <div className='row'>
      <div className='col-2 bg-light vh-100'>
      {
         <NavigationButton token = {state.token} isPatient = {state.isPatient} ID = {state.ID} firstName = {state.first_name} lastName = {state.last_name}/>
      }
      </div>
      <div className='col-10'>
        <div className='row gap-4'>
          <h1>Current Notifications</h1>
        </div>
        <div className = 'row'>
        <div className='col-10'>
          <Accordion defaultActiveKey="0" flush>
            <div>
              <div>
                <Accordion.Item eventKey="0">
                  <Accordion.Header>
                    <h1>
                      {JSON.parse(JSON.stringify(state.entireData[data].title))}
                    </h1>
                  </Accordion.Header>
                  <br></br>
                  <AccordionBody>
                    <h3>
                      Summary of Notification
                    </h3>
                  </AccordionBody>
                </Accordion.Item>
              </div>
              <div>
                <Accordion.Item eventKey="1">
                  <Accordion.Header>
                    {provider && <h1>Preview of the message to be sent</h1>}
                    {provider===false && <h1>Notification Received</h1>}
                  </Accordion.Header>
                  <AccordionBody>
                    
                    <br></br>
                    <p>{JSON.parse(JSON.stringify(state.entireData[data].content))}</p>
                    
                    {provider && <div>
                      <button onClick={()=>setApiAccept(state.entireData[data].notification_id)} type='button'>Send Notification</button>
                      <button onClick={()=>setApiDecline(state.entireData[data].notification_id)} type='button'>Reject Notification</button>
                    </div>}
                  </AccordionBody>
                </Accordion.Item>
              </div>
              <Accordion.Item eventKey="2">
              {provider && <div className='Box3'>
                <Accordion.Header>
                  <h1>Susceptible Patients</h1>
                </Accordion.Header>
                  <br></br>
                <AccordionBody>
                  <h3>Placeholder Data</h3>
                </AccordionBody>
              </div>}
              </Accordion.Item>
            </div>
          </Accordion>
        </div>

        <div className='col-2'>
          <HandleClick updateNumber = {setData} number = {state.entireData.length} data = {data} notifs = {state.entireData}/>
        </div>
      </div> 
      </div>
    </div>
  )
};
export default Notification;