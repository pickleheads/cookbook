const mongoose = require('mongoose');
const { Schema } = mongoose;

const schema = new Schema(
  {
    servings: {
      type: String,
      required: true,
    },
    prepTime: String,
    cookTime: String,
    ingredients: [
      {
        type: String,
        required: true,
      }
    ],
    steps: [
      {
        type: String,
        required: true,
      },
    ],
    link: String,
    name: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const model = mongoose.model('Recipe', schema);

module.exports = model;
