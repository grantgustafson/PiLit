/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 1);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */,
/* 1 */
/* unknown exports provided */
/* all exports used */
/*!**************************!*\
  !*** ./static/choreo.js ***!
  \**************************/
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nvar _trackdata = __webpack_require__(/*! ./trackdata.jsx */ 2);\n\nvar _trackdata2 = _interopRequireDefault(_trackdata);\n\nvar _TrackVis = __webpack_require__(/*! ./TrackVis.jsx */ 3);\n\nvar _TrackVis2 = _interopRequireDefault(_TrackVis);\n\nfunction _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }\n\nvar id = document.getElementById('main').dataset.track;\n\nvar vis = null;\n\nfetch('data/' + id).then(function (response) {\n  return response.json();\n}).then(function (data) {\n  var td = new _trackdata2.default(data);\n  vis = new _TrackVis2.default(td);\n  console.log(vis);\n});\n\nfunction play() {\n  console.log('clicked');\n  vis.play();\n}//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMS5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvY2hvcmVvLmpzP2EyYWEiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IFRyYWNrRGF0YSBmcm9tICcuL3RyYWNrZGF0YS5qc3gnO1xuaW1wb3J0IFRyYWNrVmlzIGZyb20gJy4vVHJhY2tWaXMuanN4JztcblxubGV0IGlkID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ21haW4nKS5kYXRhc2V0LnRyYWNrO1xuXG52YXIgdmlzID0gbnVsbDtcblxuZmV0Y2goJ2RhdGEvJyArIGlkKVxuLnRoZW4oZnVuY3Rpb24ocmVzcG9uc2UpIHtcbiAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKTtcbn0pLnRoZW4oZnVuY3Rpb24oZGF0YSkge1xuICBsZXQgdGQgPSBuZXcgVHJhY2tEYXRhKGRhdGEpO1xuICB2aXMgPSBuZXcgVHJhY2tWaXModGQpO1xuICBjb25zb2xlLmxvZyh2aXMpO1xufSk7XG5cbmZ1bmN0aW9uIHBsYXkoKSB7XG4gIGNvbnNvbGUubG9nKCdjbGlja2VkJyk7XG4gIHZpcy5wbGF5KCk7XG59XG5cblxuXG4vLyBXRUJQQUNLIEZPT1RFUiAvL1xuLy8gc3RhdGljL2Nob3Jlby5qcyJdLCJtYXBwaW5ncyI6Ijs7QUFBQTtBQUNBOzs7QUFBQTtBQUNBOzs7OztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlUm9vdCI6IiJ9");

/***/ }),
/* 2 */
/* unknown exports provided */
/* all exports used */
/*!******************************!*\
  !*** ./static/trackdata.jsx ***!
  \******************************/
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nObject.defineProperty(exports, \"__esModule\", {\n  value: true\n});\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nvar TrackData = function TrackData(data) {\n  _classCallCheck(this, TrackData);\n\n  this.data = data;\n};\n\nexports.default = TrackData;//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMi5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvdHJhY2tkYXRhLmpzeD9kM2M2Il0sInNvdXJjZXNDb250ZW50IjpbImV4cG9ydCBkZWZhdWx0IGNsYXNzIFRyYWNrRGF0YSB7XG4gIGNvbnN0cnVjdG9yKGRhdGEpIHtcbiAgICB0aGlzLmRhdGEgPSBkYXRhO1xuXG4gIH1cblxuXG59XG5cblxuXG4vLyBXRUJQQUNLIEZPT1RFUiAvL1xuLy8gc3RhdGljL3RyYWNrZGF0YS5qc3giXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQUE7QUFFQTtBQUNBO0FBTEEiLCJzb3VyY2VSb290IjoiIn0=");

