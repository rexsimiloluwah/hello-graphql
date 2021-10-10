"use strict";

var _pgClient = _interopRequireDefault(require("./pgClient"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

_pgClient["default"].query("SELECT * FROM users").then(function (res) {
  console.log(res);
});