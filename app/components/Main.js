import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route } from 'react-router-dom';
import Module from './Module.js'
import ModuleContainer from './ModuleContainer.jsx'
import MainNav from './Nav.js';

const Settings = () => <h1>Settings</h1>;

class Main extends React.Component{
    render() {
        return (
           <div className="container">
           <MainNav />
           <div id="2">
           </div>
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
    </Main>
  </Router>,
  document.getElementById('app'));
