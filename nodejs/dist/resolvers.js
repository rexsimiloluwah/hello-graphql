"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _pgClient = _interopRequireDefault(require("./db/pgClient"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var getProjects = function getProjects() {
  return _pgClient["default"].query('SELECT * FROM projects').then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var getProject = function getProject(_ref) {
  var id = _ref.id;
  var query = 'SELECT * FROM projects WHERE id=$1';
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var getUsers = function getUsers() {
  return _pgClient["default"].query('SELECT * FROM users').then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var getUser = function getUser(_ref2) {
  var id = _ref2.id;
  var query = 'SELECT * FROM users WHERE id=$1';
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var getProjectsByCategory = function getProjectsByCategory(_ref3) {
  var category = _ref3.category;
  var query = 'SELECT * FROM projects WHERE category=$1';
  var values = [category];
  return _pgClient["default"].query(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var createProject = function createProject(_ref4) {
  var input = _ref4.input;
  var title = input.title,
      description = input.description,
      link = input.link,
      category = input.category,
      tags = input.tags,
      likes = input.likes,
      userId = input.userId;
  var query = 'INSERT INTO projects (title,description,link,category,tags,likes,userId, createdAt) VALUES ($1,$2,$3,$4,$5,$6,$7,$8) RETURNING *';
  var values = [title, description, link, category, tags, likes || 0, userId, new Date().toISOString()];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var deleteProject = function deleteProject(_ref5) {
  var id = _ref5.id;
  var query = 'DELETE FROM projects WHERE id=$1 RETURNING *';
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var registerUser = function registerUser(_ref6) {
  var input = _ref6.input;
  var name = input.name,
      email = input.email,
      password = input.password,
      phone = input.phone,
      profile = input.profile,
      bio = input.bio;
  var query = 'INSERT INTO users (name,email,password,phone,profile,bio) VALUES ($1,$2,$3,$4,$5,$6) RETURNING *';
  var values = [name, email, password, phone, JSON.stringify(profile), bio];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.log(error);
    return error;
  });
};

var deleteUser = function deleteUser(_ref7) {
  var id = _ref7.id;
  var query = 'DELETE FROM users WHERE id=$1 RETURNING *';
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var updateUser = function updateUser(_ref8) {
  var id = _ref8.id,
      input = _ref8.input;
  var dynamicFields = Object.keys(input).map(function (item) {
    return "".concat(item, "='").concat(input[item], "'");
  }).join();
  var query = "UPDATE users SET ".concat(dynamicFields, " WHERE id=$1 RETURNING *");
  console.log(id, query);
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var updateProject = function updateProject(_ref9) {
  var id = _ref9.id,
      input = _ref9.input;
  var dynamicFields = Object.keys(input).map(function (item) {
    return "".concat(item, "='").concat(input[item], "'");
  }).join();
  var query = "UPDATE projects SET ".concat(dynamicFields, " WHERE id=$1 RETURNING *");
  console.log(id, query);
  var values = [id];
  return _pgClient["default"].one(query, values).then(function (res) {
    console.log(res);
    return res;
  })["catch"](function (error) {
    console.error(error);
    return error;
  });
};

var resolvers = {
  projects: getProjects,
  project: getProject,
  user: getUser,
  users: getUsers,
  projectsByCategory: getProjectsByCategory,
  createProject: createProject,
  deleteProject: deleteProject,
  registerUser: registerUser,
  deleteUser: deleteUser,
  updateUser: updateUser,
  updateProject: updateProject
};
var _default = resolvers;
exports["default"] = _default;