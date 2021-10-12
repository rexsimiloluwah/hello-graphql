import {buildSchema} from 'graphql';

const schema = buildSchema(`
    enum ProjectCategory{
        WEB 
        MOBILE 
        API 
        DATA_SCIENCE 
        MACHINE_LEARNING 
        BLOCKCHAIN 
        EMBEDDED_SYSTEMS 
        DESIGN
        CLI
        SDK
    }

    type User {
        id: Int
        name: String
        email: String!
        password: String
        phone: String
        profile: UserProfile
        bio: String 
    }

    type UserProfile {
        gravatar: String
        github: String
        twitter: String
        location: String 
        linkedin: String 
    }

    type Project {
        id: Int
        title: String!
        description: String!
        link: String
        category: ProjectCategory!
        tags: [String]
        likes: Int
        userId: Int
        createdAt: Int
    }

    input ProjectInput {
        title: String,
        description: String,
        category: ProjectCategory
        tags: [String]
        link: String
        userId : Int
    }

    input UserInput {
        name: String
        email: String 
        password: String
        phone: String
        profile: UserProfileInput
        bio: String 
    }

    input UserProfileInput {
        gravatar: String
        github: String
        twitter: String
        location: String 
        linkedin: String 
    }

    type Query {
        project(id: Int):Project 
        projects:[Project] 
        projectsByCategory(category:ProjectCategory):[Project]
        users:[User]
        user(id: Int): User
    }

    type Mutation {
        createProject(input:ProjectInput):Project 
        registerUser(input:UserInput):User
        deleteProject(id:Int):Project 
        deleteUser(id:Int):User 
        updateUser(id:Int,input:UserInput):User
        updateProject(id:Int,input:ProjectInput):Project
    }

`)

export default schema;