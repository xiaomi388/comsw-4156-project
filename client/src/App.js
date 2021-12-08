import logo from './logo.svg';
import './App.css';
import { useCookies } from "react-cookie";

import FurnitureHandler from './furnitureHandler.js';
import ProfileHandler from './profileHandler.js';


function App() {
  const [cookies, setCookie] = useCookies(["user"]);

  function handleCookie() {
    console.log("Set cookie user: ", "test0@columbia.edu");
    setCookie("user", "test0@columbia.edu", {
      path: "/"
    });
  }
  return (
    <div className="App">

      <button onClick={handleCookie}>set cookie</button>
      cookies.user: {cookies.user}


      <FurnitureHandler />
      <br />
      <ProfileHandler />

    </div>
  );
}

export default App;
