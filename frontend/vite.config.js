import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  optimizeDeps: {
    exclude: ['hardhat', '@nomicfoundation/hardhat-toolbox']
  },
  publicDir: './src/public'
})
