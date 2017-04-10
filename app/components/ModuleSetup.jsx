import React from 'react';
import ReactDOM from 'react-dom'
import { Link } from 'react-router-dom';


export default class ModuleSetup extends React.Component{

  constructor(props) {
    super(props);
    this.state = {module: null};
  }

    componentWillMount() {
      console.log(this.props);
      if (!this.props.location.state) {
        console.log("fetching host");
        var self = this;
        fetch('/get_host/' + this.props.match.params.id).then(function(response) {
    	// Convert to JSON
      	return response.json();
      }).then(function(j) {
      	// Yay, `j` is a JavaScript object
      	console.log(j);
        if (j.success) {
          self.setState({module: j.host});
        } else {
          // TODO handle no host found error
          console.log('Couldnt find host');
        }
      });
      } else {
        this.setState({module: this.props.location.state});
      }
    }

    handleSubmit() {
      let name = ReactDOM.findDOMNode(this.refs.name).value;
      let location = ReactDOM.findDOMNode(this.refs.location).value;
      let numLEDs = parseInt(ReactDOM.findDOMNode(this.refs.numLEDs).value);
      let data = {name: name, location: location, numLEDs: numLEDs};
      console.log(data);
      fetch('/module_setup', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      }).then(function(response) {
        return response.json();
      }).then(this.handleResponse)

      return false;
    }

    handleResponse(j) {
      console.log("handling response");
    }

    render() {
      console.log(this.state);
      if (!this.state.module) return <div>Loading...</div>
        return (
             <div className="setup-container">
               <div>
                 <Link to="/">&lt; Back to Modules</Link>
               </div>
               <div className="jumbotron text-center">
                 <div className="container">
                   <h1 className="display-3">Configure {this.state.module.name}</h1>
                   <p>{this.state.module.MAC} {this.state.module.ip}</p>
                   <button className="btn btn-secondary">Flash Strip</button>
                 </div>
               </div>
               <div className="row justify-content-md-center">
                 <div className="col-md-6">
                   <form onSubmit={() => this.handleSubmit()}>
                    <div className="form-group">
                      <label htmlFor="nameInput">Name</label>
                      <input type="text" name="name" className="form-control" ref="name" id="nameInput" />
                    </div>
                    <div className="form-group">
                      <label htmlFor="locationInput">Location</label>
                      <input type="text" className="form-control" ref="location" id="locationInput" />
                    </div>
                    <div className="form-group">
                      <label htmlFor="numLEDsInput">Number of LEDs</label>
                      <input type="number" name="numLEDs" className="form-control" ref="numLEDs" id="numLEDsInput" />
                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                  </form>
                </div>
              </div>
            </div>
            )
    }
}
