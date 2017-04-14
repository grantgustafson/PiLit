import React from 'react';
import { Link } from 'react-router-dom';


export default class UnconfiguredModule extends React.Component{
    render() {
        return (
           <div className="col col-md-4 text-center">
             <div className="box">
              <h3>{this.props.module.hostname}</h3>
              <p>{this.props.module.MAC}</p>
              <p>{this.props.module.ip}</p>
              <p>
                <Link to={{pathname: "/module_setup/" + this.props.module.hostname,
                          state: this.props.module}} className="btn btn-secondary btn-block">Configure</Link>
              </p>
              </div>
            </div>
            )
    }
}
