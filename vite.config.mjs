import { defineConfig } from 'vite'
import {resolve} from 'path'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  root: './',
  base: '/static/',
  plugins: [tailwindcss()],
  build: {
    manifest: "manifest.json",
    outDir: resolve("./static/build"),
    rollupOptions: {
      input: resolve('./static/src/js/main.js')
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './static'),
    },
  },
})