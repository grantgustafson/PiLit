import TrackData from './trackdata.jsx';
import TrackVis from './TrackVis.jsx';
import ReactDOM from 'react-dom';
import React from 'react';
import KFTable from './KFTable.jsx';
import KeyFrames from './KeyFrames.jsx';
let id = document.getElementById('main').dataset.track;

class Main extends React.Component {

  constructor(props) {
    super(props);
    this.state = {vis: null};

  }

  componentDidMount() {
    let vis = new TrackVis(this.props.data, this.props.id);
    this.setState({vis: vis});
  }

  render() {
    return (
      <div>
      <div><span id="song"></span> <span id="time"></span></div>
      <button id="play" className="btn btn-primary" >Play</button>
      <button id="pause" className="btn btn-primary">Pause</button>
      <button id="sync" className="btn btn-primary">Re-Sync</button>
      <input id="time-input"></input>
      <button id="save" className="btn btn-primary">Save Key Frames</button>
      <span id="status"></span>
    <canvas tabIndex="0" id="vis"> </canvas>
      <div id="keyframes">
        <KeyFrames id={this.props.id} vis={this.state.vis}/>
      </div>
      </div>
    )
  }
}



fetch('data/' + id)
.then(function(response) {
  return response.json();
}).then(function(data) {
  ReactDOM.render(
    <Main data={data} id={id}/>,
    document.getElementById('main')
  );
});
