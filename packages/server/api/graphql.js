const express = require('express');
const mongoose = require('mongoose');
const Recipe = require('./models/recipe');
const { ApolloServer, gql } = require('apollo-server-express');
require('dotenv').config();

const MONGODB_USER = process.env.DB_USER;
const MONGODB_PASSWORD = process.env.DB_PASSWORD;
const MONGO_DB_CONNECTION_URI = `mongodb://${MONGODB_USER}:${MONGODB_PASSWORD}@ds363118.mlab.com:63118/pickleheads-cookbook`;

const typeDefs = gql`
  input RecipeInput {
    servings: Int
    prepTime: String
    cookTime: String
    ingredients: [IngredientInput]
    steps: [String]
    links: [String]
    name: String
  }
  input IngredientInput {
    unit: String!
    quantity: Int!
    name: String!
  }
  type Ingredient {
    unit: String!
    quantity: Int!
    name: String!
  }
  type Recipe {
    servings: Int!
    prepTime: String
    cookTime: String
    ingredients: [Ingredient!]
    steps: [String!]
    links: [String]
    name: String!
  }
  type Query {
    recipes: [Recipe]
  }
  type Mutation {
    createRecipe(input: RecipeInput): Recipe
  }
`;

const resolvers = {
  Query: {
    recipes: () => Recipe.find({}).lean().exec(),
  },
  Mutation: {
    createRecipe: (parent, args) => Recipe.create(args.input),
  },
};

mongoose.connect(MONGO_DB_CONNECTION_URI);

const app = express();
const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true,
  playground: true,
});
server.applyMiddleware({ app, path: '/', cors: true });

module.exports = app;