/***/ }),
/* 3 */
/* unknown exports provided */
/* all exports used */
/*!*****************************!*\
  !*** ./static/TrackVis.jsx ***!
  \*****************************/
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nObject.defineProperty(exports, \"__esModule\", {\n  value: true\n});\n\nvar _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();\n\nvar _trackdata = __webpack_require__(/*! ./trackdata.jsx */ 2);\n\nvar _trackdata2 = _interopRequireDefault(_trackdata);\n\nvar _Segment = __webpack_require__(/*! ./Segment.jsx */ 4);\n\nvar _Segment2 = _interopRequireDefault(_Segment);\n\nfunction _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nvar REFRESH = 60;\nvar WINDOW = 10.0;\n\nvar TrackVis = function () {\n  function TrackVis(td) {\n    _classCallCheck(this, TrackVis);\n\n    this.td = td;\n    this.canvas = document.getElementById('vis');\n    this.ctx = this.canvas.getContext('2d');\n    var bounds = this.canvas.getBoundingClientRect();\n    var w = bounds.width;\n    var h = bounds.height;\n    this.width = w * 2;\n    this.height = h * 2;\n    this.timeBehind = 3.0;\n    this.pos = 0.0;\n    this.lastUpdate = new Date().getTime() / 1000;\n    this.canvas.width = this.width;\n    this.canvas.height = this.height;\n    this.xScale = this.width / WINDOW;\n    console.log(this.td);\n    this.getPos();\n    this.timeBanner = document.getElementById('time');\n    this.songBanner = document.getElementById('song');\n    this.isPlaying = true;\n    this.segments = [];\n\n    this.init();\n  }\n\n  _createClass(TrackVis, [{\n    key: 'init',\n    value: function init() {\n      this.songBanner.innerHTML = this.td.data.analysis.track.name;\n\n      var maxSegDB = -60.0;\n      for (var idx in this.td.data.analysis.segments) {\n        var db = this.td.data.analysis.segments[idx].loudness_max;\n        if (db > maxSegDB) maxSegDB = db;\n      }\n\n      for (var idx in this.td.data.analysis.segments) {\n        var d = this.td.data.analysis.segments[idx];\n        this.segments.push(new _Segment2.default(d, 150, maxSegDB));\n      }\n\n      document.getElementById('play').onclick = this.play.bind(this);\n      document.getElementById('pause').onclick = this.pause.bind(this);\n      document.getElementById('time-input').onchange = this.updateTime.bind(this);\n    }\n  }, {\n    key: 'timeToPixels',\n    value: function timeToPixels(time) {\n      return time * this.xScale;\n    }\n  }, {\n    key: 'x',\n    value: function x(time) {\n      return (time + this.timeBehind) * this.xScale;\n    }\n  }, {\n    key: 'getPos',\n    value: function getPos() {\n      var self = this;\n      fetch('pos').then(function (response) {\n        return response.json();\n      }).then(function (j) {\n        self.pos = +j.pos;\n        console.log('pos: ' + self.pos);\n        setInterval(self.draw.bind(self), 1000 / REFRESH);\n        // setTimeout(self.draw.bind(self), 1000);\n      });\n    }\n  }, {\n    key: 'drawSegments',\n    value: function drawSegments() {\n      for (var idx in this.segments) {\n        this.segments[idx].drawSelf(this);\n      }\n      this.ctx.stroke();\n    }\n  }, {\n    key: 'drawBeats',\n    value: function drawBeats() {\n      this.ctx.beginPath();\n      var barWidth = 10;\n      var barheight = 50;\n      this.ctx.lineWidth = \"2\";\n      this.ctx.strokeStyle = \"red\";\n      for (var i in this.td.data.analysis.beats) {\n        var beat = this.td.data.analysis.beats[i];\n        var start_time = beat.start;\n        var x = this.x(start_time - this.pos);\n        if (x < this.width && x > -50.0) {\n          this.ctx.rect(x, 10, barWidth, barheight);\n        }\n      }\n      this.ctx.closePath();\n      this.ctx.stroke();\n    }\n  }, {\n    key: 'drawBars',\n    value: function drawBars() {\n      this.ctx.beginPath();\n      var barheight = 50;\n      this.ctx.lineWidth = \"2\";\n      this.ctx.strokeStyle = \"blue\";\n      for (var i in this.td.data.analysis.bars) {\n        var bar = this.td.data.analysis.bars[i];\n        var start_time = bar.start;\n        var x = this.x(start_time - this.pos);\n        var barWidth = this.timeToPixels(bar.duration) - 10;\n        if (x < this.width && x > -(barWidth + 10)) {\n          this.ctx.rect(x, 70, barWidth, barheight);\n        }\n      }\n      this.ctx.closePath();\n      this.ctx.stroke();\n    }\n  }, {\n    key: 'drawCurrPos',\n    value: function drawCurrPos() {\n      this.ctx.beginPath();\n      this.ctx.moveTo(this.x(0), 0);\n      this.ctx.lineTo(this.x(0), this.height);\n      this.ctx.closePath();\n      this.ctx.stroke();\n    }\n  }, {\n    key: 'update',\n    value: function update() {\n      if (this.isPlaying) {\n        var currTime = new Date().getTime() / 1000.0;\n        var tDelta = currTime - this.lastUpdate;\n        this.pos += tDelta;\n        this.lastUpdate = currTime;\n        this.timeBanner.innerHTML = Math.round(this.pos * 100) / 100.0;\n      }\n      if (this.pos > this.td.data.analysis.track.duration) {\n        this.play = false;\n      }\n    }\n  }, {\n    key: 'play',\n    value: function play() {\n      console.log('Play!');\n      if (!this.isPlaying) {\n        this.isPlaying = true;\n        this.lastUpdate = new Date().getTime() / 1000.0;\n      }\n    }\n  }, {\n    key: 'pause',\n    value: function pause() {\n      console.log('Pause!');\n      if (this.isPlaying) {\n        this.isPlaying = false;\n      }\n    }\n  }, {\n    key: 'updateTime',\n    value: function updateTime() {\n      var elem = document.getElementById('time-input');\n      this.pos = parseFloat(elem.value);\n    }\n  }, {\n    key: 'draw',\n    value: function draw() {\n      this.update();\n      this.ctx.clearRect(0, 0, this.width, this.height);\n      this.drawBeats();\n      this.drawBars();\n      this.drawSegments();\n      this.drawCurrPos();\n    }\n  }]);\n\n  return TrackVis;\n}();\n\nexports.default = TrackVis;//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMy5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvVHJhY2tWaXMuanN4Pzc2MDUiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IFRyYWNrRGF0YSBmcm9tICcuL3RyYWNrZGF0YS5qc3gnO1xuaW1wb3J0IFNlZ21lbnQgZnJvbSAnLi9TZWdtZW50LmpzeCc7XG5sZXQgUkVGUkVTSCA9IDYwO1xubGV0IFdJTkRPVyA9IDEwLjA7XG5cbmV4cG9ydCBkZWZhdWx0IGNsYXNzIFRyYWNrVmlzIHtcbiAgY29uc3RydWN0b3IodGQpIHtcbiAgICB0aGlzLnRkID0gdGQ7XG4gICAgdGhpcy5jYW52YXMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndmlzJyk7XG4gICAgdGhpcy5jdHggPSB0aGlzLmNhbnZhcy5nZXRDb250ZXh0KCcyZCcpO1xuICAgIGxldCBib3VuZHMgPSB0aGlzLmNhbnZhcy5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICBsZXQgdyA9IGJvdW5kcy53aWR0aDtcbiAgICBsZXQgaCA9IGJvdW5kcy5oZWlnaHQ7XG4gICAgdGhpcy53aWR0aCA9IHcqMjtcbiAgICB0aGlzLmhlaWdodCA9IGgqMjtcbiAgICB0aGlzLnRpbWVCZWhpbmQgPSAzLjA7XG4gICAgdGhpcy5wb3MgPSAwLjA7XG4gICAgdGhpcy5sYXN0VXBkYXRlID0gKChuZXcgRGF0ZSgpKS5nZXRUaW1lKCkpLzEwMDA7XG4gICAgdGhpcy5jYW52YXMud2lkdGggPSB0aGlzLndpZHRoO1xuICAgIHRoaXMuY2FudmFzLmhlaWdodCA9IHRoaXMuaGVpZ2h0O1xuICAgIHRoaXMueFNjYWxlID0gdGhpcy53aWR0aCAvIFdJTkRPVztcbiAgICBjb25zb2xlLmxvZyh0aGlzLnRkKTtcbiAgICB0aGlzLmdldFBvcygpO1xuICAgIHRoaXMudGltZUJhbm5lciA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCd0aW1lJyk7XG4gICAgdGhpcy5zb25nQmFubmVyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3NvbmcnKTtcbiAgICB0aGlzLmlzUGxheWluZyA9IHRydWU7XG4gICAgdGhpcy5zZWdtZW50cyA9IFtdO1xuXG5cbiAgICB0aGlzLmluaXQoKTtcbiAgfVxuXG4gIGluaXQoKSB7XG4gICAgdGhpcy5zb25nQmFubmVyLmlubmVySFRNTCA9IHRoaXMudGQuZGF0YS5hbmFseXNpcy50cmFjay5uYW1lO1xuXG4gICAgdmFyIG1heFNlZ0RCID0gLTYwLjA7XG4gICAgZm9yICh2YXIgaWR4IGluIHRoaXMudGQuZGF0YS5hbmFseXNpcy5zZWdtZW50cykge1xuICAgICAgbGV0IGRiID0gdGhpcy50ZC5kYXRhLmFuYWx5c2lzLnNlZ21lbnRzW2lkeF0ubG91ZG5lc3NfbWF4O1xuICAgICAgaWYgKGRiID4gbWF4U2VnREIpIG1heFNlZ0RCID0gZGI7XG4gICAgfVxuXG4gICAgZm9yICh2YXIgaWR4IGluIHRoaXMudGQuZGF0YS5hbmFseXNpcy5zZWdtZW50cykge1xuICAgICAgbGV0IGQgPSB0aGlzLnRkLmRhdGEuYW5hbHlzaXMuc2VnbWVudHNbaWR4XTtcbiAgICAgIHRoaXMuc2VnbWVudHMucHVzaChuZXcgU2VnbWVudChkLCAxNTAsIG1heFNlZ0RCKSk7XG4gICAgfVxuXG4gICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3BsYXknKS5vbmNsaWNrID0gdGhpcy5wbGF5LmJpbmQodGhpcyk7XG4gICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3BhdXNlJykub25jbGljayA9IHRoaXMucGF1c2UuYmluZCh0aGlzKTtcbiAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndGltZS1pbnB1dCcpLm9uY2hhbmdlID0gdGhpcy51cGRhdGVUaW1lLmJpbmQodGhpcyk7XG4gIH1cblxuICB0aW1lVG9QaXhlbHModGltZSkge1xuICAgIHJldHVybiB0aW1lICogdGhpcy54U2NhbGU7XG4gIH1cblxuICB4KHRpbWUpIHtcbiAgICByZXR1cm4gKHRpbWUgKyB0aGlzLnRpbWVCZWhpbmQpICogdGhpcy54U2NhbGU7XG4gIH1cblxuICBnZXRQb3MoKSB7XG4gICAgdmFyIHNlbGYgPSB0aGlzO1xuICAgIGZldGNoKCdwb3MnKVxuICAgIC50aGVuKGZ1bmN0aW9uKHJlc3BvbnNlKSB7XG4gICAgICByZXR1cm4gcmVzcG9uc2UuanNvbigpO1xuICAgIH0pLnRoZW4oZnVuY3Rpb24oaikge1xuICAgICAgc2VsZi5wb3MgPSArai5wb3M7XG4gICAgICBjb25zb2xlLmxvZygncG9zOiAnICsgc2VsZi5wb3MpO1xuICAgICAgc2V0SW50ZXJ2YWwoc2VsZi5kcmF3LmJpbmQoc2VsZiksIDEwMDAvUkVGUkVTSCk7XG4gICAgICAvLyBzZXRUaW1lb3V0KHNlbGYuZHJhdy5iaW5kKHNlbGYpLCAxMDAwKTtcbiAgICB9KVxuICB9XG5cbiAgZHJhd1NlZ21lbnRzKCkge1xuICAgIGZvciAodmFyIGlkeCBpbiB0aGlzLnNlZ21lbnRzKSB7XG4gICAgICB0aGlzLnNlZ21lbnRzW2lkeF0uZHJhd1NlbGYodGhpcyk7XG4gICAgfVxuICAgIHRoaXMuY3R4LnN0cm9rZSgpO1xuXG4gIH1cblxuICBkcmF3QmVhdHMoKSB7XG4gICAgdGhpcy5jdHguYmVnaW5QYXRoKCk7XG4gICAgbGV0IGJhcldpZHRoID0gMTA7XG4gICAgbGV0IGJhcmhlaWdodCA9IDUwO1xuICAgIHRoaXMuY3R4LmxpbmVXaWR0aD1cIjJcIjtcbiAgICB0aGlzLmN0eC5zdHJva2VTdHlsZT1cInJlZFwiO1xuICAgIGZvciAodmFyIGkgaW4gdGhpcy50ZC5kYXRhLmFuYWx5c2lzLmJlYXRzKSB7XG4gICAgICBsZXQgYmVhdCA9IHRoaXMudGQuZGF0YS5hbmFseXNpcy5iZWF0c1tpXTtcbiAgICAgIGxldCBzdGFydF90aW1lID0gYmVhdC5zdGFydDtcbiAgICAgIGxldCB4ID0gdGhpcy54KHN0YXJ0X3RpbWUgLSB0aGlzLnBvcyk7XG4gICAgICBpZiAoeCA8IHRoaXMud2lkdGggJiYgeCA+IC01MC4wKSB7XG4gICAgICAgIHRoaXMuY3R4LnJlY3QoeCwgMTAsIGJhcldpZHRoLCBiYXJoZWlnaHQpO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLmN0eC5jbG9zZVBhdGgoKTtcbiAgICB0aGlzLmN0eC5zdHJva2UoKTtcbiAgfVxuXG4gIGRyYXdCYXJzKCkge1xuICAgIHRoaXMuY3R4LmJlZ2luUGF0aCgpO1xuICAgIGxldCBiYXJoZWlnaHQgPSA1MDtcbiAgICB0aGlzLmN0eC5saW5lV2lkdGg9XCIyXCI7XG4gICAgdGhpcy5jdHguc3Ryb2tlU3R5bGU9XCJibHVlXCI7XG4gICAgZm9yICh2YXIgaSBpbiB0aGlzLnRkLmRhdGEuYW5hbHlzaXMuYmFycykge1xuICAgICAgbGV0IGJhciA9IHRoaXMudGQuZGF0YS5hbmFseXNpcy5iYXJzW2ldO1xuICAgICAgbGV0IHN0YXJ0X3RpbWUgPSBiYXIuc3RhcnQ7XG4gICAgICBsZXQgeCA9IHRoaXMueChzdGFydF90aW1lIC0gdGhpcy5wb3MpO1xuICAgICAgbGV0IGJhcldpZHRoID0gdGhpcy50aW1lVG9QaXhlbHMoYmFyLmR1cmF0aW9uKSAtIDEwO1xuICAgICAgaWYgKHggPCB0aGlzLndpZHRoICYmIHggPiAtKGJhcldpZHRoICsgMTApKSB7XG4gICAgICAgIHRoaXMuY3R4LnJlY3QoeCwgNzAsIGJhcldpZHRoLCBiYXJoZWlnaHQpO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLmN0eC5jbG9zZVBhdGgoKTtcbiAgICB0aGlzLmN0eC5zdHJva2UoKTtcbiAgfVxuXG4gIGRyYXdDdXJyUG9zKCkge1xuICAgIHRoaXMuY3R4LmJlZ2luUGF0aCgpO1xuICAgIHRoaXMuY3R4Lm1vdmVUbyh0aGlzLngoMCksIDApO1xuICAgIHRoaXMuY3R4LmxpbmVUbyh0aGlzLngoMCksIHRoaXMuaGVpZ2h0KTtcbiAgICAgIHRoaXMuY3R4LmNsb3NlUGF0aCgpO1xuICAgICAgdGhpcy5jdHguc3Ryb2tlKCk7XG4gIH1cblxuICB1cGRhdGUoKSB7XG4gICAgaWYgKHRoaXMuaXNQbGF5aW5nKSB7XG4gICAgICBsZXQgY3VyclRpbWUgPSAoKG5ldyBEYXRlKCkpLmdldFRpbWUoKSkgLyAxMDAwLjA7XG4gICAgICBsZXQgdERlbHRhID0gY3VyclRpbWUgLSB0aGlzLmxhc3RVcGRhdGU7XG4gICAgICB0aGlzLnBvcyArPSB0RGVsdGE7XG4gICAgICB0aGlzLmxhc3RVcGRhdGUgPSBjdXJyVGltZTtcbiAgICAgIHRoaXMudGltZUJhbm5lci5pbm5lckhUTUwgPSBNYXRoLnJvdW5kKHRoaXMucG9zICogMTAwKSAvIDEwMC4wO1xuICAgIH1cbiAgICBpZiAodGhpcy5wb3MgPiB0aGlzLnRkLmRhdGEuYW5hbHlzaXMudHJhY2suZHVyYXRpb24pIHtcbiAgICAgIHRoaXMucGxheSA9IGZhbHNlO1xuICAgIH1cbiAgfVxuXG4gIHBsYXkoKSB7XG4gICAgY29uc29sZS5sb2coJ1BsYXkhJyk7XG4gICAgaWYgKCF0aGlzLmlzUGxheWluZykge1xuICAgICAgdGhpcy5pc1BsYXlpbmcgPSB0cnVlO1xuICAgICAgdGhpcy5sYXN0VXBkYXRlID0gKChuZXcgRGF0ZSgpKS5nZXRUaW1lKCkpIC8gMTAwMC4wO1xuICAgIH1cbiAgfVxuXG4gIHBhdXNlKCkge1xuICAgICAgY29uc29sZS5sb2coJ1BhdXNlIScpO1xuICAgIGlmICh0aGlzLmlzUGxheWluZykge1xuICAgICAgdGhpcy5pc1BsYXlpbmcgPSBmYWxzZTtcbiAgICB9XG4gIH1cblxuICB1cGRhdGVUaW1lKCkge1xuICAgIGxldCBlbGVtID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3RpbWUtaW5wdXQnKTtcbiAgICB0aGlzLnBvcyA9IHBhcnNlRmxvYXQoZWxlbS52YWx1ZSk7XG4gIH1cblxuICBkcmF3KCkge1xuICAgIHRoaXMudXBkYXRlKCk7XG4gICAgdGhpcy5jdHguY2xlYXJSZWN0KDAsIDAsIHRoaXMud2lkdGgsIHRoaXMuaGVpZ2h0KTtcbiAgICB0aGlzLmRyYXdCZWF0cygpO1xuICAgIHRoaXMuZHJhd0JhcnMoKTtcbiAgICB0aGlzLmRyYXdTZWdtZW50cygpO1xuICAgIHRoaXMuZHJhd0N1cnJQb3MoKTtcbiAgfVxufVxuXG5cblxuLy8gV0VCUEFDSyBGT09URVIgLy9cbi8vIHN0YXRpYy9UcmFja1Zpcy5qc3giXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUE7QUFDQTs7O0FBQUE7QUFDQTs7Ozs7OztBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFBQTtBQUNBO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBOzs7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7OztBQUVBO0FBQ0E7QUFDQTs7O0FBRUE7QUFDQTtBQUNBOzs7QUFFQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7OztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7OztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7OztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7OztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7OztBQUVBO0FBQ0E7QUFDQTtBQUNBOzs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7Ozs7QUEvSkEiLCJzb3VyY2VSb290IjoiIn0=");

