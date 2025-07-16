// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  theme: {
    extend: {
      colors: {
        nulldark: "#121212",
        nullaccent: "#FF3CAC",
        nullpulse: "#784BA0",
      },
    },
  },
  plugins: [],
};
