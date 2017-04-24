import React from 'react';
import KFTable from './KFTable.jsx';
import KeyFrame from './KF.jsx';
import update from 'immutability-helper';

export default class KeyFrames extends React.Component {
  constructor(props) {
    super(props);
    this.state = {ikfs: [], mkfs:[]};
  }

  componentDidMount() {
    let c = document.getElementById('vis');
    c.addEventListener('keydown', this.checkKey.bind(this), false);
    let self = this;
    fetch('/track/get_kfs/' + this.props.id)
        .then(function(response) {
          return response.json();
        }).then(function(j) {
          if (j.success) {
            console.log(j.data);
            var ikfs = [];
            for (var i in j.data.ikfs) {
              let obj = j.data.ikfs[i];
              let kf = new KeyFrame(obj.time, obj.intensity, obj.description, i);
              self.props.vis.addKF(kf);
              ikfs.push(kf);
            }
            self.setState({ikfs: ikfs});

            var mkfs = [];
            for (var i in j.data.mkfs) {
              let obj = j.data.mkfs[i];
              let kf = new KeyFrame(obj.time, -1, obj.description, i);
              self.props.vis.addKF(kf);
              mkfs.push(kf);
            }
            self.setState({mkfs: mkfs});
          } else {
            console.log('Failed to fetch keyframes')
          }
        })
  }

  existsIKF(time, intensity) {
    for (var i in this.state.ikfs) {
      let ikf = this.state.ikfs[i];
      if (ikf.time == time && ikf.intensity == intensity) return true;
    }
    return false;
  }

  removeIKF(kf) {
    let ikfs = this.state.ikfs;
    let i = ikfs.indexOf(kf);
    if (i == -1) {
      console.log('kf not found');
      return;
    }
    //let newIkfs = ikfs.splice(i, 1);
    this.setState({ikfs: update(this.state.ikfs, {$splice: [[i, 1]]})});
    this.props.vis.removeKF(kf);
  }

  removeMKF(kf) {
    let mkfs = this.state.mkfs;
    let i = mkfs.indexOf(kf);
    if (i == -1) {
      console.log('kf not found');
      return;
    }
    //let newIkfs = ikfs.splice(i, 1);
    this.setState({mkfs: update(this.state.mkfs, {$splice: [[i, 1]]})});
    this.props.vis.removeKF(kf);  }

  newIntensityKF(intensity) {
    if (this.props.vis) {
      let time = Math.round(this.props.vis.pos * 1000) / 1000.0;
      if (this.existsIKF(time, intensity)) {
        console.log('already exsits IKF');
        return;
      }
      console.log('Intensity KF: ' + time);

      let kf = new KeyFrame(time, intensity);
      this.props.vis.addKF(kf);
      let ikfs = this.state.ikfs;
      ikfs.push(kf);
      ikfs.sort(function(a, b) {return a.time - b.time});
      this.setState({ikfs: ikfs});
    }
  }

  newMetaKF() {
    if (!this.props.vis) return;
    let time = Math.round(this.props.vis.pos * 1000) / 1000.0;
    console.log('New meta KF: ' + time);
    let kf = new KeyFrame(time, -1);
    this.props.vis.addKF(kf);
    let mkfs = this.state.mkfs;
    mkfs.push(kf);
    mkfs.sort(function(a, b) {return a.time - b.time});
    this.setState({mkfs: mkfs});
  }

  checkKey(e) {
    e = e || window.event;
    let code = parseInt(e.keyCode);
    if (code >= 48 && code <= 57) {
      this.newIntensityKF(code-48);
      e.preventDefault();
    } else if (code == 16) {
      this.newMetaKF();
      e.preventDefault();
    }
  }

  render() {
    return <KFTable id={this.props.id} ikfs={this.state.ikfs} mkfs={this.state.mkfs} removeIKF={this.removeIKF.bind(this)} removeMKF={this.removeMKF.bind(this)}/>
  }
}
