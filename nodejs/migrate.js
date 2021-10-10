const {migrate} = require('postgres-migrations');
const dotenv = require('dotenv');

dotenv.config();

const dbConfig = {
    database: process.env.POSTGRES_DATABASE_NAME,
    user: process.env.POSTGRES_USERNAME,
    password: process.env.POSTGRES_PASSWORD,
    host: process.env.POSTGRES_HOST,
    port: parseInt(process.env.POSTGRES_PORT),
    ensureDatabaseExists: true
}

console.log(dbConfig)

const runMigrations = async() => {
    await migrate(dbConfig, "./migrations");
}

runMigrations();