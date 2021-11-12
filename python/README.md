Hello-GraphQL (python version)
> A simple and idiomatic boilerplate for rapidly building GraphQL APIs using `Python`,`Flask`,`Graphene`,`MySQL`, and `SQLAlchemy` ORM. Built for absolute beginners.

## Requirements 
- Python 3.x
- [Docker](https://docs.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/)
- Any MySQL server 
- GraphQL API Testing tool i.e. Postman, Insomnia

## High-level directory structure 
    .
    ├── ...
    ├── `app`                   
    │   ├── `api`
        |   ├── objects.py   # GraphQL SQLAlchemy Object types          
        |   └── schema.py    # Schema file for queries and mutations using graphene        
    │   ├── main.py          # Main flask app configuration                  
    │   └── models.py        # SQLAlchemy models    
    ├── `config.py`          # Flask config file 
    ├── `docker-compose.yml` # Docker compose file
    ├── `Dockerfile`         # Dockerfile
    ├── `run.py`             # Run the flask server
    ├── `.env`               # Yeah, environment variables  
    └── ...

## Run (without Docker)

1. Clone the repository, setup virtual environment and install dependencies
```bash
$ git clone https://github.com/rexsimiloluwah/hello-graphql.git && cd python 
$ python3 -m venv env && source activate env/bin/activate 
$ pip install -r requirements.txt
```

2. Run the server 
```bash
$ python3 run.py
```

3. Testing 
Access the `GraphiQL` web interface at `http://localhost:5000/graphql` to test queries and mutations. Sample queries and mutations are available in the `app/test.txt` file. 

## Run with Docker 

To run the flask server and mysql database services using docker compose: 

```bash
$ sudo docker-compose up
```

## Test Queries and Mutations 
1. Create a new user 
```bash
mutation{
    createUser(name:"Similoluwa Okunowo",username:"rexidic",email:"rexsimiloluwa@gmail.com",password:"password-2001",bio:"Crazy dude | Sofware Engineer"){
        user{
            id,
            name,
            username,
            email,
            createdAt
        }
    }
}
```

2. Login the user to get access_token and refresh_token 
```bash
mutation{
  loginUser(email:"rexsimiloluwa@gmail.com",password:"password-2001"){
    user{
      id,
      email,
      name,
      username,
      createdAt,
    },
    accessToken,
    refreshToken
  }
}
```

3. Create a new post (requires Bearer token for auth)
```bash
mutation{
  addPost(title:"Test title 2",category:"Test category 2",content:"Test content 2",tags:["tag1","tag2"],){
    post{
      __typename 
      ... on Post{
        id,
        title
      }
      __typename
      ... on AuthInfoField{
          message
      }
      
    }
  }
}
```
..... 


> Yeah, too lazy to write a proper documentation. But, I think this is usable. 