import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// базовый конфиг dev-сервера
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // 0.0.0.0 внутри контейнера
    port: Number(process.env.FRONTEND_PORT || 5173)
  }
})
