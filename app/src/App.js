import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Navigation from './Navigation.js';
import { Container } from 'reactstrap';

class App extends Component {
  render() {
    return (
      <Container fluid='true'>
        <Navigation/>
        <header>Kiroku</header>
      </Container>
    );
  }
}

export default App;
