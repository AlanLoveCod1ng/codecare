import logo from './logo.svg';
import CodecareIcon from './Codecare.png';
import './App.css';

function App() {
  return (
    
    <div className="App">
      <div className="App-box1">
        <img src={CodecareIcon} width="200" height="80"/>
        <h2> Box1</h2>
      </div>
      <div className="App-box2">
        <h2> Box2</h2>
      </div>
      <div className="App-box3">
        <h2> Box3</h2>
      </div>
    </div>
  );
}

export default App;
