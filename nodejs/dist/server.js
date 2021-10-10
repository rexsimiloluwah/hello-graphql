"use strict";

var _app = _interopRequireDefault(require("./app"));

var _http = _interopRequireDefault(require("http"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var server = _http["default"].createServer(_app["default"]);

var PORT = process.env.PORT || 5000;
server.listen(PORT, function () {
  console.log("Server is running on PORT: ".concat(PORT, "."));
});