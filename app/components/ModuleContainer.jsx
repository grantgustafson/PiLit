import React from 'react';
import Module from './Module.js';

export default class ModuleContainer extends React.Component {

  constructor(props) {
    super(props);
    this.state = {modules: null};
  }

  componentWillMount() {
    var self = this;
    fetch('/get_modules').then(function(response) {
	// Convert to JSON
  	return response.json();
  }).then(function(j) {
  	// Yay, `j` is a JavaScript object
  	console.log(j);
    self.setState({modules: j.configuredModules});
  });
  }

  render() {
    console.log('state: ')
    console.log(this.state);
    if (this.state.modules) {
      return (
        <div id="module-container">
          <div className="jumbotron">
            <div className="container">
              <h1 className="display-3">Light Modules</h1>
            </div>
          </div>
          <div className="row">
          {this.state.modules.map(function(module) {
            return <Module key={module.name} module={module}/>
          })}
          </div>
        </div>
      )
    }
    return <div id="module-container">...Loading</div>;
  }
}
