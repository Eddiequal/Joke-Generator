import './App.css';
import React, { Component} from "react";
import axios from "axios";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      joke: null,
    };
  }
  
  async componentDidMount() {
    this.fetchJoke();
  }

  // Fetch function to fetch joke from API endpoint
  fetchJoke = () => {
    axios.get('http://localhost:8000/api/jokes/')
      .then(response => {
        this.setState({joke: response.data.jokes});
      })
      .catch(error => {
        console.log('Error fetching', error);
      });
  }

  handleJoke = () => {
    this.fetchJoke();
  }
  
  // renderItem function to render first generated joke
  renderItem = () => {
    const { joke } = this.state;
    if (joke) {
      return (
        <div>
          <p>{joke.content}</p>
        </div>
      );
    } else {
      return <p>No jokes available</p>
    }
  }

  // Render function to render JSX
  render() {
    return (
      <body>
        <h2 className="title">This is a random Joke generator! Click the button to generate random joke.</h2>
        <div className="container">
          {this.renderItem()}
          <button className="btn-generator" onClick={this.handleJoke}>Click</button>
        </div>
      </body>

    )
  }
}

export default App;
