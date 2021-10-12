## A simple, idiomatic GraphQL server template using Node.js and Express framework

### Overview 
This is my first CRUD-based GraphQL server after learning about the wonderful GraphQL query language for a while. I believe this can serve as a template or guide for beginners like me getting started with implementing GraphQL using Node.js and JavaScript.

### Requirements 
1. [Node.js](https://nodejs.org/en/) installed on MAC,Windows, or Linux
2. [PostGreSQL](https://www.postgresql.org/) database server installed on your machine 
3. IDE or text editor i.e. VSCode 
4. Foundational Knowledge of Node.js and JavaScript 

### Setup
1. Clone the Github repository 
```bash
$ git clone http://github.com/rexsimiloluwah/hello-graphql.git
$ cd nodejs 
```
2. Install dependencies 
```bash
$ npm install 
```
3. Environment variables <br>
Create a `.env` file, and add the content of the `.env.sample` file into it, with your modified credentials.

4. Database Migrations <br>
The `postgres-migrations` library was used to facilitate database migrations for creating tables and inserting dummy data.

```bash
$ npm run migrate
```

*The SQL files for migration are available in the `/migrations` folder.

5. Start the GraphQL server 
```bash
$ npm run dev
```
<br>

<h4>The server is successfully running on http://localhost:5000 🎉🎉</h4>

## Main endpoints 
| Route   | Description |
| ----------- | ----------- |
| **/graphql**     | Access GraphiQL interface for testing queries and mutations       |
| **/docs**  | Access GraphQL API documentation, The docs were generated using the amazing `SpectaQL` tool.       |

### Documentation 
The interactive documentation was generated using [SpectaQL](https://github.com/anvilco/spectaql), kindly check it out.

Access documentation on http://localhost:5000/docs 
<img src="https://github.com/rexsimiloluwah/hello-graphql/nodejs/images/graphql-docs.png" alt="GraphQL docs">

### Simple overview of the GraphQL API 
The API is a simple one for managing projects. It provides CRUD functionality for users to manage accounts and projects. Authentication and authorization middlewares were not implemented to keep the scope of the project simple. 

### Examples 
#### 1. Get all Projects
***Query*** 
```bash
query{
  projects{
    id 
    title 
    description
    category 
    tags 
    likes 
    userId
    createdAt
  }
}
```

***Response*** 
```json
{
  "data": {
    "projects": [
      {
        "id": 1,
        "title": "scrapix-cli-v2",
        "description": "Node.js + TypeScript based image scraping CLI",
        "category": "CLI",
        "tags": [
          "Node.js",
          "TypeScript",
          "ImageScraping"
        ],
        "likes": 0,
        "userId": 1,
        "createdAt": "2021-10-12T15:14:25.359Z"
      }
    ]
  }
}
```

#### 2. Get all users  
***Query***
```bash
query{
  users{
    id 
    name
    email 
    bio 
    profile{
      github 
      gravatar 
      twitter
      location 
      linkedin
    }
  }
}
```

***Response***
```json
{
  "data": {
    "users": [
      {
        "id": 1,
        "name": "Similoluwa Okunowo",
        "email": "rexsimiloluwa@gmail.com",
        "bio": "Crazy Guy",
        "profile": {
          "github": "https://github.com/rexsimiloluwah",
          "gravatar": null,
          "twitter": "https://twitter.com/__ademola__",
          "location": "Lagos, Nigeria",
          "linkedin": "linkedin.com/in/similoluwa-okunowo"
        }
      },
      {
        "id": 3,
        "name": "Moyo Adepeju",
        "email": "moyo.adepeju@gmail.com",
        "bio": "Baby girl",
        "profile": {
          "github": "https://github.com/moyo",
          "gravatar": null,
          "twitter": null,
          "location": "Badagry, Lagos.",
          "linkedin": null
        }
      },
      {
        "id": 2,
        "name": "Sope Okunowo",
        "email": "sops@gmail.com",
        "bio": "Cool Guy | Finance",
        "profile": {
          "github": null,
          "gravatar": null,
          "twitter": "https://twitter.com/sopeseven",
          "location": "Ile-ife, Nigeria",
          "linkedin": "linkedin.com/in/sope-okunowo"
        }
      }
    ]
  }
}
```

### 3. Create new Project 
***Mutation***
```bash
mutation{
  registerUser(input:{
    name:"Salami Malcolm",
    email:"ayfabulous@gmail.com",
    password:"adetoyosi",
    phone:"07023003029",
    profile:{github:"https://github.com/malcolmx",location:"San-Francisco"},
    bio:"Crazy Guy"
  }){
    id 
    name 
    email
    profile {
      gravatar
      github
      twitter
      location
      linkedin
    }
  }
}
```

***Response***
```json
{
  "data": {
    "registerUser": {
      "id": 5,
      "name": "Salami Malcolm",
      "email": "ayfabulous@gmail.com",
      "profile": {
        "gravatar": null,
        "github": "https://github.com/malcolmx",
        "twitter": null,
        "location": "San-Francisco",
        "linkedin": null
      }
    }
  }
}
```

### 4. Create new Project 
***Mutation***
```bash
mutation{
  createProject(input:{
    title:"Test Project",
    description:"Test Project Description",
    category:MACHINE_LEARNING,
    link: "https://github.com/test-project",
    tags:["Image Segmentation","Machine learning","Computer Vision"],
    userId: 5
  }){
    id 
    title 
    description 
    tags 
  }
}
```

***Response***
```json
{
  "data": {
    "createProject": {
      "id": 3,
      "title": "Test Project",
      "description": "Test Project Description",
      "tags": [
        "Image Segmentation",
        "Machine learning",
        "Computer Vision"
      ]
    }
  }
}
```

## Checkout out other examples in the documentation at `https://localhost:5000/docs`