/***/ }),
/* 4 */
/* unknown exports provided */
/* all exports used */
/*!****************************!*\
  !*** ./static/Segment.jsx ***!
  \****************************/
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nObject.defineProperty(exports, \"__esModule\", {\n  value: true\n});\n\nvar _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nvar Segment = function () {\n  function Segment(data, yOffset, maxDB) {\n    _classCallCheck(this, Segment);\n\n    this.data = data;\n    this.yOffset = yOffset;\n    this.height = 140;\n    this.minDB = -60.0;\n    this.maxDB = maxDB;\n  }\n\n  _createClass(Segment, [{\n    key: \"calcLoudnessY\",\n    value: function calcLoudnessY() {\n      var range = this.maxDB - this.minDB;\n      var relY = (this.data.loudness_max - this.minDB) / range * this.height;\n      return this.yOffset + (this.height - relY);\n    }\n  }, {\n    key: \"drawSelf\",\n    value: function drawSelf(trackVis) {\n      var ctx = trackVis.ctx;\n      var x = trackVis.x(this.data.start - trackVis.pos);\n      var width = trackVis.timeToPixels(this.data.duration) - 1;\n      if (x < -150 || x > trackVis.width) return;\n      var max_time = trackVis.timeToPixels(this.data.loudness_max_time);\n      var loud_y = this.calcLoudnessY();\n      ctx.beginPath();\n      ctx.rect(x, this.yOffset, width, this.height);\n      ctx.fillRect(x + max_time, loud_y, 6, 6);\n      ctx.closePath();\n      ctx.stroke();\n    }\n  }]);\n\n  return Segment;\n}();\n\nexports.default = Segment;//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiNC5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvU2VnbWVudC5qc3g/MThjNCJdLCJzb3VyY2VzQ29udGVudCI6WyJleHBvcnQgZGVmYXVsdCBjbGFzcyBTZWdtZW50IHtcbiAgY29uc3RydWN0b3IoZGF0YSwgeU9mZnNldCwgbWF4REIpIHtcbiAgICB0aGlzLmRhdGEgPSBkYXRhO1xuICAgIHRoaXMueU9mZnNldCA9IHlPZmZzZXQ7XG4gICAgdGhpcy5oZWlnaHQgPSAxNDA7XG4gICAgdGhpcy5taW5EQiA9IC02MC4wO1xuICAgIHRoaXMubWF4REIgPSBtYXhEQjtcbiAgfVxuXG4gIGNhbGNMb3VkbmVzc1koKSB7XG4gICAgbGV0IHJhbmdlID0gdGhpcy5tYXhEQiAtIHRoaXMubWluREI7XG4gICAgbGV0IHJlbFkgPSAoKHRoaXMuZGF0YS5sb3VkbmVzc19tYXggLSB0aGlzLm1pbkRCKSAvIHJhbmdlKSAqIHRoaXMuaGVpZ2h0O1xuICAgIHJldHVybiB0aGlzLnlPZmZzZXQgKyAodGhpcy5oZWlnaHQgLSByZWxZKTtcbiAgfVxuXG5cbiAgZHJhd1NlbGYodHJhY2tWaXMpIHtcbiAgICBsZXQgY3R4ID0gdHJhY2tWaXMuY3R4O1xuICAgIGxldCB4ID0gdHJhY2tWaXMueCh0aGlzLmRhdGEuc3RhcnQgLSB0cmFja1Zpcy5wb3MpO1xuICAgIGxldCB3aWR0aCA9IHRyYWNrVmlzLnRpbWVUb1BpeGVscyh0aGlzLmRhdGEuZHVyYXRpb24pIC0gMTtcbiAgICBpZiAoeCA8IC0xNTAgfHwgeCA+IHRyYWNrVmlzLndpZHRoKSByZXR1cm47XG4gICAgbGV0IG1heF90aW1lID0gdHJhY2tWaXMudGltZVRvUGl4ZWxzKHRoaXMuZGF0YS5sb3VkbmVzc19tYXhfdGltZSk7XG4gICAgbGV0IGxvdWRfeSA9IHRoaXMuY2FsY0xvdWRuZXNzWSgpO1xuICAgIGN0eC5iZWdpblBhdGgoKTtcbiAgICBjdHgucmVjdCh4LCB0aGlzLnlPZmZzZXQsIHdpZHRoLCB0aGlzLmhlaWdodCk7XG4gICAgY3R4LmZpbGxSZWN0KHggKyBtYXhfdGltZSwgbG91ZF95LCA2LDYpO1xuICAgIGN0eC5jbG9zZVBhdGgoKTtcbiAgICBjdHguc3Ryb2tlKCk7XG4gIH1cbn1cblxuXG5cbi8vIFdFQlBBQ0sgRk9PVEVSIC8vXG4vLyBzdGF0aWMvU2VnbWVudC5qc3giXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7QUFBQTtBQUNBO0FBQUE7QUFDQTtBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFHQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7Ozs7O0FBNUJBIiwic291cmNlUm9vdCI6IiJ9");

/***/ })
/******/ ]);