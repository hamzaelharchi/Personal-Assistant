import './App.css';
import React from 'react';
import { Route, Routes , BrowserRouter as Router } from 'react-router-dom';

import { Navbar, Nav } from 'react-bootstrap'
import Login from './Components/Auth/Login'
import NotFound from './Components/Auth/NotFound'
import Register from './Components/Auth/Register'
import Dashboard from './Components/Auth/Dashboard' 


class App extends React.Component{

  render(){
    return(
      <Router id="root">
      <Navbar expand="lg"  bg="primary" variant="dark">
        <Navbar.Brand href="#home"> Personal Assistant</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
          <Nav.Link href='/login' onClick = {() => localStorage.clear()}>Logout</Nav.Link>
          <Nav.Link href='/login'>Login</Nav.Link>
          <Nav.Link href='/register'>Register</Nav.Link>
          </Nav>
          </Navbar.Collapse>
      </Navbar>

      <Routes >
        <Route exact path="/" element={<Login/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route element={<NotFound/>} />
      </Routes >
    </Router>     
    
    )
}
 
}


export default App;