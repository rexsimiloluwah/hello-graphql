import db from './db/pgClient';

const getProjects = () => {
    return db.query('SELECT * FROM projects')
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        });
}

const getProject = ({ id }) => {
    const query = 'SELECT * FROM projects WHERE id=$1';
    const values = [id];
    return db.one(query, values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const getUsers = () => {
    return db.query('SELECT * FROM users')
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const getUser = ({ id }) => {
    const query = 'SELECT * FROM users WHERE id=$1';
    const values = [id]
    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const getProjectsByCategory = ({ category }) => {
    const query = 'SELECT * FROM projects WHERE category=$1';
    const values = [category];
    return db.query(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const createProject = ({ input }) => {
    const {title,description,link,category,tags,likes,userId} = input;
    const query ='INSERT INTO projects (title,description,link,category,tags,likes,userId, createdAt) VALUES ($1,$2,$3,$4,$5,$6,$7,$8) RETURNING *';
    const values = [
        title,
        description,
        link,
        category,
        tags,
        likes || 0,
        userId,
        new Date().toISOString()
    ]

    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const deleteProject = ({ id }) => {
    const query = 'DELETE FROM projects WHERE id=$1 RETURNING *';
    const values = [id];
    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const registerUser = ({ input }) => {
    const {name,email,password,phone,profile,bio} = input;
    const query = 'INSERT INTO users (name,email,password,phone,profile,bio) VALUES ($1,$2,$3,$4,$5,$6) RETURNING *';
    const values = [
        name,
        email,
        password,
        phone,
        JSON.stringify(profile),
        bio
    ]

    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.log(error);
            return error;
        })
}

const deleteUser = ({ id }) => {
    const query = 'DELETE FROM users WHERE id=$1 RETURNING *';
    const values = [id];
    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const updateUser = ({id,input}) => {
    const dynamicFields = Object.keys(input).map(item => `${item}='${input[item]}'`).join();
    const query = `UPDATE users SET ${dynamicFields} WHERE id=$1 RETURNING *`;
    console.log(id, query)
    const values = [id];
    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const updateProject = ({id,input}) => {
    const dynamicFields = Object.keys(input).map(item => `${item}='${input[item]}'`).join();
    const query = `UPDATE projects SET ${dynamicFields} WHERE id=$1 RETURNING *`;
    console.log(id, query)
    const values = [id];
    return db.one(query,values)
        .then(res => {
            console.log(res);
            return res;
        })
        .catch(error => {
            console.error(error);
            return error;
        })
}

const resolvers = {
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
    updateProject: updateProject,
}

export default resolvers;