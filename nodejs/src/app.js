import path from 'path';
import express from 'express';
import schema from './schema';
import resolvers from './resolvers';
import {graphqlHTTP} from 'express-graphql'

const app = express();

/* Middlewares */
app.use(express.json());
// For serving static files 
app.use('/docs',express.static(path.join(__dirname, '../public')));

/* Root resolver */
const root = resolvers;

/* Use the express Graphql middleware */
app.use('/graphql', graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true
}))

app.use((req,res,next) => {
    return res.status(404).json({
        message: "Could not find specified route."
    })
})


export default app;