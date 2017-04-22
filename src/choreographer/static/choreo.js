import TrackData from './trackdata.jsx';
import TrackVis from './TrackVis.jsx';

let id = document.getElementById('main').dataset.track;

var vis = null;

fetch('data/' + id)
.then(function(response) {
  return response.json();
}).then(function(data) {
  let td = new TrackData(data);
  vis = new TrackVis(td);
  console.log(vis);
});

function play() {
  console.log('clicked');
  vis.play();
}
