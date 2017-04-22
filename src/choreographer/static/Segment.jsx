export default class Segment {
  constructor(data, yOffset, maxDB) {
    this.data = data;
    this.yOffset = yOffset;
    this.height = 140;
    this.minDB = -60.0;
    this.maxDB = maxDB;
  }

  calcLoudnessY() {
    let range = this.maxDB - this.minDB;
    let relY = ((this.data.loudness_max - this.minDB) / range) * this.height;
    return this.yOffset + (this.height - relY);
  }


  drawSelf(trackVis) {
    let ctx = trackVis.ctx;
    let x = trackVis.x(this.data.start - trackVis.pos);
    let width = trackVis.timeToPixels(this.data.duration) - 1;
    if (x < -150 || x > trackVis.width) return;
    let max_time = trackVis.timeToPixels(this.data.loudness_max_time);
    let loud_y = this.calcLoudnessY();
    ctx.beginPath();
    ctx.rect(x, this.yOffset, width, this.height);
    ctx.fillRect(x + max_time, loud_y, 6,6);
    ctx.closePath();
    ctx.stroke();
  }
}
