import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';

function  getResponse(email,password, navigate){
    let response = null;
     fetch('/login?email='+email+"&password="+password)
     .then((response)=>response.json())
     .then((apiData)=>{
        navigate('/details', {state:apiData.token})
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
            <form>
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
    );
};

export default Login;