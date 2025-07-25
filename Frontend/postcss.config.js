// postcss.config.js
import tailwindcss from '@tailwindcss/postcss';
import autoprefixer from 'autoprefixer';

export default {
  plugins: [
    tailwindcss(),  // ✅ NEW plugin for Tailwind 4+
    autoprefixer(),
  ],
};
