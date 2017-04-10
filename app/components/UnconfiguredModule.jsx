import React from 'react';

export default class UnconfiguredModule extends React.Component{
    render() {
        return (
           <div className="col col-md-4 text-center">
             <div className="box">
                        <h3>{this.props.module.name}</h3>
                        <p>{this.props.module.MAC}</p>
                        <p>{this.props.module.ip}</p>
                        <p>
                            <a href="#" className="btn btn-secondary btn-block">Configure</a>
                        </p>
              </div>
            </div>
            )
    }
}
