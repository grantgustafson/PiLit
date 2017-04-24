import React from 'react';
import IKFRow from './IKFrow.jsx';
import MKFRow from './MKFrow.jsx';
import KeyFrame from './KF.jsx';

export default class KFTable extends React.Component {

  constructor(props) {
    super(props);
    this.iChildren = [];
    this.mChildren = [];
  }

  save() {
    this.saveStatus.innerHTML = 'Saving...';
    let iChildren = this.iChildren.filter(function(e) {return e != null});
    let iData = iChildren.map(function(e) { return e.state; });
    let mChildren = this.mChildren.filter(function(e) {return e != null});
    let mData = mChildren.map(function(e) { return e.state; });
    let data = {'ikfs': iData, 'mkfs': mData, id: this.props.id};
    console.log(data);
    let self = this;
    fetch('/track/save_kfs', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    }).then(function(response) {
      return response.json();
    }).then(function(j) {
      if (j.success) self.saveStatus.innerHTML = 'Success!';
    });
  }

  add_i_child(elem) {
    this.iChildren.push(elem);
  }

  add_m_child(elem) {
    this.mChildren.push(elem);
  }

  componentDidMount() {
    document.getElementById('save').onclick=this.save.bind(this);
    this.saveStatus = document.getElementById('status');
  }

  render() {
    let self = this;
    this.iChildren = [];
    this.mChildren = [];
    return (
    <div className="row">
      <div className="col col-6">
        <h3 className="text-center">Intensity Key Frames</h3>
        <table className="table">
          <thead>
            <tr>
              <th>Time</th>
              <th>Description</th>
              <th>Intensity</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody>
            {this.props.ikfs.map(function(kf, idx) {
              return <IKFRow ref={self.add_i_child.bind(self)} key={kf.key} kf={kf} remove={self.props.removeIKF} />
            })}
          </tbody>
        </table>
        </div>
        <div className="col col-6">
          <h3 className="text-center">Meta Key Frames</h3>
          <table className="table">
            <thead>
              <tr>
                <th>Time</th>
                <th>Description</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              {this.props.mkfs.map(function(kf, idx) {
                return <MKFRow ref={self.add_m_child.bind(self)} key={kf.key} kf={kf} remove={self.props.removeMKF} />
              })}
            </tbody>
          </table>
          </div>
      </div>
    )
  }
}
