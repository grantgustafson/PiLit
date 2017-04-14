import React from 'react';
import Module from './Module.js';
import UnconfiguredModule from './UnconfiguredModule.jsx';

export default class ModuleContainer extends React.Component {

  constructor(props) {
    super(props);
    this.state = {modules: null, unconfiguredModules: null};
  }

  componentWillMount() {
    var self = this;
    fetch('/get_modules').then(function(response) {
	// Convert to JSON
  	return response.json();
  }).then(function(j) {
  	// Yay, `j` is a JavaScript object
  	console.log(j);
    self.setState({modules: j.configuredModules,
                   unconfiguredModules: j.unconfiguredModules});
  });
  }

  render() {
    console.log('state : ')
    console.log(this.state);
    if (this.state.modules) {
      return (
        <div id="module-container">
          <div className="jumbotron text-center">
            <div className="container">
              <h1 className="display-3">Light Modules</h1>
            </div>
          </div>
          <div className="row">
          {this.state.modules.map(function(module) {
            return <Module key={module.hostname} module={module}/>
          })}
          {this.state.unconfiguredModules.map(function(module) {
            return <UnconfiguredModule key={module.hostname} module={module}/>
          })}
          </div>
        </div>
      )
    }
    return <div id="module-container">...Loading</div>;
  }
}
