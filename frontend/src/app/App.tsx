import { useState } from 'react'
import { useChatStore } from '../features/chat/store/chatStore';

export default function App() {
  const [message, setMessage] = useState<string>('')
  const { messages, loading, error, send } = useChatStore();

  const sendMessage = (message: string) => {
    send(message)
    setMessage('')
  }

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 24 }}>
      {messages.map((a, index) => (
        <p key={index}>{a.role === 'user' ? 'You: ' : 'Assistant: '}{a.message}</p>
      ))}
      <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendMessage(message)} />
      <button onClick={() => sendMessage(message)} disabled={loading}>Answer</button>
      {error && <p>{error}</p>}
    </div>
  )
}
