import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Form from 'react-bootstrap/Form';

function  getResponse(first,second,phone,state,email,password,navigate){
    let response = null;
     fetch('/register?first_name='+first+"&last_name="+second+"&email="+email+"&password="+password+"&phone="+phone+"&state="+state)
     .then(() =>{
        navigate('/');
     })
     .catch((error)=>{
        return null;
     })
    
}
export default function Register() {
    const navigate = useNavigate();
    const[first, setFirst] = useState(null);
    const[second, setSecond] = useState(null);
    const[phone, setPhone] = useState(null);
    const[state, setNewState] = useState(null);
    const[email, setEmail] = useState(null);
    const[password, setPassword] = useState(null);
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    function changeFirst(val) {
        setFirst(val.target.value);
    }
    function changeSecond(val) {
        setSecond(val.target.value);
    }
    function changePhone(val) {
        setPhone(val.target.value);
    }
    function changeState(val) {
        setNewState(val.target.value);
    }
    function changeEmail(val) {
        setEmail(val.target.value);
    }
    function changePassword(val){
        setPassword(val.target.value);
    }
    function sendAPI(){
        let newVar = null;
        newVar = getResponse(first,second,phone,state,email,password, navigate);
    }
  return (
    <div>
            <Button variant="primary" onClick={handleShow}>
                Register
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>
                        Thanks  for  choosing us
                        
                        <h1>
                            Create your account
                        </h1>
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <FloatingLabel
                        controlId="floatingFirstName"
                        label="Enter your first name"
                        className="mb-3">
                            <Form.Control onChange={changeFirst} type="firstName" placeholder="John" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingSecondName" 
                        label="Enter your second name"
                        className="mb-3">
                            <Form.Control onChange={changeSecond} type="lastName" placeholder="Doe" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingPhoneNumber" 
                        label="Enter your phone number"
                        className="mb-3">
                            <Form.Control onChange={changePhone} type="phoneNumber" placeholder="(123) 456 7890" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingState" 
                        label="Enter your state"
                        className="mb-3">
                            <Form.Control onChange={changeState} type="state" placeholder="Wisconsin" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingEmail" 
                        label="Enter your email"
                        className="mb-3">
                            <Form.Control onChange={changeEmail} type="email" placeholder="name@example.com" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingPassword" 
                        label="Enter your password"
                        className="mb-3">
                            <Form.Control onChange={changePassword} type="password" placeholder="password" />
                    </FloatingLabel>
                </Modal.Body>
                <Modal.Footer>
                <Button variant="secondary" onClick={()=>{navigate("/")}}>
                        Login
                    </Button>
                    <Button variant="primary">
                        Register
                    </Button>
                </Modal.Footer>
            </Modal>
    </div>
  )
}
