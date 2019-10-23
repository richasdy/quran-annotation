import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person'

class App extends Component {

  state = {
    persons: [
      {
        name: "Hafiz",
        age: "220"
      }
    ],
    otherState: "Some other values"
  }

  switchNameHandler = () => {
    // console.log("Clicked");
    this.setState({
      persons: [
        {
          name: "Muhammad Hafiz Siregar",
          age: "21"
        }
      ]
    })
  }

  render() {
    return (
      <div className="App">
        <h1> Hi, I'm A React App</h1>
        <p>It Worked</p>
        <button onClick={this.switchNameHandler}>Switch Name</button>
        <Person name={this.state.persons[0].name} age={this.state.persons[0].age}>My hobbies is = Reading</Person>
      </div>
    );
  }

}

export default App;
