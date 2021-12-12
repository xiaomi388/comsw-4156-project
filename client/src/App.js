import logo from './logo.svg';
import './App.css';

import RegisterHandler from './registerHandler';
import FurnitureHandler from './furnitureHandler.js';
import ProfileHandler from './profileHandler.js';
import LoginHandler from './loginHandler.js';
import SearchHandler from './searchHandler.js';
import BuyerHandler from './buyerHandler.js';


function App() {

  return (
    <div className="App">

      <RegisterHandler />
      <br />

      <LoginHandler />
      <br />

      <FurnitureHandler />
      <br />
      
      <ProfileHandler />
      <br />

      <SearchHandler />
      <br />

      <BuyerHandler />
      <br />

      {/* SellerConfirmHandler

      BuyerRatingHandler */}

    </div>
  );
}

export default App;
