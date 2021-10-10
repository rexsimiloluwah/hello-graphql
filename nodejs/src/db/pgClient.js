// PostGreSQL Database Client 
import dbConfig from './config';
import pgPromise from 'pg-promise';

const pgp = pgPromise({});
const db = pgp(dbConfig);

export default db;