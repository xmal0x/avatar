import { useEffect, useRef } from "react"
import { Message as MessageInterface } from "../../api/chatApi"
import Message from "../Message/Message"

interface Props {
  messages: MessageInterface[]
  loading: boolean
}

const MessageList = ({ messages, loading }: Props) => {
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" })
    }
  }, [messages])

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10, overflow: 'auto', height: '500px', marginBottom: 20, border: '1px solid #d0d7de', borderRadius: 12, padding: 10 }}>
      {messages.map((msg) => (
        <Message key={msg.id} message={msg} />
      ))}
      <div ref={messagesEndRef} />
      {loading && <div style={{ opacity: 0.6 }}>thinking...</div>}
    </div>
  )
}

export default MessageList