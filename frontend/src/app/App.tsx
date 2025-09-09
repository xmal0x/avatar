import { useState } from 'react'
import { chatApi } from '../features/chat/api/chatApi'

export default function App() {
  const [message, setMessage] = useState<string>('')
  const [answer, setAnswer] = useState<string[]>([])

  const sendMessage = async (message: string) => {
    setMessage('')
    setAnswer(prev => [...prev, message])
    const response = await chatApi.send({ message })
    setAnswer(prev => [...prev, response.result])
  }

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 24 }}>
      {answer.map((a, index) => (
        <p key={index}>{a}</p>
      ))}
      <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendMessage(message)} />
      <button onClick={() => sendMessage(message)}>Answer</button>
    </div>
  )
}
