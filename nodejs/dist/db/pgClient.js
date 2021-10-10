"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _config = _interopRequireDefault(require("./config"));

var _pgPromise = _interopRequireDefault(require("pg-promise"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

// PostGreSQL Database Client 
var pgp = (0, _pgPromise["default"])({});
var db = pgp(_config["default"]);
var _default = db;
exports["default"] = _default;