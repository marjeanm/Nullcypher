// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
    "./components/**/*.{html,js}", // ← ADD THIS
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
