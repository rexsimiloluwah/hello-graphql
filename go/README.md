1. To initialize the project 
```bash
$ go run github.com/99designs/gqlgen init 
```

2. To regenerate the models (from the defined schema)
```bash
$ go run github.com/99designs/gqlgen generate
```

Test Mutation 
```bash
mutation createTweet{
  createTweet(input:{content:"Test Tweet 1",userId:"1"}){
    user{
      id
    },
    content, 
    likes_count, 
    retweets_count
  }
} 
```

Test Query 
```bash
query{
  tweets{
    id,
    user{
      id
    },
    content,
    likes_count, 
    retweets_count
  }
} 
```