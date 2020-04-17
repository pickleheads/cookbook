const mongoose = require('mongoose');
const { Schema } = mongoose;

const unitEnums = [
  "teaspoon",
  "tablespoon",
  "fluid_ounce",
  "gill",
  "cup",
  "pint",
  "quart",
  "gallon",
  "millilitre",
  "litre",
  "decilitre",
  "pound",
  "ounce",
  "milligram",
  "gram",
  "killogam",
  "millimetre",
  "centimetre",
  "metre",
  "inch"
];

const schema = new Schema(
  {
    servings: {
      type: Number,
      required: true,
    },
    prepTime: String,
    cookTime: String,
    ingredients: [{
      unit: {
        type: String,
        enum: unitEnums,
        required: true
      },
      quantity: {
        type: Number,
        required: true
      },
    }],
    steps: [
      {
        type: String,
        required: true,
      },
    ],
    links: [String],
    name: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const model = mongoose.model('Recipe', schema);

module.exports = model;
