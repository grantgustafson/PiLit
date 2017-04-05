import React from 'react';

export default class Module extends React.Component{
    render() {
        return (
           <div className="col col-md-4">
            {this.props.module.name}
            </div>
            )
    }
}
