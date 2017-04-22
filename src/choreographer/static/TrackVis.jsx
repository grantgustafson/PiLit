import TrackData from './trackdata.jsx';
import Segment from './Segment.jsx';
let REFRESH = 60;
let WINDOW = 10.0;

export default class TrackVis {
  constructor(td) {
    this.td = td;
    this.canvas = document.getElementById('vis');
    this.ctx = this.canvas.getContext('2d');
    let bounds = this.canvas.getBoundingClientRect();
    let w = bounds.width;
    let h = bounds.height;
    this.width = w*2;
    this.height = h*2;
    this.timeBehind = 3.0;
    this.pos = 0.0;
    this.lastUpdate = ((new Date()).getTime())/1000;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    this.xScale = this.width / WINDOW;
    console.log(this.td);
    this.getPos();
    this.timeBanner = document.getElementById('time');
    this.songBanner = document.getElementById('song');
    this.isPlaying = true;
    this.segments = [];


    this.init();
  }

  init() {
    this.songBanner.innerHTML = this.td.data.analysis.track.name;

    var maxSegDB = -60.0;
    for (var idx in this.td.data.analysis.segments) {
      let db = this.td.data.analysis.segments[idx].loudness_max;
      if (db > maxSegDB) maxSegDB = db;
    }

    for (var idx in this.td.data.analysis.segments) {
      let d = this.td.data.analysis.segments[idx];
      this.segments.push(new Segment(d, 150, maxSegDB));
    }

    document.getElementById('play').onclick = this.play.bind(this);
    document.getElementById('pause').onclick = this.pause.bind(this);
    document.getElementById('time-input').onchange = this.updateTime.bind(this);
  }

  timeToPixels(time) {
    return time * this.xScale;
  }

  x(time) {
    return (time + this.timeBehind) * this.xScale;
  }

  getPos() {
    var self = this;
    fetch('pos')
    .then(function(response) {
      return response.json();
    }).then(function(j) {
      self.pos = +j.pos;
      console.log('pos: ' + self.pos);
      setInterval(self.draw.bind(self), 1000/REFRESH);
      // setTimeout(self.draw.bind(self), 1000);
    })
  }

  drawSegments() {
    for (var idx in this.segments) {
      this.segments[idx].drawSelf(this);
    }
    this.ctx.stroke();

  }

  drawBeats() {
    this.ctx.beginPath();
    let barWidth = 10;
    let barheight = 50;
    this.ctx.lineWidth="2";
    this.ctx.strokeStyle="red";
    for (var i in this.td.data.analysis.beats) {
      let beat = this.td.data.analysis.beats[i];
      let start_time = beat.start;
      let x = this.x(start_time - this.pos);
      if (x < this.width && x > -50.0) {
        this.ctx.rect(x, 10, barWidth, barheight);
      }
    }
    this.ctx.closePath();
    this.ctx.stroke();
  }

  drawBars() {
    this.ctx.beginPath();
    let barheight = 50;
    this.ctx.lineWidth="2";
    this.ctx.strokeStyle="blue";
    for (var i in this.td.data.analysis.bars) {
      let bar = this.td.data.analysis.bars[i];
      let start_time = bar.start;
      let x = this.x(start_time - this.pos);
      let barWidth = this.timeToPixels(bar.duration) - 10;
      if (x < this.width && x > -(barWidth + 10)) {
        this.ctx.rect(x, 70, barWidth, barheight);
      }
    }
    this.ctx.closePath();
    this.ctx.stroke();
  }

  drawCurrPos() {
    this.ctx.beginPath();
    this.ctx.moveTo(this.x(0), 0);
    this.ctx.lineTo(this.x(0), this.height);
      this.ctx.closePath();
      this.ctx.stroke();
  }

  update() {
    if (this.isPlaying) {
      let currTime = ((new Date()).getTime()) / 1000.0;
      let tDelta = currTime - this.lastUpdate;
      this.pos += tDelta;
      this.lastUpdate = currTime;
      this.timeBanner.innerHTML = Math.round(this.pos * 100) / 100.0;
    }
    if (this.pos > this.td.data.analysis.track.duration) {
      this.play = false;
    }
  }

  play() {
    console.log('Play!');
    if (!this.isPlaying) {
      this.isPlaying = true;
      this.lastUpdate = ((new Date()).getTime()) / 1000.0;
    }
  }

  pause() {
      console.log('Pause!');
    if (this.isPlaying) {
      this.isPlaying = false;
    }
  }

  updateTime() {
    let elem = document.getElementById('time-input');
    this.pos = parseFloat(elem.value);
  }

  draw() {
    this.update();
    this.ctx.clearRect(0, 0, this.width, this.height);
    this.drawBeats();
    this.drawBars();
    this.drawSegments();
    this.drawCurrPos();
  }
}
