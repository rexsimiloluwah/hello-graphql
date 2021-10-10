"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _path = _interopRequireDefault(require("path"));

var _express = _interopRequireDefault(require("express"));

var _schema = _interopRequireDefault(require("./schema"));

var _resolvers = _interopRequireDefault(require("./resolvers"));

var _expressGraphql = require("express-graphql");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var app = (0, _express["default"])();
/* Middlewares */

app.use(_express["default"].json());
app.use(_express["default"]["static"](_path["default"].join(__dirname, 'public')));
/* Root resolver */

var root = _resolvers["default"];
/* Use the express Graphql middleware */

app.use('/graphql', (0, _expressGraphql.graphqlHTTP)({
  schema: _schema["default"],
  rootValue: root,
  graphiql: true
}));
app.use(function (req, res, next) {
  return res.status(404).json({
    message: "Could not find specified route."
  });
});
var _default = app;
exports["default"] = _default;