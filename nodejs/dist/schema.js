"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _graphql = require("graphql");

var schema = (0, _graphql.buildSchema)("\n    enum ProjectCategory{\n        WEB \n        MOBILE \n        API \n        DATA_SCIENCE \n        MACHINE_LEARNING \n        BLOCKCHAIN \n        EMBEDDED_SYSTEMS \n        DESIGN\n        CLI\n        SDK\n    }\n\n    type User {\n        id: Int\n        name: String\n        email: String!\n        password: String\n        phone: String\n        profile: UserProfile\n        bio: String \n    }\n\n    type UserProfile {\n        gravatar: String\n        github: String\n        twitter: String\n        location: String \n        linkedin: String \n    }\n\n    type Project {\n        id: Int\n        title: String!\n        description: String!\n        link: String\n        category: ProjectCategory!\n        tags: [String]\n        likes: Int\n        user: User!\n        createdAt: Int\n    }\n\n    input ProjectInput {\n        title: String,\n        description: String,\n        category: ProjectCategory\n        tags: [String]\n        link: String\n        userId : Int\n    }\n\n    input UserInput {\n        name: String\n        email: String \n        password: String\n        phone: String\n        profile: UserProfileInput\n        bio: String \n    }\n\n    input UserProfileInput {\n        gravatar: String\n        github: String\n        twitter: String\n        location: String \n        linkedin: String \n    }\n\n    type Query {\n        project(id: Int):Project \n        projects:[Project] \n        projectsByCategory(category:ProjectCategory):[Project]\n        users:[User]\n        user(id: Int): User\n    }\n\n    type Mutation {\n        createProject(input:ProjectInput):Project \n        registerUser(input:UserInput):User\n        deleteProject(id:Int):Project \n        deleteUser(id:Int):User \n        updateUser(id:Int,input:UserInput):User\n        updateProject(id:Int,input:ProjectInput):Project\n    }\n\n");
var _default = schema;
exports["default"] = _default;