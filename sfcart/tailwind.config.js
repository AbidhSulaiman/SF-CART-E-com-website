/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html',
    './products/templates/**/*.html',
    './carts/templates/**/*.html',
  ],

  theme: {
    extend: {
      colors: {
        'category-color': '#00b4d8',
      },
    },
  },
  plugins: [],
}

