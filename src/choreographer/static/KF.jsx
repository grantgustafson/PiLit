export default class KeyFrame {
  constructor(time, intensity, description, idx) {
    this.time = time;
    this.intensity = intensity;
    this.description = description || '';
    this.idx = idx || 0;
    this.key = (new Date()).getTime() - this.idx * 1013;
  }
}
