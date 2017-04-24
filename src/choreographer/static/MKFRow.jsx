import React from 'react';
import KeyFrame from './KF.jsx';

export default class MKFRow extends React.Component {

  constructor(props) {
    super(props);
    this.state = {description: this.props.kf.description,
                  time: this.props.kf.time};
  }

  remove() {
    this.props.remove(this.props.kf);
  }

  descriptionChange(e) {
    this.setState({description: e.target.value});
  }

  render() {
    let time = Math.round(this.state.time * 1000) / 1000.0;
    return (
      <tr>
        <td>{time}</td>
        <td><input placeholder="description" onChange={this.descriptionChange.bind(this)} value={this.state.description}></input></td>
        <td><button className="btn btn-primary" onClick={this.remove.bind(this)}>Delete</button></td>
      </tr>
    )
  }
}
