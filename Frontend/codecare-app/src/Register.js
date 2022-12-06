import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';

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
        <form>
            <label>
                First Name:
                <input onChange={changeFirst} type="text" name="name" />
            </label>
            <label>
                Second Name:
                <input onChange={changeSecond} type="text" name="name" />
            </label>
            <label>
                PhoneNumber:
                <input onChange={changePhone} type="text" name="name" />
            </label>
            <label>
                State:
                <input onChange={changeState} type="text" name="name" />
            </label>
            <label>
                Email:
                <input onChange={changeEmail} type="text" name="name" />
            </label>
            <label>
                Password:
                <input onChange={changePassword} type="text" name="name"/>
            </label>
        </form>
        <br/>
        <button onClick={sendAPI} type="button">Submit</button>
    </div>
  )
}
