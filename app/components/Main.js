import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route } from 'react-router-dom';
import Module from './Module.js'
import ModuleContainer from './ModuleContainer.jsx'
import ModuleSetup from './ModuleSetup.jsx'
import MainNav from './Nav.js';

const Settings = () => <h1>Settings</h1>;

class Main extends React.Component{
    render() {
        return (
           <div className="container">
           <MainNav />
            {this.props.children}
           </div>
            )
    }
}

ReactDOM.render(
  <Router>
    <Main>
      <Route exact path="/" component={ModuleContainer} />
      <Route path="/settings" component={Settings} />
      <Route path="/module_setup/:id" component={ModuleSetup} />
    </Main>
  </Router>,
  document.getElementById('app'));
