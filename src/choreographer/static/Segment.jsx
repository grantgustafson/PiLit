export default class Segment {
  constructor(data, yOffset, maxDB) {
    this.data = data;
    this.yOffset = yOffset;
    this.height = 140;
    this.minDB = -40.0;
    this.maxDB = maxDB;
  }

  calcLoudnessY(db) {
    let range = this.maxDB - this.minDB;
    let relY = ((db - this.minDB) / range) * this.height;
    return this.yOffset + (this.height - relY);
  }


  drawSelf(trackVis) {
    let ctx = trackVis.ctx;
    let x = trackVis.x(this.data.start - trackVis.pos);
    let width = trackVis.timeToPixels(this.data.duration) - 1;
    if (x < -width || x > trackVis.width) return;
    let max_time = trackVis.timeToPixels(this.data.loudness_max_time);
    let loud_y = this.calcLoudnessY(this.data.loudness_max);
    //ctx.beginPath();
    ctx.strokeRect(x, this.yOffset, width, this.height);
    ctx.fillRect(x + max_time, loud_y, 6,6);
    if (this.data.loudness_start) {
      let min_y = this.calcLoudnessY(this.data.loudness_start);
      ctx.fillRect(x-3, min_y, 6,6);
    }


  }
}
