import React from 'react';
import logo from './logo.svg';
import './App.css';
import Main from './components/Main/Main';

import { Switch, Route, BrowserRouter as Router, Redirect, HashRouter } from 'react-router-dom';


function App() {
  return (
    <div className='app'>
    <HashRouter basename="/">
      <Switch>
        <Route exact path="/" component={ Main }/>
      </Switch>
    </HashRouter>
  </div>
  );
}

export default App;
