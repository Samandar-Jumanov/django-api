import './App.css';
import axios from 'axios'
import React, {useState, useEffect} from 'react'
function App() {
  let url ='http://localhost:3002/challanges/'
   const [data, setData] = useState([]);
  useEffect(() => {
    axios.get(url)
      .then(response => setData(response.data))
      .catch(error => console.log(error));
  }, []);
  return (
    <div className="App">
      {data.map(item => (
        <p>{item.name}</p>
      ))}
    </div>
  );
}

export default App;
