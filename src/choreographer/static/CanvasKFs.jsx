import KF from './KF.jsx';

export default class CanvasKFs {
  constructor(vis, yOffset) {
    this.vis = vis;
    this.kfs = [];
    this.yOffset = yOffset;
    this.height = 200;
  }

  addKF(kf) {
    this.kfs.push(kf);
  }

  removeKF(kf) {
    let i = this.kfs.indexOf(kf);
    if (i == -1) {
      console.log('CanvasKFS: kf not found');
      return;
    }
    this.kfs.splice(i, 1);
  }

  kfY(intensity) {
    if (intensity < 0) return this.height / 2 + this.yOffset;
    return (this.height / 9) * (9-intensity) + this.yOffset;
  }

  draw() {
    let ctx = this.vis.ctx;
    ctx.beginPath();
    for (var i in this.kfs) {
      let kf = this.kfs[i];
      let time = kf.time - this.vis.pos;
      let x = this.vis.x(time);
      let y = this.kfY(kf.intensity);
      //console.log(x);
      if (x < -20 || x > this.vis.width) continue;
      if (kf.intensity < 0) ctx.fillRect(x-1, y, 3, 25);
      else ctx.fillRect(x - 4, y, 8, 8);
      //console.log('drawing kf');
    }
    ctx.closePath();
    ctx.stroke();
  }
}
