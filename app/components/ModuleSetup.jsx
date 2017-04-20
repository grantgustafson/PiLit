import React from 'react';
import ReactDOM from 'react-dom'
import { Link } from 'react-router-dom';


export default class ModuleSetup extends React.Component{

  constructor(props) {
    super(props);
    this.state = {module: null, error: null, message: null};
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
          self.setState({error: 'Could not find host ' + self.props.match.params.id});
        }
      });
      } else {
        this.setState({module: this.props.location.state});
      }
    }

    handleSubmit(e) {
      e.preventDefault();
      let name = ReactDOM.findDOMNode(this.refs.name).value;
      let location = ReactDOM.findDOMNode(this.refs.location).value;
      let hostname = this.state.module.hostname;
      let data = {name: name, location: location, hostname: hostname};
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
      }).then(this.handleResponse.bind(this))

      return false;
    }

    renderError() {
      return (
      <div className="alert alert-danger" role="alert">
       <strong>Error: </strong> {this.state.error}
      </div>
    )
    }

    renderMessage() {
      return (
      <div className="alert alert-success" role="alert">
       {this.state.message}
      </div>
    )
    }

    handleResponse(j) {
      if (j.success) this.setState({message: j.message});
      return false;
    }

    flash() {
      fetch('/flash_module/' + this.state.module.hostname);
    }

    render() {
      console.log(this.state);
      if (!this.state.module) {
        if (this.state.error) {
          return this.renderError()
       } else return <div>Loading...</div>
      }
        return (
             <div className="setup-container">
               <div>
                 <Link to="/">&lt; Back to Modules</Link>
               </div>
               {this.state.error && this.renderError()}
               <div className="jumbotron text-center">
                 <div className="container">
                   <h1 className="display-3">Configure {this.state.module.hostname}</h1>
                   <p>{this.state.module.ip}</p>
                   <button className="btn btn-secondary" onClick={this.flash.bind(this)}>Flash Strip</button>
                 </div>
               </div>
               {this.state.message && this.renderMessage()}
               <div className="row justify-content-md-center">
                 <div className="col-md-6">
                   <form onSubmit={(e) => this.handleSubmit(e)}>
                    <div className="form-group">
                      <label htmlFor="nameInput">Name</label>
                      <input type="text" name="name" className="form-control" ref="name" id="nameInput" />
                    </div>
                    <div className="form-group">
                      <label htmlFor="locationInput">Location</label>
                      <input type="text" className="form-control" ref="location" id="locationInput" />
                    </div>
                    <button type="submit" className="btn btn-primary">Save</button>
                  </form>
                </div>
              </div>
            </div>
            )
    }
}
