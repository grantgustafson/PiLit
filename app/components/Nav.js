import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

export default class MainNav extends React.Component {

  render() {
    return (
      <nav className="navbar navbar-toggleable-md navbar-inverse bg-inverse fixed-top">
        <ul className="navbar-nav mr-auto">
            <NavLink exact className="nav-link" to="/" activeClassName="active">
              <li className="nav-item">
                Modules
              </li>
            </NavLink>
            <NavLink exact className="nav-link" to="/settings" activeClassName="active">
              <li className="nav-item">
                Settings
              </li>
            </NavLink>

        </ul>
    </nav>
    )
  }

}
