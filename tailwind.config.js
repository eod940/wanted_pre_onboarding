/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.{js,html}',
      './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('flowbite/plugin')
  ],
}
