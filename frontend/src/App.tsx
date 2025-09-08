import { useState } from 'react'
import { apiMessage } from './api'

export default function App() {
  const [message, setMessage] = useState<string>('…')
  const [answer, setAnswer] = useState<string>('…')

  const sendMessage = async (message: string) => {
    const response = await apiMessage(message)
    setAnswer(response.result)
  }

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 24 }}>
      <p>{answer}</p>
      <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={() => sendMessage(message)}>Answer</button>
    </div>
  )
}
