import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Form from 'react-bootstrap/Form';

function getResponse(email,password, navigate){
    let response = null;
     fetch('/login?email='+email+"&password="+password)
     .then((response)=>response.json())
     .then((apiData)=>{
        navigate('/details', {state:{token:apiData.token, isPatient:apiData.is_patient, ID:apiData.id}})
     })
     .catch((error)=>{
        return null;
     })
    
}

function Login () {
    const navigate = useNavigate();
    const[email, setEmail] = useState(null);
    const[password, setPassword] = useState(null);
    const[success, setSuccess] = useState(null);
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    function changeEmail(val) {
        setEmail(val.target.value);
    }
    function changePassword(val){
        setPassword(val.target.value);
    }
    function sendAPI(){
        let newVar = null;
        newVar = getResponse(email,password, navigate);
    }

    return (
        <div>
            <Button variant="primary" onClick={handleShow}>
                Login
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>
                        Nice to see you again
                        
                        <h1>
                            Welcome Back
                        </h1>
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <FloatingLabel
                        controlId="floatingInput"
                        label="Enter your username"
                        className="mb-3">
                            <Form.Control onChange={changeEmail} type="email" placeholder="name@example.com" />
                    </FloatingLabel>
                    <FloatingLabel 
                        controlId="floatingPassword" 
                        label="Enter your password">
                            <Form.Control onChange={changePassword} type="password" placeholder="Password" />
                    </FloatingLabel>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={()=>{navigate("/register")}}>
                        Register
                    </Button>
                    <Button variant="primary" onClick={sendAPI}>
                        Submit
                    </Button>
                </Modal.Footer>
            </Modal>
      </div>
    );
};

export default Login;