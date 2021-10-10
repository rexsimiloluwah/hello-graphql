import db from './pgClient';

db.query("SELECT * FROM users")
    .then(res => {
        console.log(res);
    })