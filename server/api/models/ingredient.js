const mongoose = require('mongoose');
const { Schema } = mongoose;

const schema = new Schema(
  {
    name: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const model = mongoose.model('Ingredient', schema);

module.exports = model;
